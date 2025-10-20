from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height_cm, weight_kg):
    """
    Calculate BMI and return the value and category
    BMI = weight (kg) / (height (m))^2
    """
    # Convert height from cm to meters
    height_m = height_cm / 100
    
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:  # BMI >= 30
        category = "Obese"
    
    return round(bmi, 2), category

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    error = None
    
    if request.method == 'POST':
        try:
            height = float(request.form.get('height'))
            weight = float(request.form.get('weight'))
            
            if height <= 0 or weight <= 0:
                error = "Please enter positive values for height and weight."
            else:
                bmi, category = calculate_bmi(height, weight)
        except (ValueError, TypeError):
            error = "Please enter valid numeric values."
    
    return render_template('index.html', bmi=bmi, category=category, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
