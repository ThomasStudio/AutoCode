from page_base import BasePage
from util_template import *
from util_web import *


class Template(BasePage):

    def __init__(self):
        super().__init__()

        self.templates = []
        self.cmds = []
        self.source = None
        self.c1 = None
        self.c0 = None
        self.template = None

    def initData(self):
        self.templates = [x for x in os.listdir(TemplateFolder) if x.endswith('.py')]
        self.source = currentSourceFile()
        self.template = currentTemplate()

        self.cmds = [
            ['edit', editCurrentTemplate],
            ['add', self.add()],
            ['reload', self.reload],
            ['clone', self.clone],
            ['remove', self.remove],
        ]

    def initUi(self):
        c = self.container
        c.write('')

        with st.sidebar:
            st.button('Home', on_click=toHomePage)

            st.title(colorText('orange', 'Template list'))

            c0, c1 = st.columns([2, 1])

            selected = c0.radio(
                "",
                self.templates,
                label_visibility='collapsed'
            )

            if len(selected) > 0:
                setSessionState(TemplateKey, selected)
                self.showTemplateFile()

            for n, (name, f) in enumerate(self.cmds):
                if c1.button(name, type='primary'):
                    f()

        self.c0, self.c1 = st.columns([6, 4])
        self.showSource()
        self.showTemplate()

    def showTemplateFile(self):
        c = self.container

        c.title(currentSourceFile())

    @log
    def clone(self):
        pass

    @log
    def remove(self):
        pass

    @log
    def reload(self):
        pass

    def showSource(self):
        c1 = self.c1

        c1.write(f'### {ss("Source").orange()}')
        c1.code(currentSource())

    # @st.cache_data
    def showTemplate(self):
        t = currentTemplate()
        print('ttt', t)
        print('t.args', t.args)
        print('t.files', t.files)
        c0 = self.c0
        c0.write('### ' + ss('args').orange())

        if len(t.args.keys()) > 0:
            cols = c0.columns(2)
            for n, k in enumerate(t.args.keys()):
                t.args[k] = cols[n % 2].text_input(ss(k).green().bold(), "" if t.args[k] is None else t.args[k])

        for f in t.files:
            t.showFile(f, c0)

    def add(self):
        pass
