from code_template import *

args = dict(
    output=''
)

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
    args=args,
    files=[f1],
)
