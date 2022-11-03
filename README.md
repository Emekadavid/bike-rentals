# Prediction of hourly bike rentals in Seoul, South Korea

Bikes are essential to mobility in big cities. They also serve to reduce the impact of transportation on global warming and climate change. Therefore, it is important to make accessibility to bikes a matter of priority for city councils. 

This project used data collected from Seoul, South Korea, and made accessible in the UCI Machine Learning repository to predict the hourly count of bike rentals among Seoul residents. The result of this project would help city councils to provide bikes for rental purposes that would make the supply stable and convenient for residents. Some of the features of the data includes weather information, date information, and the target feature is the number of bike rentals counted each hour. 

# Exploratory Data Analysis (EDA)

During the EDA, after taking the mutual information scores for categorical features and the correlation coefficient for numeric features, four features looked to have low predictive powers. They were holiday, daysofyear, month and day. But after comparing their RMSE score against the baseline model, I decided to train the dataset with all the complete features. 

