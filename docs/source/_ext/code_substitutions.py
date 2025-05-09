from docutils import nodes
from docutils.parsers.rst import Directive, roles
from sphinx.highlighting import PygmentsBridge
from pygments.formatters import HtmlFormatter
import sys
import importlib.util
from pathlib import Path

# Load the version once when the extension is loaded
def get_version():
    try:
        # Find the repository root - go up two levels from docs/source
        docs_source_dir = Path(__file__).resolve().parent.parent  # _ext -> source
        repo_root = docs_source_dir.parent.parent  # source -> docs -> root
        version_path = repo_root / 'src' / 'molnetpack' / '_version.py'
        
        print(f"Looking for version file at: {version_path}")
        
        if not version_path.exists():
            # Try alternative path
            repo_root = docs_source_dir.parent  # source -> docs
            version_path = repo_root.parent / 'src' / 'molnetpack' / '_version.py'
            print(f"Alternative path: {version_path}")
        
        if not version_path.exists(): 
            # One more attempt - list directories to help debug
            print(f"Repository root directory contents: {os.listdir(repo_root)}")
            if (repo_root / 'src').exists():
                print(f"src directory contents: {os.listdir(repo_root / 'src')}")
            raise FileNotFoundError(f"Could not find _version.py in expected locations")
        
        # Import just the version file
        spec = importlib.util.spec_from_file_location("_version", version_path)
        version_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(version_module)
        return version_module.__version__
    except Exception as e:
        print(f"Error loading version: {e}")
        return "unknown"

# Store the version for reuse
MOLNETPACK_VERSION = get_version()
print(f"Loaded version in extension: {MOLNETPACK_VERSION}")

# Custom role for version
def version_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Custom role that returns the molnetpack version."""
    node = nodes.Text(MOLNETPACK_VERSION)
    return [node], []

class SubstitutionCodeBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        language = self.arguments[0]
        content = '\n'.join(self.content)
        
        # Replace version with actual version - using our directly loaded version
        content = content.replace('|version|', MOLNETPACK_VERSION)
        
        # Apply syntax highlighting using PygmentsBridge
        env = self.state.document.settings.env
        config = env.config
        highlighter = PygmentsBridge('html', config.pygments_style, config.pygments_dark_style)
        formatter = HtmlFormatter(style=config.pygments_style, 
                                 linenos=False,
                                 cssclass='highlight',
                                 wrapcode=True)
        highlighted = highlighter.highlight_block(content, language, location=None, formatter=formatter)
        
        # Create a raw HTML node with appropriate wrapper classes
        html = f'<div class="highlight-{language} notranslate"><div class="highlight">{highlighted}</div></div>'
        raw_node = nodes.raw('', html, format='html')
        return [raw_node]

def setup(app):
    # Register the directive
    app.add_directive('substcode', SubstitutionCodeBlock)
    
    # Register the role
    roles.register_local_role('molnetversion', version_role)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }