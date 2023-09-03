from util_template import *
from Cheetah.Template import Template

templates = [
    getCreateTemplate(
        path='',
        args=dict(
            title='hello world'
        ),
        content='''
print('$title')
'''
    ),

    getTemplate(
        path='',
        args=dict(
            title='this is a example'
        ),
        content='''
The title is $title
'''
    )
]
