import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# -- Project information -----------------------------------------------------

project = 'django-keygen'
copyright = '2022, Daniel Perrefort'
author = 'Daniel Perrefort'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_copybutton'
]

source_suffix = '.rst'
master_doc = 'index'
pygments_style = None

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = []
