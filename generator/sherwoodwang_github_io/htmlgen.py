from simple_format import scan, HTMLRenderer


def find_title(data):
    for element in data:
        if element[0] == 'title':
            return element[2]
        else:
            title = find_title(element[-1])

            if title is not None:
                return title


def htmlgen(file):
    data = scan(file.read().splitlines())
    renderer = HTMLRenderer()

    title = ''.join(renderer(find_title(data)))

    def generator():
        yield '<html>\n'
        yield '\t<head>\n'
        yield '\t<title></title>\n'
        yield '\t</head>\n'
        yield '\t<body>\n'
        yield from renderer(data)
        yield '\n'
        yield '\t</body>\n'
        yield '</html>\n'

    return generator(), title
