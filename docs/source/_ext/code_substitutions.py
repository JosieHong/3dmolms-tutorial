from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.highlighting import highlight_block

class SubstitutionCodeBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        language = self.arguments[0]
        content = '\n'.join(self.content)
        
        # Get config values for substitution
        env = self.state.document.settings.env
        config = env.config
        
        # Replace version with actual version
        content = content.replace('|version|', config.version)
        
        # Apply syntax highlighting
        highlighted = highlight_block(content, language, True)
        
        # Create a raw HTML node
        raw_node = nodes.raw('', highlighted, format='html')
        return [raw_node]

def setup(app):
    app.add_directive('substcode', SubstitutionCodeBlock)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }