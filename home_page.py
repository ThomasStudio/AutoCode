from base_page import BasePage
from util_template import *
from util_web import *
import streamlit as st


class HomePage(BasePage):

    def initData(self):
        if hasSessionState(TemplateKey):
            print('initData', getSessionState(TemplateKey))

        pass

    def initUi(self):
        self.features()
        self.reference()

        with st.sidebar:
            st.button('Template', on_click=self.showTemplate)

    def reference(self):
        st.write(
            f"""
            # Reference
            ###### Home page {blank(4)} https://streamlit.io
            ###### Documentation {blank(4)} https://docs.streamlit.io
            ###### Git  {blank(4)} https://github.com/streamlit/streamlit
            ###### extras {blank(4)} https://extras.streamlit.app/
        """
        )

    def features(self):
        st.write('''
        # Features

        ## Generate code by template
        User can select a template and input some parameters, then generate code by the template.
        
        ## Add/Edit/Remove code template
        ''')

    def showTemplate(self):
        setSessionState(PageType, ShowTemplate)
