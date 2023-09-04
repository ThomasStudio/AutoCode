from page_base import BasePage

from util_template import *
from util_web import *


class Generate(BasePage):
    def __init__(self):
        super().__init__()
        self.source = None
        self.c1 = None
        self.c0 = None
        self.template = None

    def initData(self):
        self.source = currentSourceFile()
        self.template = currentTemplate()

    def initUi(self):
        st.title(self.source)

        self.c0, self.c1 = st.columns([6, 4])

        with st.sidebar:
            st.button('template', on_click=toShowTemplate)

        self.showSource()
        self.showPreview()

    def showSource(self):
        c1 = self.c1

        c1.write(f'### {ss("Source").orange()}')
        c1.code(currentSource())

    def showPreview(self):
        t = currentTemplate()

        for tl in t.templates:
            self.showTemplate(tl)

    # @st.cache_data
    def showTemplate(self, t: CodeTemplate):
        c0 = self.c0
        c0.title(ss('Template').orange())

        c0.write(f'### {ss("args").orange()}')
        if len(t.args.keys()) > 0:
            cols = c0.columns(2)
            for n, k in enumerate(t.args.keys()):
                t.args[k] = cols[n % 2].text_input(ss(k).green().bold(), "" if t.args[k] is None else t.args[k])

        c0.write(f'### {ss("path").orange()}')
        c0.code(t.getPathPreview())

        c0.write(f'### {ss("code preview").orange()}')

        c0.code(t.getCodePreview())
