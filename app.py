from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
db = SQLAlchemy(app)

# Login Setup
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    expenses = db.relationship('Expense', backref='owner', lazy=True)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    currency = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Chart Logic
def generate_chart(user_expenses):
    if not user_expenses: return False
    data = {}
    for e in user_expenses:
        data[e.category] = data.get(e.category, 0) + e.amount

    plt.figure(figsize=(6, 4))
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', colors=['#0056b3', '#007bff', '#cce5ff'])
    plt.savefig(os.path.join('static', 'images', f'chart_{current_user.id}.png'))
    plt.close()
    return True


# --- Routes ---
@app.route('/')
@login_required
def index():
    user_expenses = Expense.query.filter_by(user_id=current_user.id).all()
    total = sum(e.amount for e in user_expenses)
    has_chart = generate_chart(user_expenses)
    # Default currency from last entry or USD
    curr = user_expenses[0].currency if user_expenses else "$"
    return render_template('index.html', expenses=user_expenses, total=total, has_chart=has_chart, curr=curr)
@app.route('/link-bank', methods=['POST'])
@login_required
def link_bank():
    # Simulate an API call to a bank
    bank_name = request.form.get('bank_name')
    # In a real app, Plaid API would return the balance here
    mock_balance = 5250.75
    flash(f"Successfully linked to {bank_name}! Current Balance: ${mock_balance}")
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
@login_required
def add_expense():
    new_ex = Expense(
        category=request.form.get('category'),
        amount=float(request.form.get('amount')),
        currency=request.form.get('currency'),
        user_id=current_user.id
    )
    db.session.add(new_ex)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.password == request.form.get('password'):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_user = User(username=request.form.get('username'), password=request.form.get('password'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    target_amount = db.Column(db.Float)
    current_saved = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class BudgetPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    limit_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)