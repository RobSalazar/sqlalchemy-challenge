# SQLAlchemy Homework - Surfs Up!

![surfs-up.png](images/surfs-up.png)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Step 1 - Climate [Analysis](https://github.com/RobSalazar/sqlalchemy-challenge/blob/main/climate_starter.ipynb) and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


### Precipitation Analysis

* Retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.

 ![precipitation](images/precipitation_line_chart.PNG)

### Station Analysis

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (i.e. which stations have the most rows?).


 ![station-histogram](images/station_temp.PNG)

- - -

## Step 2 - [Climate App](https://github.com/RobSalazar/sqlalchemy-challenge/blob/main/app.py)



### Routes

![routes.png](images/routes.PNG)

* Please replace the "yyyy-mm-dd" with dates youd like to query.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? [Why?](https://github.com/RobSalazar/sqlalchemy-challenge/blob/main/temp_analysis_bonus_1_starter.ipynb)
