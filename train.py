# this file is for training the final model and saving it. 
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler


# import the data
bike_df = pd.read_csv("seoulbikedata.csv", encoding="unicode_escape")
# preprocessing comes next
# remove the parenthesis in the features
bike_df.columns = bike_df.columns.str.replace(r"\([^)]+\)", "", regex=True)
# convert the column names to lower case and replace spaces with _
bike_df.columns = bike_df.columns.str.lower().str.rstrip(" ").str.replace(" ", "_")
# convert date to datetime object
bike_df.date = pd.to_datetime(bike_df.date)
# convert all the string values to lower case and replace space
strings = list(bike_df.dtypes[bike_df.dtypes == "object"].index)
for col in strings:
    bike_df[col] = bike_df[col].str.lower().str.replace(" ", "_")
# extract year, month, weekday and dayofyear from date column
bike_df['year'] = bike_df.date.dt.year
bike_df['month'] = bike_df.date.dt.month
bike_df['day'] = bike_df.date.dt.day
bike_df['weekday'] = bike_df.date.dt.weekday
bike_df['daysofyear'] = bike_df.date.dt.dayofyear
# map the weekdays to actual strings
weekdays_dict = {
    0: "monday", 
    1: "tuesday", 
    2: "wednesday", 
    3: "thursday",
    4: "friday", 
    5: "saturday",
    6: "sunday"
}
bike_df.weekday = bike_df.weekday.map(weekdays_dict)
# remove the date column
bike_df.drop("date", axis=1, inplace=True)
# Note: there are no nulls or duplicate rows, so we proceed with modeling

# modeling the full dataset. check notebook.ipynb for how the best model
# was chosen. 
y_full = bike_df.rented_bike_count.values 
X_full = bike_df.drop("rented_bike_count", axis=1)
# one hot encode and scale the full data
dicts_full_train = X_full.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_full = dv.fit_transform(dicts_full_train)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_full)
X_standardise = pd.DataFrame(X_scaled,columns=dv.get_feature_names_out())
# preparing the xgboost regressor
features = dv.get_feature_names_out()
dtrain = xgb.DMatrix(X_standardise, label=y_full, feature_names=features)
# the number of boosting rounds or trees was based on hyperparameter tuning
# see notebook.ipynb
params = {'max_depth': 7,
 'min_child_weight': 6,
 'eta': 0.05,
 'subsample': 0.7,
 'colsample_bytree': 0.7,
 'objective': 'reg:squarederror'}
model = xgb.train(params, dtrain, num_boost_round=537)

# save the model
import pickle
with open('model.bin', 'wb') as f_out:
   pickle.dump((dv, scaler, model), f_out)
f_out.close()

