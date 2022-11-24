!!! note
	Not sure how to handle all the different types of `datasets`. What may work is to have a generic front page like this one simply listing the `catalog` and data types, but then have a separate page for more details. We can autogenerate some from the data itself i.e. using `pandas-profiling` or some simple `pandas` commands. This should be easily extendable for other `datasets` to enable automatic generation. 




## raw

| Name          | Type                | Path                      | Details                                                      |
| ------------- | ------------------- | ------------------------- | ------------------------------------------------------------ |
| **companies** | pandas.CSVDataSet   | data/01_raw/companies.csv | [basic info](../companies), [pandas profiling](companies/companies.html) |
| **reviews**   | pandas.CSVDataSet   | data/01_raw/reviews.csv   | [basic info](../reviews), [pandas profiling](reviews/reviews.html) |
| **shuttles**  | pandas.ExcelDataSet | data/01_raw/shuttles.xlsx | [basic info](../shuttles), [pandas profiling](shuttles/shuttles.html) |



## intermediate

| Name                       | Type                  | Path                                           | Details |
| -------------------------- | --------------------- | ---------------------------------------------- | ------- |
| **preprocessed_companies** | pandas.ParquetDataSe  | data/02_intermediate/preprocessed_companies.pq |         |
| **preprocessed_shuttles**  | pandas.ParquetDataSet | data/02_intermediate/preprocessed_shuttles.pq  |         |


## primary

| Name                  | Type                  | Path                                 | Details                                                      |
| --------------------- | --------------------- | ------------------------------------ | ------------------------------------------------------------ |
| **model_input_table** | pandas.ParquetDataSet | data/03_primary/model_input_table.pq | [basic info](../model_input_table), [pandas profiling](model_input_table/model_input_table.html) |

## models

| Name                                    | Type                 | Path                                      | Details |
| --------------------------------------- | -------------------- | ----------------------------------------- | ------- |
| **active_modelling_pipeline.regressor** | pickle.PickleDataSet | data/06_models/regressor_active.pickle    |         |
| **regressor_candidate.regressor**       | pickle.PickleDataSet | data/06_models/regressor_candidate.pickle |         |