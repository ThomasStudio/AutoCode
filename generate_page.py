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
        self.showBackButtion()
        st.title(self.template)

    def showBackButtion(self):
        st.button('go back', on_click=self.toShowTemplate, type='primary')

    def toShowTemplate(self):
        setSessionState(PageType, ShowTemplate)
