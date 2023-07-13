from flask import Flask, render_template, request, jsonify
import calendar
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'  # Using SQLite for simplicity
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)

@app.route('/')
def home():
    year = datetime.now().year
    month = datetime.now().month
    _, num_days = calendar.monthrange(year, month)
    days = list(range(1, num_days + 1))
    return render_template('home.html', days=days)


@app.route('/update-habit', methods=['POST'])
def update_habit():
    data = request.get_json()
    habit = data['habit']
    status = data['status']
    date = datetime.strptime(data['date'], '%Y-%m-%d').date()  # Convert the string date to a datetime.date object

    habit_entry = Habit.query.filter_by(habit=habit, date=date).first()

    if habit_entry is None:
        habit_entry = Habit(habit=habit, status=status, date=date)
        db.session.add(habit_entry)
    else:
        habit_entry.status = status

    db.session.commit()

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
