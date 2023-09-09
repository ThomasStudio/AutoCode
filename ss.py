from __future__ import annotations

import os
from functools import wraps


def color(fun):
    @wraps(fun)
    def new_fun(*args):
        funName = fun.__name__
        return ss(f":{funName}[{args[0]}]")

    return new_fun


class ss(str):
    """This is super string class for web"""

    @color
    def red(self):
        pass

    @color
    def blue(self):
        pass

    @color
    def orange(self):
        pass

    @color
    def green(self):
        pass

    @color
    def violet(self):
        pass

    @color
    def gray(self):
        pass

    @color
    def rainbow(self):
        pass

    def toUrl(self, url: str):
        return ss(f"[{self}]({url})")

    def append(self, text: str):
        return ss(f'{self}{text}')

    def prepend(self, text: str):
        return ss(f'{text}{self}')

    def title(self):
        return self.prepend('# ')

    def bold(self):
        return ss(f'**{self}**')

    def toPath(self):
        rs = self
        keys = ['\\', '/']
        for k in keys:
            if os.sep != k:
                rs = rs.replace(k, os.sep)

        return rs


if __name__ == '__main__':
        print(ss('hello222').red().title())
