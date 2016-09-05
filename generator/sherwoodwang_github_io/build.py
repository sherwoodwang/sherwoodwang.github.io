import os
import sys
from functools import partial


def scan(base, exclude=None, rpath=None):
    if rpath is not None:
        path = os.path.join(base, rpath)
    else:
        path = base

    for name in os.listdir(path):
        if exclude is not None and exclude(name):
            continue

        rfn = os.path.join(rpath, name) if rpath is not None else name

        if os.path.isdir(os.path.join(path, name)):
            yield from scan(base, exclude, rfn)
        else:
            yield rfn


def process(directory):
    processors = {
        '.sf': processor_sf
    }

    srcdir = os.path.join(directory, 'src')

    index = []

    for rfn in scan(srcdir, lambda name: name.startswith('.')):
        for ext in processors:
            if rfn.endswith(ext):
                with open(os.path.join(srcdir, rfn), 'r') as sfile:
                    dst, gen, title = processors[ext](sfile, rfn)
                    dst = os.path.join('html', dst)
                    index.append((dst, title))
                    yield dst, gen

    from .indexgen import indexgen
    yield 'index.html', indexgen(index)


def generate(dst, gen):
    dir = os.path.dirname(dst)
    if dir:
        os.makedirs(dir, exist_ok=True)

    with open(dst, "w") as dfile:
        for data in gen:
            dfile.write(data)


def build(directory):
    for item in process(directory):
        generate(*item)


def processor_sf(file, fn):
    name, ext = os.path.splitext(fn)

    from .htmlgen import htmlgen
    generator, title = htmlgen(file)

    return name + '.html', generator, title


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) > 1:
        dir = argv[1]
    else:
        dir = '.'

    build(dir)


if __name__ == '__main__':
    main()
