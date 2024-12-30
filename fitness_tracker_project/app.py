from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for exercises
exercises = [
    {"id": 1, "name": "Push-ups", "description": "A basic upper body exercise to strengthen chest and arms.", "calories_burned": 100},
    {"id": 2, "name": "Squats", "description": "Strengthens legs and core muscles.", "calories_burned": 120},
    {"id": 3, "name": "Jumping Jacks", "description": "A cardio exercise to improve stamina.", "calories_burned": 150},
    {"id": 4, "name": "Plank", "description": "Enhances core stability and strength.", "calories_burned": 50}
]

@app.route('/')
def home():
    return render_template('home.html', exercises=exercises)

@app.route('/exercise/<int:exercise_id>')
def exercise_detail(exercise_id):
    exercise = next((e for e in exercises if e["id"] == exercise_id), None)
    if exercise:
        return render_template('exercise_detail.html', exercise=exercise)
    return "Exercise not found", 404

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        user_name = request.form['name']
        exercise_id = int(request.form['exercise'])
        exercise = next((e for e in exercises if e['id'] == exercise_id), None)
        if exercise:
            return render_template('log_success.html', name=user_name, exercise=exercise)
    return render_template('log.html', exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
