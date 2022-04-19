project = 'Flask-IPFilter'
copyright = '2019-2022, Douglas Anger'
author = 'Douglas Anger'
version = '0.0'
release = '0.0.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'pallets_sphinx_themes'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None

html_theme = 'flask'
html_static_path = ['_static']

todo_include_todos = True
