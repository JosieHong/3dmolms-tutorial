# Configuration file for the Sphinx documentation builder.

# -- Project information
project = '3DMolMS'
copyright = '2023, Yuhui Hong'
author = 'Yuhui Hong'

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

# For autodoc to work with modules that are not installed, we need to mock them before import molnetpack.
autodoc_mock_imports = [
    # External packages
    'requests',
    'numpy',
    'pandas',
    'yaml',
    'pyteomics',
    'zipfile',
    'rdkit',
    'PIL',
    'matplotlib',

    'torch',
    'torch.nn',
    'torch.optim',
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

# -- Autodoc configuration
import sys
from pathlib import Path
sys.path.insert(0, str(Path('..', 'src').resolve()))

try:
    import molnetpack
    print("Successfully imported molnetpack")
    # Optionally print some debug info
    print(f"Found MolNet class: {'MolNet' in dir(molnetpack)}")

except ImportError as e:
    print(f"Failed to import molnetpack: {e}")
    # The autodoc_mock_imports should handle this case
