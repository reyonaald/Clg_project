from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# File to store tasks persistently
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    """Display all tasks"""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    task_text = request.form.get('task', '').strip()
    priority = request.form.get('priority', 'medium')
    due_date = request.form.get('due_date', '')
    
    if task_text:
        tasks = load_tasks()
        
        # Create new task with unique ID and fun features
        new_task = {
            'id': len(tasks) + 1 if tasks else 1,
            'text': task_text,
            'completed': False,
            'priority': priority,
            'due_date': due_date,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        tasks.append(new_task)
        save_tasks(tasks)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task by ID"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_completed():
    """Clear all completed tasks"""
    tasks = load_tasks()
    tasks = [task for task in tasks if not task['completed']]
    save_tasks(tasks)
    
    return redirect(url_for('index'))

@app.route('/filter/<filter_type>')
def filter_tasks(filter_type):
    """Filter tasks by type"""
    all_tasks = load_tasks()
    
    if filter_type == 'active':
        tasks = [task for task in all_tasks if not task['completed']]
    elif filter_type == 'completed':
        tasks = [task for task in all_tasks if task['completed']]
    elif filter_type == 'high':
        tasks = [task for task in all_tasks if task.get('priority') == 'high']
    elif filter_type == 'medium':
        tasks = [task for task in all_tasks if task.get('priority') == 'medium']
    elif filter_type == 'low':
        tasks = [task for task in all_tasks if task.get('priority') == 'low']
    else:
        tasks = all_tasks
    
    return render_template('index.html', tasks=tasks, filter_type=filter_type)

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    """Edit a task"""
    new_text = request.form.get('task', '').strip()
    
    if new_text:
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['text'] = new_text
                break
        save_tasks(tasks)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
