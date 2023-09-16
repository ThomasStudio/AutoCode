from code_template import *

args = dict(
    filePath='template\modfy_sample.py',
)

f1 = CodeFile(
    path=f'$filePath',
    templateType=TemplateType.Modify,
    operators=[
        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''def testInsertBefore():
    print("testInsertBefore")\n\n\n''',
            type=OperatorType.InsertBefore
        ),

        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''\n\n\ndef testInsertAfter():
    print("testInsertAfter")\n''',
            type=OperatorType.InsertAfter
        ),

        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''def testReplace():
    print("testReplace")''',
            type=OperatorType.Replace
        )

    ]
)

template = CodeTemplate(
    args=args,
    files=[f1],
)


def testFun():
    print('this is test fun')
