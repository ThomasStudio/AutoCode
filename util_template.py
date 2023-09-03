from __future__ import annotations
from enum import Enum
from typing import *
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


def currentTemplate() -> Any:
    path = currentSourceFile()

    model = path.replace('.py', '')

    t = import_module(model)
    reload(t)

    return t


def openTemplate(fName: str) -> str:
    return openFile(f'{TemplateFolder}{os.sep}{fName}')


def openFile(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


class TemplateType(Enum):
    CREATE = 1  # create new file
    Modify = 2  # modify file
    SAMPLE = 3  # show some sample code


class CodeTemplate:
    def __init__(self, templateType=TemplateType.CREATE, content='', path='', args: Dict = None,
                 handlePath: Callable[[str], str] = None, handleCode: Callable[[str], str] = None):
        self.type = templateType
        self.content = content
        self.path = path
        self.args = args

        self.handlePath = handlePath
        self.handleCode = handleCode

    def getCodePreview(self) -> str:
        rs = str(Template(source=self.content, namespaces=self.args))

        return rs if (self.handleCode is None) else self.handlePath(rs)

    def getPathPreview(self):
        rs = ss(Template(source=self.path, namespaces=self.args)).toPath()

        return rs if (self.handlePath is None) else self.handlePath(rs)


def toShowTemplate():
    setSessionState(PageType, ShowTemplate)


def toHomePage():
    setSessionState(PageType, ShowHomePage)


def toGenerateCode():
    setSessionState(PageType, GenerateCode)
