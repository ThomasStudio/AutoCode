from code_template import *

args = dict(
    filePath='template\modfy_sample.py',
    newFunBefore='''def testInsertBefore():
    print("testInsertBefore")\n\n\n''',
    newFunAfter='''\n\n\ndef testInsertAfter():
    print("testInsertAfter")\n''',
    newFunReplace='''def testReplace():
    print("testReplace")''',
)

f1 = CodeFile(
    path=f'$filePath',
    templateType=TemplateType.Modify,
    operators=[
        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''$newFunBefore''',
            type=OperatorType.InsertBefore
        ),

        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''$newFunAfter''',
            type=OperatorType.InsertAfter
        ),

        Operator(
            patt='''(def\s*?testFun[\s\S]*?fun'\))''',
            code='''$newFunReplace''',
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
