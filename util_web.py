from functools import wraps

import streamlit as st
from typing import *
import urllib.parse
import tornado
from tornado import httputil
from util_decorator import *

AppTitle = 'AtoCode'
AppIcon = '🚀'
AppAbout = '# This is AutoCode by Thomas!'


def appTitle():
    return AppTitle


def appIcon():
    return AppIcon


def appAbout():
    return AppAbout


def getSessionState(k: str) -> Any:
    if k not in st.session_state:
        None
    else:
        return st.session_state[k]


@log
def setSessionState(k: str, v: Any):
    st.session_state[k] = v


def hasSessionState(k: str) -> bool:
    return k in st.session_state


def initPage():
    st.set_page_config(
        page_title=appTitle(),
        page_icon=appIcon(),
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={'About': appAbout()}
    )


def colorText(color: str, txt: str) -> str:
    return f":{color}[{txt}]"


def urlText(txt: str, url: str) -> str:
    return f"[{txt}]({url})"


def blank(n):
    return '&nbsp;' * n


def getUrl():
    session = st.runtime.get_instance()._session_mgr.list_active_sessions()[0]
    st_base_url = urllib.parse.urlunparse(
        [session.client.request.protocol, session.client.request.host, "", "", "", ""])

    print(session.client.request.protocol)
    print(session.client.request.host)
    print(session.client.request)
    return st_base_url


if __name__ == '__main__':
    pass

    print(orangeText('hello'))
