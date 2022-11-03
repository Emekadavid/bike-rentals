# this file serves as the web service for deploying the model
# I will be using flask
import pickle
from flask import Flask, request, jsonify
import xgboost as xgb

# import the pickled files
with open('model.bin', 'rb') as f_in:  ## Note that never open a binary file you do not trust!
    dv, scaler, model = pickle.load(f_in)
f_in.close()

def predict_once(mydata, dv, scaler, model):
    data_encoded = dv.transform(mydata)
    data_scaled = scaler.transform(data_encoded)
    features = dv.get_feature_names_out()
    pred_data = xgb.DMatrix(data_scaled, feature_names=features)
    # now make prediction
    prediction = model.predict(pred_data)
    return prediction[0] #could remove this

app = Flask("bike-rentals")

@app.route('/predict', methods=['POST'])
def predict():
    mydata = request.get_json()
    prediction = predict_once(mydata, dv, scaler, model)
    result = {"prediction": float(prediction)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)    

