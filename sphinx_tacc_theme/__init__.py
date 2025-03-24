"""
TACC Sphinx Theme - extends sphinx_rtd_theme
"""
import os

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir

def setup(app):
    """Setup connects events to the sitemap builder"""
    app.require_sphinx('4.0')
    app.add_html_theme('sphinx_tacc_theme', os.path.abspath(os.path.dirname(__file__)))

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
