from code_template import *

f1 = CodeFile(
    language='kotlin',
    content='''
import java.util.Scanner

fun main(args: Array<String>) {

    println("You entered: $output")

}
''',
)

template = CodeTemplate(
    args=dict(output='hello world'),
    files=[f1],
)
