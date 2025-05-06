# Configuration file for the Sphinx documentation builder.
import sys
import os
from pathlib import Path
from unittest.mock import MagicMock

# ===== STEP 1: Mock ALL dependencies FIRST =====
class BetterMock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return BetterMock()

# Create the torch module FIRST, before any imports happen
sys.modules['torch'] = BetterMock()
sys.modules['torch.utils'] = BetterMock()
sys.modules['torch.utils.data'] = BetterMock()
sys.modules['torch.utils.data.DataLoader'] = BetterMock()

# Mock other external dependencies
MOCK_MODULES = [
    'numpy', 'pandas', 'yaml', 'requests', 'pickle',
    'pathlib', 'zipfile',
    'pyteomics', 'pyteomics.mgf',
    'rdkit', 'rdkit.Chem', 'rdkit.Chem.Descriptors', 'rdkit.Chem.Draw', 'rdkit.Chem.AllChem', 'rdkit.RDLogger',
    'PIL', 'PIL.Image', 'PIL.ImageFilter',
    'matplotlib', 'matplotlib.pyplot', 'matplotlib.offsetbox',
]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = BetterMock()

# ===== STEP 2: Set up sys.path AFTER mocking =====
sys.path.insert(0, str(Path('..', '..', 'src').resolve()))

# ===== STEP 3: Create stubs for internal modules =====
# These are needed because your code uses relative imports
sys.modules['molnetpack.model'] = type('model', (), {
    'MolNet_MS': type('MolNet_MS', (), {}),
    'MolNet_Oth': type('MolNet_Oth', (), {}),
    'Encoder': type('Encoder', (), {})
})

sys.modules['molnetpack.dataset'] = type('dataset', (), {
    'Mol_Dataset': type('Mol_Dataset', (), {})
})

sys.modules['molnetpack.data_utils'] = type('data_utils', (), {
    'csv2pkl_wfilter': lambda *args: None,
    'nce2ce': lambda *args: None,
    'precursor_calculator': lambda *args: None,
    'filter_spec': lambda *args: None,
    'mgf2pkl': lambda *args: None,
    'ms_vec2dict': lambda *args: None
})

sys.modules['molnetpack.utils'] = type('utils', (), {
    'pred_step': lambda *args: None,
    'eval_step_oth': lambda *args: None,
    'pred_feat': lambda *args: None
})

# ===== STEP 4: NOW try to import molnetpack =====
try:
    import molnetpack
    print("Successfully imported molnetpack")
    print(f"Found MolNet class: {'MolNet' in dir(molnetpack)}")
    print(f"Found plot_msms function: {'plot_msms' in dir(molnetpack)}")
except ImportError as e:
    print(f"Failed to import molnetpack: {e}")
    print(f"Current sys.path: {sys.path}")
    # Additional debugging
    print(f"'torch' in sys.modules: {'torch' in sys.modules}")

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

# # For autodoc to work with modules that are not installed, we need to mock them before import molnetpack.
# autodoc_mock_imports = [
#     # External packages
#     'requests',
#     'numpy',
#     'pandas',
#     'yaml',
#     'pickle',
#     'pathlib',
#     'pyteomics',
#     'zipfile',
#     'torch',
#     'rdkit',
#     'PIL',
#     'matplotlib',
# ]
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path('..', 'src').resolve()))

# try:
#     import molnetpack
#     print("Successfully imported molnetpack")
#     # Optionally print some debug info
#     print(f"Found MolNet class: {'MolNet' in dir(molnetpack)}")
# except ImportError as e:
#     print(f"Failed to import molnetpack: {e}")
#     # The autodoc_mock_imports should handle this case

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