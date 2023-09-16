from page_base import BasePage
from util_template import *
from util_web import *
import streamlit as st


class HomePage(BasePage):

    def initData(self):
        pass

    def initUi(self):
        self.showTitle()

        self.features()
        self.reference()

        with st.sidebar:
            st.button('Template', on_click=toShowTemplate)

    def reference(self):
        st.write(
            f"""
            # Reference
            ###### Home page {blank(4)} https://streamlit.io
            ###### Documentation {blank(4)} https://docs.streamlit.io
            ###### Git  {blank(4)} https://github.com/streamlit/streamlit
            ###### extras {blank(4)} https://extras.streamlit.app/
            ###### emoji {blank(4)} https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
            ###### import emoji: {blank(4)} from rich._emoji_codes import EMOJI
        """
        )

    def features(self):
        st.write('''
        # Features

        ## Generate code by template
        User can select a template and input some parameters, then generate code by the template.
        
        ## Add/Edit/Remove code template
        ''')
