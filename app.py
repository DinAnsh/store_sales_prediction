# doing necessary imports
import numpy as np
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import pickle   
import log
import Encoding
import store_predictions

# initialising the flask app with the name 'app'
app = Flask(__name__)

# load the model for prediction
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    log.put_log(2, "Open Home page")
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        log.put_log(2, "Predict func called")
        user_values = list(request.form.values())
        log.put_log(2, "Got values from user")
        features = Encoding.get_features(user_values)
        log.put_log(2, "Values encoded")
        try:
            final_features = [np.array(features)]
            prediction = model.predict(final_features)
        except:
            log.put_log(3, " There is some error!!")
            return f"There is an ERROR - {features}"
        log.put_log(2, "Values predicted")

        output = round(prediction[0], 4)
        store_predictions.write_in_file(user_values, output)

        log.put_log(2, f"Got output {output}")
        return render_template('index.html', prediction_text='Item Outlet Sales Should be $ {}'.format(output**4))

    except Exception as e:
        log.put_log(3, " There is some error!!")
        return f"There is an ERROR in prediction - {e} !!"

    finally:
        log.put_log(2, "Prediction Successfull!")


if __name__ == "__main__":
    app.run(debug=True)
