from base_page import BasePage
import streamlit as st

import streamlit as st
import urllib.parse

from util_template import *
from util_web import *


class Generate(BasePage):
    def initData(self):
        self.template = currentTemplate()

    def initUi(self):
        with st.sidebar:
            st.button('template', on_click=self.toShowTemplate)

        st.title(self.template)

    def toShowTemplate(self):
        setSessionState(PageType, ShowTemplate)
