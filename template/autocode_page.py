from __future__ import annotations

from util_template import *


def handlePath(path: str) -> str:
    return path.lower()


templates = [
    CodeTemplate(
        args=dict(
            rootPath=None,
            pageName=None,
        ),
        path=f'$rootPath/$[pageName]_page.py',
        content='''
from base_page import BasePage

from util_template import *
from util_web import *


class $[pageName](BasePage):
    def __init__(self):
        super().__init__()

    def initData(self):
        pass

    def initUi(self):
        pass
''',
        handlePath=handlePath
    ),

    CodeTemplate(
        args=dict(
            title='this is a example'
        ),
        path='',
        content='''
The title is 
    $title
'''
    )
]
