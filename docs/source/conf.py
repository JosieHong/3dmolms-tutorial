# Configuration file for the Sphinx documentation builder.
import sys
from pathlib import Path
sys.path.insert(0, str(Path('..', 'src').resolve()))

# -- Project information

project = '3DMolMS'
copyright = '2025, Yuhui Hong'
author = 'Yuhui Hong'

release = '0.1.11'
version = '0.1.11'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]
autodoc_mock_imports = [
    # External packages
    'requests',
    'numpy',
    'pandas',
    'yaml',
    'pickle',
    'pathlib',
    'pyteomics',
    'zipfile',
    'torch',
    'rdkit',
    'PIL',
    'matplotlib',
    
    # Local modules
    'model',  # for .model
    'dataset',  # for .dataset
    'data_utils',  # for .data_utils
    'utils'  # for .utils
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
