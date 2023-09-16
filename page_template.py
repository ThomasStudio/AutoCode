from code_template import CodeTemplate
from page_base import BasePage
from util_template import *
from util_web import *
from ss import ss


class Template(BasePage):
    CurrentTemplate: CodeTemplate = None

    def __init__(self):
        super().__init__()

        self.templates = []
        self.cmds = []
        self.source = None
        self.c1 = None
        self.c0 = None

    def initData(self):
        self.templates = [x for x in os.listdir(TemplateFolder) if x.endswith('.py')]
        self.source = currentSourceFile()

        self.cmds = [
            ['edit', editCurrentTemplate],
            ['add', self.add],
            ['clone', self.clone],
            ['remove', self.remove],
        ]

    def initUi(self):
        with st.sidebar:
            st.button('Home', on_click=toHomePage)

            st.title(colorText('orange', 'Template list'))

            selected = st.radio(
                "template list",
                self.templates,
                label_visibility='collapsed',
                format_func=lambda x: ss(x).green()
            )

            if len(selected) > 0:
                setSessionState(TemplateKey, selected)
                self.showTemplateFile()

            if st.button(f'make {currentSourceFile()}', type='primary', use_container_width=True):
                t = Template.CurrentTemplate
                if t is None:
                    st.warning('No template selected')
                else:
                    if t.checkArgs():
                        cs = st.columns(2)

                        cs[0].button('OK', type='primary', on_click=self.generate)

                        cs[1].button('Cancel', type='primary')

            cs = st.columns(2)
            for n, (name, f) in enumerate(self.cmds):
                if cs[n % 2].button(name):
                    f()

        self.c0, self.c1 = st.columns([6, 4])
        self.showSource()

        t = Template.CurrentTemplate = currentTemplate()

        if t is not None:
            t.showTemplate(self.c0)

    def showTemplateFile(self):
        c = self.container

        c.subheader(f'{ss("Template").orange()}  {blank(1)}{ss(currentSourceFile()).green()}')

    @log
    def clone(self):
        pass

    @log
    def remove(self):
        pass

    def showSource(self):
        c1 = self.c1

        c1.write(f'### {ss("Source").orange()}')
        c1.code(currentSource())

    def add(self):
        pass

    def generate(self):
        print('generate generate generate')
        t = Template.CurrentTemplate
        t.generateCode()
