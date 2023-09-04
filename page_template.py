from os import popen

from page_base import BasePage
from util_decorator import log
from util_template import *
from util_web import *


class Template(BasePage):

    def __init__(self):
        super().__init__()

        self.templates = []
        self.cmds = []

    def initData(self):
        self.templates = [x for x in os.listdir(TemplateFolder) if x.endswith('.py')]

        self.cmds = [
            ['source', self.showCode],
            ['reload', self.reload],
            ['clone', self.clone],
            ['edit', editCurrentTemplate],
            ['remove', self.remove],
        ]

    def initUi(self):
        c = self.container
        c.write('')

        index = 0
        if hasSessionState(TemplateKey):
            index = self.templates.index(getSessionState(TemplateKey))

        with st.sidebar:
            c0, c1 = st.columns(2)
            c0.button('go home', on_click=toHomePage)
            c1.button('generate', on_click=toGenerateCode)

            st.title(colorText('orange', 'Template list'))

            selected = st.radio(
                TemplateKey,
                self.templates,
                index=index,
                label_visibility='collapsed'
            )

            if len(selected) > 0:
                setSessionState(TemplateKey, selected)
                self.showCmds()

    def showCode(self):
        c = self.container

        c.code(currentSource(), line_numbers=True)

    def showCmds(self):
        c = self.container

        path = currentSourceFile()

        c.title(path)

        cols = c.columns(len(self.cmds))

        for n, (name, f) in enumerate(self.cmds):
            if cols[n].button(name):
                f()

    @log
    def clone(self):
        pass

    @log
    def remove(self):
        pass

    @log
    def reload(self):
        pass
