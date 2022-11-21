!!! note
	Describing the data is tricky as there are so many different data types. I think what would work is to have a genric front page simply listing the catalog and data types, but then have a separate page for more details. We can autogenerate some from the data itself i.e. using `pandas-profiling` or `AutoViz` or some simple `pandas` commands. This should be easily extendable for other DataSets to enable automatic generation.




## raw

| Name          | Type                | Path                      | Details                                                      |
| ------------- | ------------------- | ------------------------- | ------------------------------------------------------------ |
| **companies** | pandas.CSVDataSet   | data/01_raw/companies.csv | [basic info](../companies), [pandas profiling](companies/companies.html) |
| **reviews**   | pandas.CSVDataSet   | data/01_raw/reviews.csv   |                                                              |
| **shuttles**  | pandas.ExcelDataSet | data/01_raw/shuttles.xlsx | [autoViz](../shuttles)                                       |



## intermediate

| Name                       | Type                  | Path                                           | Details |
| -------------------------- | --------------------- | ---------------------------------------------- | ------- |
| **preprocessed_companies** | pandas.ParquetDataSe  | data/02_intermediate/preprocessed_companies.pq |         |
| **preprocessed_shuttles**  | pandas.ParquetDataSet | data/02_intermediate/preprocessed_shuttles.pq  |         |
| **model_input_table**      | pandas.ParquetDataSet | data/03_primary/model_input_table.pq           |         |

## primary

| Name                  | Type                  | Path                                 | Details |
| --------------------- | --------------------- | ------------------------------------ | ------- |
| **model_input_table** | pandas.ParquetDataSet | data/03_primary/model_input_table.pq |         |

## models

| Name                                    | Type                 | Path                                      | Details |
| --------------------------------------- | -------------------- | ----------------------------------------- | ------- |
| **active_modelling_pipeline.regressor** | pickle.PickleDataSet | data/06_models/regressor_active.pickle    |         |
| **regressor_candidate.regressor**       | pickle.PickleDataSet | data/06_models/regressor_candidate.pickle |         |