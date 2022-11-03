# this is the file that contains our data
# you can modify it at your delight
import requests

mydata = {'hour': 23, # number between 0 and 23 
    'temperature': -6.0, # float, the temperature scale 
    'humidity': 25, # int 
    'wind_speed': 2.5, # int
    'visibility': 2000, # int 
    'dew_point_temperature': -10.0, # float 
    'solar_radiation': 0.1, # float 
    'rainfall': 0.0, # float
    'snowfall': 0.0, #float 
    'seasons': "summer", #from winter, summer, autumn and spring 
    'holiday': "no_holiday", # values are 'no_holiday' or 'holiday' 
    'functioning_day': "yes", # values are "yes" or "no" 
    'year': 2018, # years of the calendar. our data was just for 2017 and 2018 
    'month': 6, # values are 1 to 12. numeric values for the calendar months
    'day': 15, # values are 1 to 31. days of the month numerically 
    'weekday': "thursday", # string values. monday to thursday. all lower case 
    'daysofyear': 183 # values are 1 to 365. days of the year.

}

url = 'http://localhost:9696/predict' ## this is the route we made for prediction
response = requests.post(url, json=mydata) ## post the customer information in json format
result = response.json() ## get the server response
print(f'The bike rental demand is {int(round(result["prediction"], 0))}')