import mkdocs_gen_files
import os

with mkdocs_gen_files.open("pipelines.md", "w") as f:
    print("Hello, world! again", file=f)


print(os.getcwd())