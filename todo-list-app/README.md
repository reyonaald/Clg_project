# To-Do List Web Application

A beautiful, web-based To-Do List application built with Flask, HTML, and CSS. Users can add, view, complete, and delete tasks with a serene earthy aesthetic design.

## Features

- ✅ Add new tasks with priority levels (Low, Medium, High)
- � Set optional due dates for tasks
- �👁️ View all tasks with creation timestamps
- ✓ Mark tasks as complete/incomplete with celebration effect
- 🗑️ Delete individual tasks
- 🧹 Clear all completed tasks at once
- 🔍 Filter tasks by status (All, Active, Completed) and priority
- 📊 View task statistics (Total, Pending, Done)
- 💾 Persistent storage (tasks saved to JSON file)
- � Fun confetti animation when completing tasks
- ⚠️ Visual alerts for overdue tasks
- �🎨 Beautiful earthy aesthetic with nature-inspired design
- 📱 Fully responsive mobile-friendly interface
- 🎭 Priority badges with fun animations (🔥 High, ⭐ Medium, 🌱 Low)

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3
- **Storage**: JSON file (persistent storage)
- **Server**: Flask development server (can be hosted on Linux)

## Project Structure

```
todo-list-app/
│
├── app.py                 # Flask backend with task management logic
├── templates/
│   └── index.html        # HTML frontend with forms and task display
├── static/
│   └── style.css         # Earthy aesthetic CSS styling
├── tasks.json            # Task storage file (auto-generated)
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore configuration
└── README.md            # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.x installed
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd todo-list-app
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
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5001
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
   cd todo-list-app
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   python3 app.py
   ```

4. **Access from network**
   The application runs on `0.0.0.0:5001`, making it accessible from other devices on your network.

## Usage

### Adding Tasks
1. Type your task in the input field
2. Select priority level: Low 🟢, Medium 🟡, or High 🔴
3. Optionally set a due date
4. Click "Add Task" or press Enter
5. Task appears in the list with priority badge

### Priority Levels
- **High Priority 🔥**: Red border, bouncing flame icon
- **Medium Priority ⭐**: Yellow border, rotating star icon
- **Low Priority 🌱**: Green border, growing plant icon

### Completing Tasks
- Click the circular checkbox next to any task to mark it as complete
- Enjoy the confetti celebration animation! 🎉
- Completed tasks show with a checkmark and green background
- Click again to mark as incomplete

### Filtering Tasks
Use the filter buttons to view:
- **All 📋**: Show all tasks
- **Active ⏳**: Show only incomplete tasks
- **Done ✅**: Show only completed tasks
- **High 🔴**: Show only high priority tasks
- **Medium 🟡**: Show only medium priority tasks
- **Low 🟢**: Show only low priority tasks

### Due Dates
- Tasks with due dates show ⏰ Due: [date]
- Overdue tasks pulse with a red warning
- Shake animation alerts you to overdue tasks

### Deleting Tasks
- Click the 🗑️ trash icon next to any task to delete it
- Task is immediately removed from the list

### Clearing Completed Tasks
- When you have completed tasks, a "Clear Completed Tasks" button appears
- Click it to remove all completed tasks at once

### Task Statistics
- View total tasks, pending tasks, and completed tasks at a glance
- Statistics update automatically as you add/complete/delete tasks

## Data Storage

- Tasks are stored in `tasks.json` file
- Data persists between application restarts
- Each task includes:
  - Unique ID
  - Task text
  - Completion status
  - Priority level (high, medium, low)
  - Due date (optional)
  - Creation timestamp

## Design Theme

🌿 **Earthy Aesthetic with Serene Elements**
- Cream, beige, and sage green color palette
- Cute decorative emojis (🌸, 🌿, 📝, ✅)
- Natural earth tones throughout
- Smooth animations and transitions
- Peaceful, calming interface

## API Endpoints

- `GET /` - Display all tasks
- `POST /add` - Add a new task (with priority and due date)
- `POST /delete/<task_id>` - Delete a specific task
- `POST /toggle/<task_id>` - Toggle task completion status
- `POST /clear` - Clear all completed tasks
- `GET /filter/<filter_type>` - Filter tasks (active, completed, high, medium, low)
- `POST /edit/<task_id>` - Edit task text

## Fun Features

### 🎉 Celebration Animation
- Completing a task triggers colorful confetti
- Checkbox scales up with a satisfying effect
- Makes task completion feel rewarding!

### 🎨 Priority Badges
- High priority: Bouncing 🔥 flame
- Medium priority: Rotating ⭐ star on hover
- Low priority: Growing 🌱 plant on hover

### ⚠️ Overdue Alerts
- Overdue tasks pulse with red shadow
- Due dates shake to grab attention
- Visual feedback keeps you on track

### 🌈 Smooth Animations
- Tasks slide in when added
- Completed tasks glow green
- Hover effects on all interactive elements
- Color-coded priority borders

## Future Enhancements

- Add task editing inline
- Include task categories/projects
- Add recurring tasks
- Implement task search
- Add user authentication for multiple users
- Include task notes/descriptions
- Export tasks to CSV/PDF
- Dark mode toggle
- Drag and drop to reorder tasks
- Task reminders/notifications

## Screenshots

The application features:
- Modern gradient background (cream to sage green)
- Clean white card design
- Interactive checkboxes with smooth animations
- Task statistics dashboard
- Responsive layout for all screen sizes

## Author

Created as part of a web development project.

## License

This project is open source and available for educational purposes.
