from enum import Enum
from Cheetah.Template import Template
from ss import ss
from util_template import writeFile
from util_web import *

class TemplateType(Enum):
    CREATE = 1  # create new file
    Modify = 2  # modify file
    SAMPLE = 3  # show some sample code


class CodeFile:
    def __init__(self, path: str = '', content: str = '', templateType=TemplateType.CREATE,
                 handlePath: Callable[[str], str] = None, handleCode: Callable[[str], str] = None):
        self.path = path
        self.content = content
        self.templateType = templateType
        self.handlePath = handlePath
        self.handleCode = handleCode


class CodeTemplate:
    def __init__(self, args: dict = None, files: [CodeFile] = []):
        self.args = args
        self.files = files

    def getCodePreview(self, f: CodeFile) -> str:
        rs = str(Template(source=f.content, namespaces=self.args))

        return rs if (f.handleCode is None) else f.handlePath(rs)

    def getPathPreview(self, f: CodeFile):
        rs = ss(Template(source=f.path, namespaces=self.args)).toPath()

        return rs if (f.handlePath is None) else f.handlePath(rs)

    def showTemplate(self, container=None):
        c = st if container is None else container

        if len(self.args.keys()) > 0:
            cols = c.columns(2)
            for n, k in enumerate(self.args.keys()):
                self.args[k] = cols[n % 2].text_input(ss(k).orange().bold(),
                                                      "" if self.args[k] is None else self.args[k])

        for f in self.files:
            self.showFile(f, c)

    def showFile(self, f: CodeFile, container=None):
        c = st if container is None else container

        c.write(f'#### {ss("path").orange()} {blank(3)} {ss(self.getPathPreview(f)).green()}')

        c.code(self.getCodePreview(f))

    def generateCode(self):
        for f in self.files:
            print(f.path)
            self.generateFile(f)

    def generateFile(self, f: CodeFile):
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
