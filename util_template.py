from __future__ import annotations

import os
from importlib import import_module, reload
from util_web import *

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


def currentTemplate():
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


def writeFile(path: str, content: str):
    try:
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)

        with open(path, 'w', encoding='utf-8') as f:
            print(path)
            print(content)
            f.write(content)

    except Exception as e:
        print('writeFile', e)


def toShowTemplate():
    setSessionState(PageType, ShowTemplate)


def toHomePage():
    setSessionState(PageType, ShowHomePage)


if __name__ == '__main__':
    pass
