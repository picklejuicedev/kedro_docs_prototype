# pandas.DataFrame: reviews 
## Info 

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77096 entries, 0 to 77095
Data columns (total 10 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   shuttle_id               77096 non-null  int64  
 1   review_scores_rating     55956 non-null  float64
 2   review_scores_comfort    55896 non-null  float64
 3   review_scores_amenities  55909 non-null  float64
 4   review_scores_trip       55833 non-null  float64
 5   review_scores_crew       55902 non-null  float64
 6   review_scores_location   55831 non-null  float64
 7   review_scores_price      55828 non-null  float64
 8   number_of_reviews        77096 non-null  int64  
 9   reviews_per_month        57553 non-null  float64
dtypes: float64(8), int64(2)
memory usage: 5.9 MB

```
## Table Head 

``` 
   shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month
0       63561                 97.00                  10.00                     9.00               10.00               10.00                    9.00                10.00                133               1.65
1       36260                 90.00                   8.00                     9.00               10.00                9.00                    9.00                 9.00                  3               0.09
2       57015                 95.00                   9.00                    10.00                9.00               10.00                    9.00                 9.00                 14               0.14
3       14035                 93.00                  10.00                     9.00                9.00                9.00                   10.00                 9.00                 39               0.42
4       10036                 98.00                  10.00                    10.00               10.00               10.00                    9.00                 9.00                 92               0.94
```

## Table Tail 

``` 
       shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month
77091        4368                   NaN                    NaN                      NaN                 NaN                 NaN                     NaN                  NaN                  0                NaN
77092        2983                   NaN                    NaN                      NaN                 NaN                 NaN                     NaN                  NaN                  0                NaN
77093       69684                   NaN                    NaN                      NaN                 NaN                 NaN                     NaN                  NaN                  0                NaN
77094       21738                   NaN                    NaN                      NaN                 NaN                 NaN                     NaN                  NaN                  0                NaN
77095       72645                   NaN                    NaN                      NaN                 NaN                 NaN                     NaN                  NaN                  0                NaN
```

## Describe 

```
       shuttle_id  review_scores_rating  review_scores_comfort  review_scores_amenities  review_scores_trip  review_scores_crew  review_scores_location  review_scores_price  number_of_reviews  reviews_per_month
count   77,096.00             55,956.00              55,896.00                55,909.00           55,833.00           55,902.00               55,831.00            55,828.00          77,096.00          57,553.00
mean    38,548.50                 92.76                   9.52                     9.28                9.64                9.67                    9.47                 9.28              15.26               1.26
std     22,255.84                  9.76                   0.96                     1.12                0.87                0.85                    0.84                 1.00              32.20               1.46
min          1.00                 20.00                   2.00                     2.00                2.00                2.00                    2.00                 2.00               0.00               0.01
25%     19,274.75                 90.00                   9.00                     9.00               10.00               10.00                    9.00                 9.00               0.00               0.27
50%     38,548.50                 96.00                  10.00                    10.00               10.00               10.00                   10.00                10.00               4.00               0.77
75%     57,822.25                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00              15.00               1.71
max     77,096.00                100.00                  10.00                    10.00               10.00               10.00                   10.00                10.00             578.00              16.56
```

## NaN counts 
```
shuttle_id                     0
review_scores_rating       21140
review_scores_comfort      21200
review_scores_amenities    21187
review_scores_trip         21263
review_scores_crew         21194
review_scores_location     21265
review_scores_price        21268
number_of_reviews              0
reviews_per_month          19543
```


## Unique Values 
```
shuttle_id                 77096
review_scores_rating          55
review_scores_comfort          9
review_scores_amenities        9
review_scores_trip             9
review_scores_crew             9
review_scores_location         8
review_scores_price            9
number_of_reviews            369
reviews_per_month            949
```



