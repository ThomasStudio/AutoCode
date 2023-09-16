import os.path
from enum import Enum, auto
from Cheetah.Template import Template
from ss import ss
from util_template import writeFile, openFile
from util_web import *
import re
from dataclasses import dataclass


class TemplateType(Enum):
    CREATE = 1  # create new file
    Modify = 2  # modify file
    SAMPLE = 3  # show some sample code


class OperatorType(Enum):
    InsertAfter = auto()
    InsertBefore = auto()
    Replace = auto()


@dataclass
class Operator:
    patt: str = ''
    code: str = ''
    type: OperatorType = OperatorType.InsertAfter


class CodeFile:
    def __init__(self, path: str = '', content: str = '', templateType=TemplateType.SAMPLE, language='python',
                 operators: [Operator] = list(), handlePath: Callable[[str], str] = None,
                 handleCode: Callable[[str], str] = None):
        self.path = path
        self.content = content
        self.templateType: TemplateType = templateType
        self.languate = language

        self.handlePath = handlePath
        self.handleCode = handleCode

        self.operators: [Operator] = operators


class CodeTemplate:
    def __init__(self, args: dict = None, files: [CodeFile] = []):
        self.args = args
        self.files = files

    def getCodePreview(self, f: CodeFile) -> str:
        if f.templateType in [TemplateType.CREATE, TemplateType.SAMPLE]:
            rs = str(Template(source=f.content, namespaces=self.args))
        else:
            rs = self.getModifiedContent(f)

        return rs if (f.handleCode is None) else f.handleCode(rs)

    def getPathPreview(self, f: CodeFile):
        rs = ss(Template(source=f.path, namespaces=self.args)).toPath()

        return rs if (f.handlePath is None) else f.handlePath(rs)

    def getPatt(self, m: Operator):
        return ss(Template(source=m.patt, namespaces=self.args))

    def getCode(self, m: Operator):
        return ss(Template(source=m.code, namespaces=self.args))

    def showTemplate(self, container=None):
        c = st if container is None else container

        if len(self.args.keys()) > 0:
            cols = c.columns(2)
            for n, k in enumerate(self.args.keys()):
                content = "" if self.args[k] is None else self.args[k]
                showArea = '\n' in content

                if showArea:
                    self.args[k] = cols[n % 2].text_area(ss(k).orange(), content)
                else:
                    if cols[n % 2].checkbox(ss(f'↕ {blank(1)} {k}').orange().bold(),
                                            value=showArea):
                        self.args[k] = cols[n % 2].text_area(k, content, label_visibility='collapsed', height=38)
                    else:
                        self.args[k] = cols[n % 2].text_input(k, content, label_visibility='collapsed')

        for f in self.files:
            self.showFile(f, c)

    def showFile(self, f: CodeFile, container=None):
        c = st if container is None else container

        if f.templateType in [TemplateType.CREATE, TemplateType.Modify]:
            c.write(f'#### {ss(f.templateType.name.lower()).orange()} {blank(3)} {ss(self.getPathPreview(f)).green()}')
        elif f.templateType in [TemplateType.SAMPLE]:
            c.write(f'#### {ss("sample").orange()} {blank(3)}')

        c.code(self.getCodePreview(f), language=f.languate)

    def generateCode(self):
        for f in self.files:
            print(f.path)
            self.generateFile(f)

    def generateFile(self, f: CodeFile) -> str:
        if f.templateType not in [TemplateType.CREATE, TemplateType.Modify]:
            print("This is a sample template")
            return

        path = self.getPathPreview(f)
        code = self.getCodePreview(f)

        writeFile(path, code)

    def checkArgs(self) -> bool:
        rs = True
        for k in self.args:
            if self.args[k] is None or len(self.args[k]) == 0:
                st.error(f'{k} cannot be None')
                rs = False

        return rs

    def getModifiedContent(self, f: CodeFile) -> str:

        path = self.getPathPreview(f)

        if not os.path.exists(path):
            return f'File {path}\nnot exists'

        content = openFile(path)
        f.content = content

        for op in f.operators:
            patt, code, type = self.getPatt(op), self.getCode(op), op.type
            print('type : ', type)

            mt = re.findall(rf'''{patt}''', content)

            if len(mt) == 0:
                return content

            mt = mt[0]
            print('mt : ', mt)

            if op.type is OperatorType.InsertBefore:
                content = content.replace(mt, code + mt)
            elif op.type is OperatorType.InsertAfter:
                content = content.replace(mt, mt + code)
            elif op.type is OperatorType.Replace:
                content = content.replace(mt, code)

        f.content = content

        return content
