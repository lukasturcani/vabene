extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'numpydoc',
]
autodoc_default_options = {
    'inherited-members': True,
    'show-inheritance': True,
}
add_module_names = False
templates_path = [
    '_templates',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'vabene'
copyright = '2020, Lukas Turcani'
author = 'Lukas Turcani'
version = ''
release = ''
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
}
html_static_path = [
    '_static',
]
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ],
}
htmlhelp_basename = 'vabenedoc'
latex_elements = {}
latex_documents = [
    [
        master_doc,
        'vabene.tex',
        'vabene Documentation',
        'Lukas Turcani',
        'manual',
    ],
]
man_pages = [
    [
        master_doc,
        'vabene',
        'vabene Documentation',
        [author, ],
        1,
    ],
]
texinfo_documents = [
    [
        master_doc,
        'vabene',
        'vabene Documentation',
        author,
        'vabene',
        (
            'A Python library for making molecular graphs with valid '
            'valence.'
        ),
        'Miscellaneous',
    ],
]
