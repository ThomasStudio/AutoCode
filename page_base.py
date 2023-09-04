from abc import ABC, abstractmethod
from util_web import *


class BasePage(ABC):
    def __init__(self) -> None:
        initPage()
        self.showTitle()

        self.container = st.container()

        self.initData()
        self.initUi()
        self.afterInitUi()

    @abstractmethod
    def initData(self):
        pass

    @abstractmethod
    def initUi(self):
        pass

    def afterInitUi(self):
        pass

    def showTitle(self):
        st.title(f'{appIcon()} {appTitle()}')
