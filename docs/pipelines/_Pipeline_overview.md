## Description

The `data_processing` pipeline takes in the raw input data `Shuttles`, `Companies` and `Reviews`. `Shuttles` and `Companies` require some pre-processing (converting strings to float/boolean values)
before the 3 input tables are merged into a single `model_input_table` to be used in model creation.

The `data_science` pipeline consumes the `model_input_table` and generates models from it. There are 2 variants, one is the `active_modelling_pipeline` and the other is a `candidate_modelling_pipeline` demonstrating the use of modular pipelines and how to use the same code with different sets of parameters.


!!! note "Automatic Doc creation"
    This is a standalone KedroViz React component in a static website.
    It can be embedded in the document as seen here or accessed as a [separate page.](/kedro_viz/index.html){:target="\blank"}


## KedroViz Pipeline Viewer [>>](/kedro_viz/index.html){:target="\blank"}

<script defer="defer" src="/kedro_viz/static/js/main.de525c6c.js">
</script><link href="/kedro_viz/static/css/main.957ee550.css" rel="stylesheet">
<div id="kedroviz"></div>
