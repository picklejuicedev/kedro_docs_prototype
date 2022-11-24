# pandas.DataFrame: companies 
## Info 

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
## Table Head 

``` 
      id company_rating       company_location  total_fleet_count iata_approved
0  35029           100%                   Niue               4.00             f
1  30292            67%               Anguilla               6.00             f
2  19032            67%     Russian Federation               4.00             f
3   8238            91%               Barbados              15.00             t
4  30342            NaN  Sao Tome and Principe               2.00             t
```

## Table Tail 

``` 
          id company_rating company_location  total_fleet_count iata_approved
77091   6654           100%            Tonga               3.00             f
77092   8000            NaN            Chile               2.00             t
77093  14296            NaN      Netherlands               4.00             f
77094  27363            80%              NaN               3.00             t
77095  12542            98%       Mauritania              19.00             t
```

## Describe 

```
             id  total_fleet_count
count 77,096.00          77,089.00
mean  25,155.39              30.47
std   14,300.99             165.55
min        1.00               1.00
25%   12,935.75               1.00
50%   25,253.50               1.00
75%   37,410.25               4.00
max   50,098.00           1,484.00
```

## NaN counts 
```
id                       0
company_rating       29909
company_location     19130
total_fleet_count        7
iata_approved            7
```


## Unique Values 
```
id                   50098
company_rating          70
company_location       181
total_fleet_count       90
iata_approved            2
```



