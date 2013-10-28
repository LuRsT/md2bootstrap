import sys

from markdown import markdown
from bottle import route, run, template


TEMPLATE_CONTENTS = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>md2bootstrap</title>

        <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">

        <!--[if lt IE 9]>
            <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6/html5shiv.min.js"></script>
        <![endif]-->
    </head>

    <body>
        <div class="container">
            <h1>{{filename}}</h1>
            <p class="lead">{{!file_contents}}</p>
        </div>

        <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
        <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
"""


@route('/')
def index():
    if 1 < len(sys.argv) < 3:
        filename = sys.argv[1]
    else:
        raise TypeError('One argument please')

    with open(filename) as file:
        file_contents = file.read()

    markdown_content = markdown(file_contents)

    return template(
        TEMPLATE_CONTENTS,
        filename=filename,
        file_contents=markdown_content,
    )


if __name__=='__main__':
    run(host='localhost', port=5000)
