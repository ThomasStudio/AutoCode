import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
pages = os.path.join(current, 'pages')
template = os.path.join(current, 'template')

for p in [current, parent, pages, template]:
    if p not in sys.path:
        sys.path.append(p)
