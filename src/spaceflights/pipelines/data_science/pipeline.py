"""
!!! note "Automatic Doc creation"
    In this example one still has to create the `Inputs` and `Outputs` tables by hand, 
    which is pretty tedius. So to investigate if this can be a more automated process similar 
    to standard docstrings.
"""
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import evaluate_model, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    """ ## Overview
    
    The `data_science` pipeline uses the `model_input_table` and splits the 
    dataset into a train and test set and then uses `LinearRegression` to build a model
    to predict flight prices. It then evaluates the model and prints the result to the log.
    It creates 2 instances of the pipelines with independent parameters, `active_modelling_pipeline`
    and `candidate_modelling_pipeline`.

    ## Inputs:

    | Name                | Type               | Description                             |
    | ------------------- | ------------------ | --------------------------------------- |
    | `model_input_table` | `pandas.DataFrame` | Tidied up and combined list of all </br>shuttles with companies and reviews |
 


    **Outputs:**

    | Name                                   | Type                 | Description                             |
    | -------------------------------------- | -------------------- | --------------------------------------- |
    | `active_modelling_pipeline.regressor`    | `pickle.PickleDataSet` |  Active model in production             |
    | `candidate_modelling_pipeline.regressor` | `pickle.PickleDataSet` |  Candidate model in development         |
    """

    pipeline_instance = pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )
    ds_pipeline_1 = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="active_modelling_pipeline",
    )
    ds_pipeline_2 = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="candidate_modelling_pipeline",
    )
    return pipeline(
        pipe=ds_pipeline_1 + ds_pipeline_2,
        inputs="model_input_table",
        namespace="data_science",
    )
