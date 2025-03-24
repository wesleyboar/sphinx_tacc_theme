# TACC Sphinx Theme

A Sphinx theme for TACC documentation that extends the ReadTheDocs theme (`sphinx_rtd_theme`).

## Installation

Install the theme using pip:

```bash
pip install sphinx_tacc_theme
```

## Usage

To use the theme in your Sphinx documentation:

1. Add `sphinx_tacc_theme` to your project's dependencies
2. In your `conf.py`, set:

```python
import sphinx_tacc_theme

html_theme = "sphinx_tacc_theme"
```

## Development

To work on this theme:

1. Clone the repository
2. Install in editable mode:
   ```bash
   pip install -e .
   ```
3. Make your changes
4. Test with a Sphinx project by setting the theme in its `conf.py`

## License

MIT License 