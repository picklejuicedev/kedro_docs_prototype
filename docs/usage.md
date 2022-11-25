# Usage

!!! note
    Normally you wold discuss how to use the project here, i.e. the spaceflights code and/or model.
    However it is much more interesting to highlight how to use the documentation system.

## Run a local server

Assuming you have installed all [prerequisites](prerequisites.md), you can now run a local test server:
```
mkdocs serve
```

It will collect the documentation and serve them up to a local host:
```
(docs-prototype-py3.10) PS C:\code\kedro\docs_prototype\spaceflights> mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.95 seconds
INFO     -  [16:15:17] Watching paths for changes: 'docs', 'mkdocs.yml', 'README.md'
INFO     -  [16:15:17] Serving on http://127.0.0.1:8000/
```

Open a browser and point to `http://127.0.0.1:8000/` and you should see the documentation website.

This page will auto-reload on any changes, so try modifying any of the .md files in the `/docs` folder and on save it will be reflected on the site. This is a fast and easy workflow to get all manual docs written and check the automatically generated ones look correct.

## Deploy docs manually

Once happy with the documentation you can build the site manually using:

```
mkdocs build
```

It will create a static site in the subfolder `/site`. Use your ftp client or other tool to upload to your hosting platform.

## Deploy automatically using github workflows

For this project a `github workflow` has been added (see `/.github/workflows/ci.yml`).
It will automatically build the documentation and deploy to the `gh-pages` branch so will be visible at `<username>.github.io/<repository>`.

## Changing the theme

`mkdocs` comes with the excellent `readthedocs` theme and this is running here by default. You can switch to the `material` theme by changing the `theme` entry in `mkdocs.yml` to `material`:

```

...

theme: material

...

```


## More help

Have a look at the excellent [mkdocs website](https://www.mkdocs.org/) for more help.
Hopefully this shold get you started.

