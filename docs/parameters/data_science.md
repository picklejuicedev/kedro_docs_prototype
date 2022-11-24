# data_science

##  active_modelling_pipeline:

Parameters for the currently active model used in production.

### model_options:

| Param        | Value                     | Description                          |
| ------------ | ------------------------- | ------------------------------------ |
| test_size    | 0.2                       | Percentage of data used for testing. |
| random_state | 3                         | Split Random parameter.              |
| features     |                           | Columns included in model creation.  |
|              | - engines                 |                                      |
|              | - passenger_capacity      |                                      |
|              | - crew                    |                                      |
|              | - check_complete          |                                      |
|              | - moon_clearance_complete |                                      |
|              | - ta_approved             |                                      |
|              | - company_rating          |                                      |
|              | - review_scores_rating    |                                      |

## candidate_modelling_pipeline:

Parameters used in testing to compare against production model.

### model_options:

| Param        | Value                  | Description                          |
| ------------ | ---------------------- | ------------------------------------ |
| test_size    | 0.2                    | Percentage of data used for testing. |
| random_state | 3                      | Split Random parameter.              |
| features     |                        | Columns included in model creation.  |
|              | - engines              |                                      |
|              | - passenger_capacity   |                                      |
|              | - crew                 |                                      |
|              | - check_complete       |                                      |
|              | - review_scores_rating |                                      |


