"""
!!! note "Automatic Doc creation"
    In this example one still has to create the `Inputs` and `Outputs` tables by hand, 
    which is pretty tedius. So we should investigate if this can be a more automated process similar 
    to standard docstrings.
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    """ ## Overview
    
    The `data_processing` pipeline takes in the raw input data and carries 
    out preprocessing to clean up the data nd merge the 3 input tables to a 
    single `model_input_table` to be used in model creation.

    ## Inputs:

    | Name      | Type             | Description          |
    | --------- | ---------------- | -------------------- |
    | shuttles  | pandas.DataFrame | List of all shuttles |
    | companies | pandas.DataFrame | List of companies    |
    | reviews   | pandas.DataFrame | List of reviews      |



    **Outputs:**

    | Name              | Type             | Description                             |
    | ----------------- | ---------------- | --------------------------------------- |
    | model_input_table | pandas.DataFrame | Tidied up and combined list of all </br>shuttles with companies and reviews |
    """


    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ],
        namespace="data_processing",
        inputs=["companies", "shuttles", "reviews"],
        outputs="model_input_table",
    )
