# Prediction of hourly bike rentals in Seoul, South Korea

Bikes are essential to mobility in big cities. They also serve to reduce the impact of transportation on global warming and climate change. Therefore, it is important to make accessibility to bikes a matter of priority for city councils. 

This project used data collected from Seoul, South Korea, and made accessible in the UCI Machine Learning repository to predict the hourly count of bike rentals among Seoul residents. The result of this project would help cities like Seoul to provide bikes for rental purposes that would make the supply stable and convenient for residents. Some of the features of the data includes weather information, date information, and the target feature is the number of bike rentals counted each hour. 

Many cities that have high bike usage and want to reduce the impact of transportation on climate change and global warming are looking for ways to encourage their citizens to switch to using bikes and other sustainable transportation methods. Bike rentals like taxis would then have to be provisioned. To be efficient in provisioning this, local authorities need an efficient way to predict the demand for bikes within their jurisdiction. 

This solution uses the popular XGBoost Model to predict hourly bike rental demand based on data from Seoul city between the years 2017 and 2018. We hope the model in this project would be used in the future to solve this problem. 

# Exploratory Data Analysis (EDA)

During the EDA, after taking the mutual information scores for categorical features and the correlation coefficient for numeric features, four features looked to have low predictive powers. They were holiday, daysofyear, month and day. But after comparing their RMSE score against the baseline model, I decided to train the dataset with all the complete features. 

A full outline of what was done for the EDA can be seen by looking through the `notebook.ipynb` file. 

# Model Training

I trained the cleaned and processed data on several models including linear regression, support vector regressor, k nearest neighbor, decision tree regressor, ridge regression, lasso regression, adaboost regressor, random forest regressor, and the XGBoost regressor. 

The XGBoost model turned out to have the best performance among all the regressors and models. So the final model was created based on the XGBoost model. The final model and the training process can be found in the `train.py` file. The model and supporting artefacts were then saved in a pickle file, `model.bin`. 

# Dataset used

The data for the project was taken from UCI Machine Learning Repository. It is included with this project as `seoulbikedata.csv`. You can [download it from the UCI site](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand).

# Deploying the app on flask

The first deployment was locally in a flask web app with the gunicorn framework as the production backend. Gunicorn only works with Linux systems. If you are on a Windows machine, then use waitress as the production backend for the web app on flask. 

Here's how to do it. 

1. Fork this repo so you can own it.

2. On your local machine clone your forked repo.

3. Install pipenv in your machine to create the local environment 

    ```pip install pipenv```

4. Navigate to the directory where you cloned this repo

5. Create a virtual environment using pipenv in that directory. These are the steps to do it. The app was created with python 3.8 and your python might be different. So just go to the pipfile in the directory, open it and change the python requirement to the python version you have on your system. That do, carry out this command:

    ```pipenv shell```

    This will create a virtual environment on your system.

6. Install all the dependencies for the project

    ```pipenv install -r requirements.txt```

    The above command updates the pipfile.lock file and installs all the required dependencies for the project in the virtual environment. 

7. Now run the flask app. First, you need to run the web server. Use this command:
    If on Linux, use: 
    
    ``` gunicorn --bind 0.0.0.0:9696 predict:app```
    
    The server would be bound to port 9696. 
    
    If on Windows, use this command:

    ```waitress-serve --listen=0.0.0.0:9696 predict:app``` 

    The server would also be bound to port 9696 on your Windows machine. 

    Then open another terminal and run the following command for the client to send data to the server and receive a response:

    ``` python client.py```

    Make sure you run the above command in the virtual environment in the new terminal. 

    When the server sends the prediction, you will instantly see the response in the client terminal. 

    That's all for deploying on flask with gunicorn or waitress backend. 

    You can see the data that was sent to the server when you open the client.py file in an editor. 

    I hope to deploy the app on streamlit soon. Just stay tuned. 

# Creating a Docker image

The app can be deployed to the cloud using a Docker image. But I will show you how to deploy the app locally with a Docker image. 

I assume you are using a Linux machine or Windows Subsystem for Linux if on a Windows machine. Also, that you have Docker Desktop installed on your machine. 

1. First, get a base python image file that will be used to power the Docker image file. Just search on Google for "docker python image" and pick one that conforms to the python version installed on your machine. 

2. Build the python image file on your machine. 
    
    ```docker run -it --rm python:<name of python image file>```

    Since I am using python 3.8 on my machine, this is the command I used:

    ```docker run -it --rm python:3.8.10-slim```

3. Build the docker image for the app. The build will be using the Dockerfile that is in the present directory. Just open the file and change the first line to reflect the python image file you run in step 2. Make sure you are in the direcotry of the Dockerfile before building. The code for building the docker image is:

    ``` docker build -t bike-rentals . ```

    bike-rentals is the tag name given to the Docker image and . signifies the Dockerfile is in the present directory. 

    It takes some time to do the complete building process. Be patient. 

4. Now you can run the docker image as our prediction app. The code for doing this is:

    ``` docker run -it -p 9696:9696 bike-rentals:latest ```

5. Open another terminal and run the   ` client.py ` file. 

Voila! You have run the app and received the prediction. 