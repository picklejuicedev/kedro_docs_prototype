
The `data_processing` pipeline takes in the raw input data `Shuttles`, `Companies` and `Reviews`. `Shuttles` and `Companies` require some pre-processing (converting strings to float/boolean values)
before the 3 input tables are merged into a single `model_input_table` to be used in model creation.


!!! note "Automatic Doc creation"
    It would be nice to have a Kedro interactive Viz here.
    I tried the [Kedro-static-viz plugin](https://github.com/WaylonWalker/kedro-static-viz) which would be perfect, but seem out of date, so doesn't run.
    So here a static image instead.

## The complete pipeline

![overview](img\overview.svg) 



## Data Processing Detail

![data_science](img\data_science.svg)
