# A new doc system

Creating documentation is not everyones favourite - it takes time away from valuable dev time and is so quickly out of date. Will anybody read it? Or are we just documenting to tick a box? 

## Why documentation is a first class citizen

I find it very helpful for any serious software or data project to adapt a product mindset. You embark on a journey and develop this *thing* that solves a problem. During development assumptions are made, solutions desigend and tested until finally it solves the problem that it was tasked to solve. Unless it was a one-shot project and never to be used again, there will be the need to communicate to others how it works and what it does, what assumptions were made during the design and how it can be used. Without this, the project will slowly wither away and die, especially when the original designers aren't around any more.

So the question is: Where and how do we write stuff down?

## Anatomy of a Kedro project

Let's consider the different parts of a Kero project:

- Pipelines and Nodes - the *meaty* stuff!
- Settings - all those yaml files
- Data - lots of it, in many different forms
- Setup, Installation, Deployment - How to install or deploy it
- Testing - how to ensure it works correctly
- Usage - how should one use it, and what for

The great news is that for many of those sections Kedro has an answer for how it should be done, committed to code and stored in a repository. So if you are a developer and understand the framework you can look up most things and make sense of the code together maybe with a high level Readme.md in the root of the repository. This may be ok for small projects but for anything more significant we need some kind of docs framework. Also what to do when some of your *customers* aren't developers that are familiar with repositories? How can you include them into the fold?

## Write as little as possible

So it is paramount that a documentation system can extract all the inherent information in a Kedro project and publish this automatically in such a way that it is readable by newcomers to the project and external stakeholders.

So for example, the `catalog` defines all DataSet resources - they can easily be referenced and auto-generate documentation that then can be annotated with context. `nodes` and `pipelines` have docstrings and those can be used to explain how the parts of the processing work. `KedroViz` has a wealth of information that is best explored interactively.

## Make it easy to write the rest

Many things just need to be written, but there is nothing more daunting than a clean white page. If we have a well documented template (or multiple templates for different types of projects) then architectural decisions have a home, assumptions can be written up quickly. Just as with pushing a developer towards using standard building blocks when creating data processing pipelines (nodes, pipelines, DataSets, etc) they should also be encourage to adopt a certain documentation structure. Consistency will then make both the writing easier and quicker, but also the reader will know where to find the information they seek as it is in the same place.

## And design better products

Have you ever tried to document a half-cooked idea? Doesn't work! So documentation (just like testing) is a great tool to review your own work and test it for public consumption. It is one thing to make something work, quite another to build and explain it in such a way that *others* can use it easily and without errors. The job is only complete when you are not needed any more and the project can life on its own.

## Building blocks

- mkdocs documentation system based on .md documents in /docs folder
- write anything and it will compile into a nice looking webpage
- publish to github pages easily
- be able to include root/Readme.md as index (if possible)
- use mkdocsstrings to parse code and add to documentation
- parse settings (conf)  and annotate with comments
- parse catalog and provide framework for describing datasets
- provide boilerplate documentation for building, deploying and installing 
- provide notebook index with comments
- use autogeneration to create base documentation but be able to manually annotate
- 