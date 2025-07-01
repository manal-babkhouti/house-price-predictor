from flask import Flask, request, render_template_string
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("models/model.pkl")

form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>🏠 House Price Predictor</title>
    <style>
        body {
            background: #f4f7f8;
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
        }
        .container {
            background: #fff;
            padding: 30px 40px;
            max-width: 600px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #34495e;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            margin-top: 25px;
            width: 100%;
            background-color: #2ecc71;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #27ae60;
        }
        .result {
            text-align: center;
            font-size: 26px;
            color: #2980b9;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏡 Predict House Price</h1>
        <form action="/predict" method="post">
            <label>🏷️ Building Class</label>
            <input type="number" name="MSSubClass" required>

            <label>🏘️ Zoning Classification</label>
            <select name="MSZoning">
                <option value="RL">Residential Low Density</option>
                <option value="RM">Residential Medium Density</option>
                <option value="FV">Floating Village Residential</option>
                <option value="RH">Residential High Density</option>
                <option value="C (all)">Commercial</option>
            </select>

            <label>🔧 Overall Quality (1–10)</label>
            <input type="number" name="OverallQual" min="1" max="10" required>

            <label>📐 Living Area (sqft)</label>
            <input type="number" name="GrLivArea" required>

            <label>🚗 Garage Cars</label>
            <input type="number" name="GarageCars" required>

            <label>🔥 Fireplaces</label>
            <input type="number" name="Fireplaces" required>

            <label>🏚️ Basement Area (sqft)</label>
            <input type="number" name="TotalBsmtSF" required>

            <label>📅 Year Built</label>
            <input type="number" name="YearBuilt" required>

            <label>❄️ Central Air</label>
            <select name="CentralAir">
                <option value="Y">Yes</option>
                <option value="N">No</option>
            </select>

            <label>🏡 Exterior Quality</label>
            <select name="ExterQual">
                <option value="TA">Typical/Average</option>
                <option value="Gd">Good</option>
                <option value="Ex">Excellent</option>
                <option value="Fa">Fair</option>
            </select>

            <button type="submit">🔍 Predict Price</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(form_html)

@app.route("/predict", methods=["POST"])
def predict():
    form = request.form

    input_data = {
        'MSSubClass': [float(form["MSSubClass"])],
        'MSZoning': [form["MSZoning"]],
        'OverallQual': [float(form["OverallQual"])],
        'GrLivArea': [float(form["GrLivArea"])],
        'GarageCars': [float(form["GarageCars"])],
        'Fireplaces': [float(form["Fireplaces"])],
        'TotalBsmtSF': [float(form["TotalBsmtSF"])],
        'YearBuilt': [float(form["YearBuilt"])],
        'CentralAir': [form["CentralAir"]],
        'ExterQual': [form["ExterQual"]],
    }

    df_input = pd.DataFrame(input_data)
    prediction = model.predict(df_input)[0]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Prediction Result</title>
        <style>
            body {{
                background-color: #f0f4f8;
                font-family: 'Segoe UI', sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: white;
                padding: 40px 60px;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h2 {{
                color: #2c3e50;
                font-size: 26px;
                margin-bottom: 20px;
            }}
            .price {{
                font-size: 36px;
                font-weight: bold;
                color: #27ae60;
            }}
            a button {{
                margin-top: 30px;
                padding: 12px 24px;
                font-size: 16px;
                background-color: #2980b9;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }}
            a button:hover {{
                background-color: #1f5d88;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>📊 Predicted House Price:</h2>
            <div class="price">${int(prediction):,}</div>
            <a href="/"><button>🔁 Try Another Prediction</button></a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
