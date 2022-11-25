# Getting set up

!!! note
    You only need to do this if you want to play with documentation system, update or change the content and preview locally.

This project can be found at `https://github.com/picklejuicedev/kedro_docs_prototype.git`

Either `clone` or download it to a local folder.

If you want to play with the documentation locally, install the following packages:

```
- `mkdocs`             # core document library
- `mkdocstrings`       # used to extract `docstrings` from code
- `mkdocstring-python` # python extension for `docstrings`
- `mkdocs-gen-files`   # helper to create markdown files programatically
- `mkdocs-material`    # very nice material theme
- `mkdocs-include-markdown-plugin` # plugin to insert .md or other files into markdown files
```

Like this:
```
pip install mkdocs mkdocstrings mkdocstring-python mkdocs-gen-files mkdocs-material mkdocs-include-markdown-plugin
```

## Kedro requirements

You don't need to run the kedro project to be able to generate the documentation.
But if you want to run kedro then you also need to do the usual `pip install -m src/requirements.txt`.
