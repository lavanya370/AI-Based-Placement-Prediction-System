from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load("placement_model.pkl")

@app.route('/')
def home():
    return """
    <h1>AI Placement Prediction System</h1>

    <form action='/predict' method='post'>

    CGPA:<br>
    <input type='number' step='0.1' name='cgpa'><br><br>

    Attendance:<br>
    <input type='number' name='attendance'><br><br>

    Aptitude:<br>
    <input type='number' name='aptitude'><br><br>

    Technical:<br>
    <input type='number' name='technical'><br><br>

    Communication:<br>
    <input type='number' name='communication'><br><br>

    <input type='submit' value='Predict'>

    </form>
    """

@app.route('/predict', methods=['POST'])
def predict():

    values = [[
        float(request.form['cgpa']),
        float(request.form['attendance']),
        float(request.form['aptitude']),
        float(request.form['technical']),
        float(request.form['communication'])
    ]]

    result = model.predict(values)[0]

    if result == 1:
        return "<h2>Likely To Be Placed ✅</h2>"
    else:
        return "<h2>Needs Improvement ❌</h2>"

if __name__ == "__main__":
    app.run(debug=True)