from __future__ import annotations

from util_template import *


def handlePath(path: str) -> str:
    return path.lower()


args = dict(
    rootPath=None,
    pageName=None,
    testName=None,
)

f1 = CodeFile(
    path=f'$rootPath/page_$[pageName].py',
    handlePath=handlePath,
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
)

f2 = CodeFile(
    path=f'$rootPath/pages/$[pageName]_page.py',
    content='''
import streamlit as st

st.write('This is $[pageName] page')

''',
)

template = CodeTemplate(
    args=args,
    files=[f1, f2],
)
