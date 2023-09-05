import init

from page_home import HomePage
from util_template import *
from util_web import *
import page_template as tp

if __name__ == '__main__':
    initPage()

    if hasSessionState(PageType):
        if getSessionState(PageType) == ShowTemplate:
            tp.Template()
        elif getSessionState(PageType) == ShowHomePage:
            HomePage()
    else:
        HomePage()
