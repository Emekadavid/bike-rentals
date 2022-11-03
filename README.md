# Prediction of hourly bike rentals in Seoul, South Korea

Bikes are essential to mobility in big cities. They also serve to reduce the impact of transportation on global warming and climate change. Therefore, it is important to make accessibility to bikes a matter of priority for city councils. 

This project used data collected from Seoul, South Korea, and made accessible in the UCI Machine Learning repository to predict the hourly count of bike rentals among Seoul residents. The result of this project would help city councils to provide bikes for rental purposes that would make the supply stable and convenient for residents. Some of the features of the data includes weather information, date information, and the target feature is the number of bike rentals counted each hour. 

# Exploratory Data Analysis (EDA)

During the EDA, after taking the mutual information scores for categorical features and the correlation coefficient for numeric features, four features looked to have low predictive powers. They were holiday, daysofyear, month and day. But after comparing their RMSE score against the baseline model, I decided to train the dataset with all the complete features. 

# Deploying the app

The first deployment was locally in a flask web app with the gunicorn framework as the production backend. Gunicorn only works with Linux systems. If you are on a Windows machine, then use waitress as the production backend for the web app on flask. 

Here's how to do it. 

1. Fork this repo so you can own it.
2. On your local machine clone your forked repo.
3. Install pipenv in your machine to create the local environment 

```pip install pipenv```

4. Navigate to the directory where you cloned this repo
5. Create a virtual environment using pipenv in that directory.

```pipenv shell```

6. 