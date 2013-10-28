from sys import argv
from markdown import markdown
from bottle import route, run, template


TEMPLATE_CONTENTS = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{{filename}}</title>
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            {{!file_contents}}
        </div>
  </body>
</html>
"""


@route('/')
def index():
    if len(argv) < 2:
        raise TypeError('Needs at least one argument.')

    file_contents = ''
    for filename in argv[1:]:
        with open(filename) as file:
            file_contents += markdown(file.read())

    return template(
        TEMPLATE_CONTENTS,
        filename=filename,
        file_contents=file_contents,
    )


if __name__=='__main__':
    run(host='localhost', port=5000)
