# BMI Calculator Web Application

A web-based Body Mass Index (BMI) calculator built with Flask, HTML, and CSS. Users can input their height and weight to calculate their BMI and see which category they fall into.

## Features

- 🎯 Calculate BMI based on height (cm) and weight (kg)
- 🎨 Beautiful, responsive UI with gradient design
- 📊 Color-coded BMI categories (Underweight, Normal, Overweight, Obese)
- ✅ Input validation and error handling
- 📱 Mobile-friendly responsive design

## BMI Categories

- **Underweight**: BMI < 18.5 (Blue)
- **Normal**: BMI 18.5 - 24.9 (Green)
- **Overweight**: BMI 25 - 29.9 (Orange)
- **Obese**: BMI ≥ 30 (Red)

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3
- **Server**: Flask development server (can be hosted on Linux)

## Project Structure

```
reyona/
│
├── app.py                 # Flask backend with BMI calculation logic
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   └── style.css         # CSS styling
├── .venv/                # Python virtual environment
└── README.md             # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.x installed
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd reyona
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install flask
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Hosting on Linux

To host this application on a Linux machine:

1. **Install Python and pip** (if not already installed)
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Clone and setup the project**
   ```bash
   git clone <your-repository-url>
   cd reyona
   python3 -m venv .venv
   source .venv/bin/activate
   pip install flask
   ```

3. **Run the Flask application**
   ```bash
   python3 app.py
   ```

4. **Access from network**
   The application runs on `0.0.0.0:5000`, making it accessible from other devices on your network using your machine's IP address.

## Usage

1. Enter your height in centimeters (e.g., 170)
2. Enter your weight in kilograms (e.g., 70)
3. Click the "Calculate BMI" button
4. View your BMI value and category with color indication

## BMI Formula

```
BMI = weight (kg) / (height (m))²
```

## Screenshots

The application features:
- Modern gradient background (purple to violet)
- Clean white card design
- Color-coded results based on BMI category
- Responsive layout for all screen sizes

## Future Enhancements

- Add BMI history tracking
- Include metric/imperial unit conversion
- Add charts for BMI trends over time
- Implement user authentication
- Add health recommendations based on BMI

## Author

Created as part of a web development project.

## License

This project is open source and available for educational purposes.
