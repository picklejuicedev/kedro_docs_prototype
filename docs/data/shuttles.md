# pandas.DataFrame: shuttles 
## Info 

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77096 entries, 0 to 77095
Data columns (total 13 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   id                       77096 non-null  int64  
 1   shuttle_location         77096 non-null  object 
 2   shuttle_type             77096 non-null  object 
 3   engine_type              77096 non-null  object 
 4   engine_vendor            77096 non-null  object 
 5   engines                  77057 non-null  float64
 6   passenger_capacity       77096 non-null  int64  
 7   cancellation_policy      77096 non-null  object 
 8   crew                     76947 non-null  float64
 9   d_check_complete         77096 non-null  object 
 10  moon_clearance_complete  77096 non-null  object 
 11  price                    77096 non-null  object 
 12  company_id               77096 non-null  int64  
dtypes: float64(2), int64(3), object(8)
memory usage: 7.6+ MB

```
## Table Head 

``` 
      id       shuttle_location shuttle_type engine_type       engine_vendor  engines  passenger_capacity cancellation_policy  crew d_check_complete moon_clearance_complete     price  company_id
0  63561                   Niue      Type V5     Quantum  ThetaBase Services     1.00                   2              strict  1.00                f                       f  $1,325.0       35029
1  36260               Anguilla      Type V5     Quantum  ThetaBase Services     1.00                   2              strict  1.00                t                       f  $1,780.0       30292
2  57015     Russian Federation      Type V5     Quantum  ThetaBase Services     1.00                   2            moderate  0.00                f                       f  $1,715.0       19032
3  14035               Barbados      Type V5      Plasma  ThetaBase Services     3.00                   6              strict  3.00                f                       f  $4,770.0        8238
4  10036  Sao Tome and Principe      Type V2      Plasma  ThetaBase Services     2.00                   4              strict  2.00                f                       f  $2,820.0       30342
```

## Table Tail 

``` 
          id           shuttle_location shuttle_type engine_type       engine_vendor  engines  passenger_capacity cancellation_policy  crew d_check_complete moon_clearance_complete     price  company_id
77091   4368                   Barbados      Type V5     Quantum  ThetaBase Services     2.00                   4            flexible  2.00                t                       f  $4,107.0        6654
77092   2983  Bouvet Island (Bouvetoya)      Type F5     Quantum  ThetaBase Services     1.00                   1            flexible  1.00                t                       f  $1,169.0        8000
77093  69684                 Micronesia      Type V5      Plasma  ThetaBase Services     0.00                   2            flexible  1.00                t                       f  $1,910.0       14296
77094  21738                 Uzbekistan      Type V5      Plasma  ThetaBase Services     1.00                   2            flexible  1.00                t                       f  $2,170.0       27363
77095  72645                      Malta      Type F5     Quantum  ThetaBase Services     0.00                   2            moderate  2.00                t                       f  $1,455.0       12542
```

## Describe 

```
             id   engines  passenger_capacity      crew  company_id
count 77,096.00 77,057.00           77,096.00 76,947.00   77,096.00
mean  38,548.50      1.40                3.16      1.74   25,155.39
std   22,255.84      0.91                1.97      1.24   14,300.99
min        1.00      0.00                1.00      0.00        1.00
25%   19,274.75      1.00                2.00      1.00   12,935.75
50%   38,548.50      1.00                2.00      1.00   25,253.50
75%   57,822.25      2.00                4.00      2.00   37,410.25
max   77,096.00     44.00               20.00     23.00   50,098.00
```

## NaN counts 
```
id                           0
shuttle_location             0
shuttle_type                 0
engine_type                  0
engine_vendor                0
engines                     39
passenger_capacity           0
cancellation_policy          0
crew                       149
d_check_complete             0
moon_clearance_complete      0
price                        0
company_id                   0
```


## Unique Values 
```
id                         77096
shuttle_location              30
shuttle_type                  42
engine_type                    3
engine_vendor                  5
engines                       15
passenger_capacity            17
cancellation_policy            3
crew                          20
d_check_complete               2
moon_clearance_complete        1
price                        848
company_id                 50098
```



