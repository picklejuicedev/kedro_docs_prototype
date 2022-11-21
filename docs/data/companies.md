## dataframe head

|      | id    | company_rating | company_location      | total_fleet_count | iata_approved |
| ---- | ----- | -------------- | --------------------- | ----------------- | ------------- |
| 0    | 35029 | 100%           | Niue                  | 4.0               | f             |
| 1    | 30292 | 67%            | Anguilla              | 6.0               | f             |
| 2    | 19032 | 67%            | Russian Federation    | 4.0               | f             |
| 3    | 8238  | 91%            | Barbados              | 15.0              | t             |
| 4    | 30342 | NaN            | Sao Tome and Principe | 2.0               | t             |

## info

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77096 entries, 0 to 77095
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 77096 non-null  int64  
 1   company_rating     47187 non-null  object 
 2   company_location   57966 non-null  object 
 3   total_fleet_count  77089 non-null  float64
 4   iata_approved      77089 non-null  object 
dtypes: float64(1), int64(1), object(3)
memory usage: 2.9+ MB
```

## continuous values

|       | id           | total_fleet_count |
| ----- | ------------ | ----------------- |
| count | 77096.000000 | 77089.000000      |
| mean  | 25155.386272 | 30.473699         |
| std   | 14300.990642 | 165.548267        |
| min   | 1.000000     | 1.000000          |
| 25%   | 12935.750000 | 1.000000          |
| 50%   | 25253.500000 | 1.000000          |
| 75%   | 37410.250000 | 4.000000          |
| max   | 50098.000000 | 1484.000000       |

## Nan

```
id                       0
company_rating       29909
company_location     19130
total_fleet_count        7
iata_approved            7

```

## Unique

```
id                   50098
company_rating          70
company_location       181
total_fleet_count       90
iata_approved            2
```