# pandas.DataFrame: model_input_table 
## Info 

```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 759609 entries, 0 to 1864889
Data columns (total 28 columns):
 #   Column                   Non-Null Count   Dtype  
---  ------                   --------------   -----  
 0   id_x                     759609 non-null  int64  
 1   shuttle_location         759609 non-null  object 
 2   shuttle_type             759609 non-null  object 
 3   engine_type              759609 non-null  object 
 4   engine_vendor            759609 non-null  object 
 5   engines                  759609 non-null  float64
 6   passenger_capacity       759609 non-null  int64  
 7   cancellation_policy      759609 non-null  object 
 8   crew                     759609 non-null  float64
 9   d_check_complete         759609 non-null  bool   
 10  moon_clearance_complete  759609 non-null  bool   
 11  price                    759609 non-null  float64
 12  company_id               759609 non-null  int64  
 13  shuttle_id               759609 non-null  int64  
 14  review_scores_rating     759609 non-null  float64
 15  review_scores_comfort    759609 non-null  float64
 16  review_scores_amenities  759609 non-null  float64
 17  review_scores_trip       759609 non-null  float64
 18  review_scores_crew       759609 non-null  float64
 19  review_scores_location   759609 non-null  float64
 20  review_scores_price      759609 non-null  float64
 21  number_of_reviews        759609 non-null  int64  
 22  reviews_per_month        759609 non-null  float64
 23  id_y                     759609 non-null  int64  
 24  company_rating           759609 non-null  float64
 25  company_location         759609 non-null  object 
 26  total_fleet_count        759609 non-null  float64
 27  iata_approved            759609 non-null  bool   
dtypes: bool(3), float64(13), int64(6), object(6)
memory usage: 152.9+ MB

```
## Table Head 

``` 
    id_x shuttle_location shuttle_type engine_type             engine_vendor  engines  passenger_capacity cancellation_policy  crew  d_check_complete  moon_clearance_complete    price  company_id  shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month   id_y  company_rating company_location  total_fleet_count  iata_approved
0  63561             Niue      Type V5     Quantum        ThetaBase Services     1.00                   2              strict  1.00             False                    False 1,325.00       35029       63561                 97.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                133               1.65  35029            1.00             Niue               4.00          False
1  63561             Niue      Type V5     Quantum        ThetaBase Services     1.00                   2              strict  1.00             False                    False 1,325.00       35029       63561                 97.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                133               1.65  35029            1.00             Niue               4.00          False
2  63561             Niue      Type V5     Quantum        ThetaBase Services     1.00                   2              strict  1.00             False                    False 1,325.00       35029       63561                 97.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                133               1.65  35029            1.00             Niue               4.00          False
3  63561             Niue      Type V5     Quantum        ThetaBase Services     1.00                   2              strict  1.00             False                    False 1,325.00       35029       63561                 97.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                133               1.65  35029            1.00             Niue               4.00          False
4  53260             Niue      Type V5     Quantum  Banks, Wood and Phillips     1.00                   2              strict  1.00             False                    False 1,325.00       35029       53260                 98.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                 37               0.48  35029            1.00             Niue               4.00          False
```

## Table Tail 

``` 
          id_x           shuttle_location shuttle_type engine_type       engine_vendor  engines  passenger_capacity cancellation_policy  crew  d_check_complete  moon_clearance_complete    price  company_id  shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month   id_y  company_rating    company_location  total_fleet_count  iata_approved
1864307  39094         Russian Federation      Type F5     Quantum  ThetaBase Services     1.00                   2              strict  1.00             False                    False 1,455.00       42904       39094                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00                  1               1.00  42904            0.70  Russian Federation               2.00           True
1864357  20330                 Uzbekistan      Type V5     Quantum  ThetaBase Services     1.00                   2            flexible  1.00             False                    False 1,585.00        5701       20330                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00                  1               1.00   5701            1.00          Costa Rica               1.00           True
1864386  16445                  Nicaragua      Type V5      Plasma  ThetaBase Services     1.00                   1            flexible  3.00             False                    False 1,715.00       13728       16445                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00                  3               3.00  13728            1.00            Pakistan               1.00          False
1864448  76469  Bouvet Island (Bouvetoya)      Type V5     Quantum  ThetaBase Services     1.00                   2            moderate  1.00             False                    False 1,520.00       41714       76469                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00                  1               1.00  41714            1.00             Lebanon               1.00          False
1864889  75780         Russian Federation      Type V5      Plasma  ThetaBase Services     1.00                   2              strict  1.00              True                    False 2,820.00       47766       75780                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00                  1               1.00  47766            1.00          Uzbekistan               1.00           True
```

## Describe 

```
            id_x    engines  passenger_capacity       crew      price  company_id  shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month       id_y  company_rating  total_fleet_count
count 759,609.00 759,609.00          759,609.00 759,609.00 759,609.00  759,609.00  759,609.00            759,609.00             759,609.00               759,609.00          759,609.00          759,609.00              759,609.00           759,609.00         759,609.00         759,609.00 759,609.00      759,609.00         759,609.00
mean   38,504.63       2.07                4.72       2.62   3,503.88   26,968.06   38,504.63                 88.14                   9.05                     9.04                9.05                9.13                    9.36                 8.70              10.30               0.83  26,968.06            0.98             716.92
std    22,169.91       1.28                2.36       1.61   1,866.61    9,058.39   22,169.91                 13.42                   1.41                     1.38                1.52                1.45                    1.12                 1.42              23.05               1.11   9,058.39            0.07             616.04
min         4.00       0.00                1.00       0.00     870.00        4.00        4.00                 20.00                   2.00                     2.00                2.00                2.00                    2.00                 2.00               1.00               0.01       4.00            0.00               1.00
25%    19,107.00       1.00                3.00       1.00   2,417.00   22,721.00   19,107.00                 80.00                   9.00                     9.00                9.00                9.00                    9.00                 8.00               1.00               0.16  22,721.00            1.00              60.00
50%    39,049.00       2.00                4.00       2.00   3,145.00   29,647.00   39,049.00                 90.00                  10.00                    10.00               10.00               10.00                   10.00                 9.00               3.00               0.40  29,647.00            1.00           1,305.00
75%    58,363.00       3.00                6.00       4.00   4,146.00   29,647.00   58,363.00                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00               9.00               1.00  29,647.00            1.00           1,305.00
max    77,095.00      12.00               20.00      20.00  86,150.00   50,094.00   77,095.00                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00             578.00              16.56  50,094.00            1.00           1,484.00
```

## NaN counts 
```
id_x                       0
shuttle_location           0
shuttle_type               0
engine_type                0
engine_vendor              0
engines                    0
passenger_capacity         0
cancellation_policy        0
crew                       0
d_check_complete           0
moon_clearance_complete    0
price                      0
company_id                 0
shuttle_id                 0
review_scores_rating       0
review_scores_comfort      0
review_scores_amenities    0
review_scores_trip         0
review_scores_crew         0
review_scores_location     0
review_scores_price        0
number_of_reviews          0
reviews_per_month          0
id_y                       0
company_rating             0
company_location           0
total_fleet_count          0
iata_approved              0
```


## Unique Values 
```
id_x                       29768
shuttle_location              30
shuttle_type                  32
engine_type                    3
engine_vendor                  5
engines                       13
passenger_capacity            17
cancellation_policy            3
crew                          18
d_check_complete               2
moon_clearance_complete        1
price                        527
company_id                 15354
shuttle_id                 29768
review_scores_rating          54
review_scores_comfort          9
review_scores_amenities        9
review_scores_trip             9
review_scores_crew             9
review_scores_location         8
review_scores_price            9
number_of_reviews            358
reviews_per_month            899
id_y                       15354
company_rating                64
company_location             159
total_fleet_count             81
iata_approved                  2
```



