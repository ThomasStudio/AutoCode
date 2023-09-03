from __future__ import annotations
from enum import Enum
from typing import *
import os
from Cheetah.Template import Template
from util_web import *

TemplateFolder = 'template'

TemplateKey = 'Template'

TemplateArgsKey = 'TemplateArgs'

ShowTemplate = 'ShowTemplate'
GenerateCode = 'GenerateCode'
ShowHomePage = 'ShowHomePage'

PageType = ShowTemplate


def currentTemplate() -> str:
    return getSessionState(TemplateKey)


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
    def __init__(self, templateType=TemplateType.CREATE, content='', path='', args: Dict = None):
        self.type = templateType
        self.content = content
        self.path = path
        self.args = args

    def getCode(self) -> str:
        return str(Template(source=self.content, namespaces=self.args))


def getTemplate(templateType=TemplateType.CREATE, content='', path='', args: Dict = None) -> CodeTemplate:
    return CodeTemplate(templateType, content, path, args)


def getCreateTemplate(content='', path='', args: Dict = None) -> CodeTemplate:
    return getTemplate(TemplateType.CREATE, content, path, args)


def getModifyTemplate(content='', path='', args: Dict = None) -> CodeTemplate:
    return getTemplate(TemplateType.Modify, content, path, args)
