from flask import Flask, render_template
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
    habit = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def home():
    year = datetime.now().year
    month = datetime.now().month
    _, num_days = calendar.monthrange(year, month)
    days = list(range(1, num_days + 1))
    return render_template('home.html', days=days)

if __name__ == '__main__':
    app.run(debug=True)
