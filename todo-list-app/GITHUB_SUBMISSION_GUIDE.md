# GitHub Submission Guide - To-Do List App

## Steps to Upload Your To-Do List App to GitHub

### 1. Initialize Git Repository

```bash
cd "c:\Users\lenovo\OneDrive\Desktop\todo-list-app"
git init
```

### 2. Add All Files to Git

```bash
git add .
```

### 3. Create Initial Commit

```bash
git commit -m "Initial commit: To-Do List web application with earthy aesthetic"
```

### 4. Create a New Repository on GitHub

1. Go to https://github.com
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., "todo-list-app")
5. Choose "Public" or "Private"
6. DO NOT initialize with README (we already have one)
7. Click "Create repository"

### 5. Link Your Local Repository to GitHub

Replace `<your-username>` with your actual GitHub username:

```bash
git remote add origin https://github.com/<your-username>/todo-list-app.git
git branch -M main
git push -u origin main
```

### 6. Verify Upload

Visit your GitHub repository URL to confirm all files are uploaded:
- app.py
- index.html (in templates folder)
- style.css (in static folder)
- README.md
- requirements.txt
- .gitignore

## Alternative: Using GitHub Desktop

1. Download and install GitHub Desktop
2. Click "Add" → "Add Existing Repository"
3. Choose the folder: `c:\Users\lenovo\OneDrive\Desktop\todo-list-app`
4. Click "Publish repository" button
5. Choose repository name and visibility
6. Click "Publish repository"

## Project Structure (For Reference)

```
todo-list-app/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   └── style.css         # CSS styling
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

## Important Notes

- The `.venv` folder is excluded via `.gitignore` (good practice)
- The `tasks.json` file (task storage) is optional to include
- Make sure to include all three main files: app.py, index.html, and style.css
- The README.md contains complete documentation for your project
- requirements.txt allows others to easily install dependencies

## Testing Your Submission

After uploading to GitHub, clone it to a different location to test:

```bash
git clone https://github.com/<your-username>/todo-list-app.git
cd todo-list-app
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5001 to test!

Your To-Do List App is ready for submission! 🎉
