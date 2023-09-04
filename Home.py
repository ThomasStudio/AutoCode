import init

from page_home import HomePage
from util_template import *
from util_web import *
import page_template as tp
from page_generate import Generate

if __name__ == '__main__':
    if hasSessionState(PageType):
        if getSessionState(PageType) == ShowTemplate:
            tp.Template()
        elif getSessionState(PageType) == GenerateCode:
            Generate()
        elif getSessionState(PageType) == ShowHomePage:
            HomePage()
    else:
        HomePage()
