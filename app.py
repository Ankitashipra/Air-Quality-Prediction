from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('random_forest_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Define the features used for prediction
features = ['CO(GT)', 'PT08.S1(CO)', 'C6H6(GT)', 'NOx(GT)', 'T', 'RH']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_html', methods=['POST'])
def predict_html():
    try:
        # Extract data from form
        input_data = [float(request.form[feature]) for feature in features]
        
        # Predict using the model
        prediction = model.predict([input_data])[0]

        # Determine air quality category
        if prediction <= 50:
            category = "Good"
            recommendation = "Enjoy the fresh air!"
        elif prediction <= 100:
            category = "Moderate"
            recommendation = "Air quality is acceptable, but sensitive groups should be cautious."
        elif prediction <= 150:
            category = "Unhealthy for Sensitive Groups"
            recommendation = "People with respiratory issues should limit outdoor activities."
        elif prediction <= 200:
            category = "Unhealthy"
            recommendation = "Everyone may experience health effects. Avoid prolonged outdoor exertion."
        elif prediction <= 300:
            category = "Very Unhealthy"
            recommendation = "Health alert: Everyone may experience serious health effects."
        else:
            category = "Hazardous"
            recommendation = "Emergency conditions. Stay indoors and wear a mask if necessary."

        return render_template('index.html', prediction=round(prediction, 2), category=category, recommendation=recommendation)
    
    except Exception as e:
        return str(e)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check for JSON data
        if not request.is_json:
            return jsonify({"error": "Invalid input. Please send JSON data."}), 415

        data = request.get_json()

        # Validate all features are provided
        missing_features = [f for f in features if f not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Extract input data for prediction
        input_data = [float(data[feature]) for feature in features]

        # Predict using the model
        prediction = model.predict([input_data])[0]

        # Determine air quality category
        if prediction <= 50:
            category = "Good"
            recommendation = "Enjoy the fresh air!"
        elif prediction <= 100:
            category = "Moderate"
            recommendation = "Air quality is acceptable, but sensitive groups should be cautious."
        elif prediction <= 150:
            category = "Unhealthy for Sensitive Groups"
            recommendation = "People with respiratory issues should limit outdoor activities."
        elif prediction <= 200:
            category = "Unhealthy"
            recommendation = "Everyone may experience health effects. Avoid prolonged outdoor exertion."
        elif prediction <= 300:
            category = "Very Unhealthy"
            recommendation = "Health alert: Everyone may experience serious health effects."
        else:
            category = "Hazardous"
            recommendation = "Emergency conditions. Stay indoors and wear a mask if necessary."

        # Return detailed response
        return jsonify({
            "AQI_Prediction": round(prediction, 2),
            "Category": category,
            "Recommendation": recommendation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
