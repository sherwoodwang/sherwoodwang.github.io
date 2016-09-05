from chameleon import PageTemplate
from pkg_resources import resource_string
import os


def indexgen(index):
    template = PageTemplate(resource_string('sherwoodwang_github_io', os.path.join('templates', 'index.pt')))
    yield template(index=index)
