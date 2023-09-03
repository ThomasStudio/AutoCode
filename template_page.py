from importlib import import_module, reload

from base_page import BasePage
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
            ['preview', self.preview],
            ['template', self.showCode],
            ['reload', self.reload],
            ['clone', self.clone],
            ['edit', self.edit],
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
            c0.button('go home', on_click=self.goHome)
            c1.button('generate', on_click=self.generate)

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
        path = currentTemplate()

        c.code(openTemplate(path), line_numbers=True)

    def showCmds(self):
        c = self.container

        path = currentTemplate()

        c.title(path)

        cols = c.columns(len(self.cmds))

        for n, (name, f) in enumerate(self.cmds):
            if cols[n].button(name):
                f()

    @log
    def edit(self):
        pass

    @log
    def clone(self):
        pass

    @log
    def remove(self):
        pass

    @log
    def reload(self):
        pass

    @log
    def preview(self):
        path = st.session_state[TemplateKey]

        model = path.replace('.py', '')

        t = import_module(model)
        reload(t)

        for tl in t.templates:
            self.showTemplage(tl)

    # @st.cache_data
    def showTemplage(self, t: CodeTemplate):
        c = self.container

        if len(t.args.keys()) > 0:
            cols = c.columns(len(t.args.keys()))
            for n, k in enumerate(t.args.keys()):
                t.args[k] = cols[n].text_input(k, t.args[k])
                c.write(t.args)

        c.code(t.getCode())

        c.divider()

    def getSessionArgs(self):
        '''
        get template args from session
        :return:
        '''

        pass

    def generate(self):
        setSessionState(PageType, GenerateCode)

    def goHome(self):
        setSessionState(PageType, ShowHomePage)
