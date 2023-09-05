from __future__ import annotations
from enum import Enum
import os
from Cheetah.Template import Template
from ss import ss
from util_web import *
from importlib import import_module, reload

TemplateFolder = 'template'

TemplateKey = 'Template'

TemplateArgsKey = 'TemplateArgs'

ShowTemplate = 'ShowTemplate'
GenerateCode = 'GenerateCode'
ShowHomePage = 'ShowHomePage'

PageType = ShowTemplate


def currentSourceFile() -> str:
    return getSessionState(TemplateKey)


def editCurrentTemplate():
    cmd = f'code {TemplateFolder}{os.sep}{currentSourceFile()}'
    print(cmd)
    os.popen(cmd)


def currentSource() -> str:
    return openTemplate(currentSourceFile())


def currentTemplate() -> CodeTemplate:
    path = currentSourceFile()
    if path is None:
        return None

    model = path.replace('.py', '')

    t = import_module(model)
    reload(t)

    return t.template


def openTemplate(fName: str) -> str:
    return openFile(f'{TemplateFolder}{os.sep}{fName}')


def openFile(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


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

    def showFile(self, f: CodeFile, container=None):
        c = st if container is None else container

        c.write(f'### {ss("file").orange()} {blank(3)} {ss(self.getPathPreview(f)).green()}')

        c.code(self.getCodePreview(f))


def toShowTemplate():
    setSessionState(PageType, ShowTemplate)


def toHomePage():
    setSessionState(PageType, ShowHomePage)


def toGenerateCode():
    setSessionState(PageType, GenerateCode)


if __name__ == '__main__':
    pass
