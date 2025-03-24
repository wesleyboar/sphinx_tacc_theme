# TACC Sphinx Theme

A [TACC](https://www.tacc.utexas.edu/)-styled [Sphinx](https://www.sphinx-doc.org/) theme based on **ReadTheDocs**'s own [Sphinx theme](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/README.rst).

## How to Install

1. Install the theme e.g.

   > [!CAUTION]
   > **Not published yet.**
   >
   > ```bash
   > pip install sphinx-tacc-theme
   > ```

   > [!NOTE]
   > **Development method.**
   >
   > ```bash
   > pip install -e "sphinx-tacc-theme @git+https://github.com/TACC/sphinx-tacc-theme.git#work-in-progress"
   > ```

2. In your `conf.py`:

    - Add theme `sphinx_tacc_theme`:

      ```python
      import sphinx_tacc_theme

      html_theme = "sphinx_tacc_theme"
      ```
    - <del>Set [typical extensions for this theme](./docs/extensions.md#typical).</del>
      <ins>Not yet certain to be documented.</ins>

> [!NOTE]
> We <del>also</del> <ins>do not yet</ins> offer <!--[-->detailed instructions<!--](https://tacc.github.io/mkdocs-tacc/)--> instead.

## Known Clients

| Status | Repository |
| - | - |
| Active | |
| Upcoming | [TACC/life_sciences_ml_at_tacc](https://github.com/TACC/life_sciences_ml_at_tacc) |
| Potential | [TACC/containers_at_tacc](https://github.com/TACC/containers_at_tacc) |

## Contributing

<del>We welcome contributions. Read ["How to Contribute"](./CONTRIBUTING.md).</del>

<ins>We do not yet offer guidance on how to contribute</ins>.
