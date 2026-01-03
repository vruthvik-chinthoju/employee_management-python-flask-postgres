from flask import Flask,render_template,request,url_for,flash,redirect
from models import Manager,db,Employee
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
import os
from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.secret_key = os.getenv("SECRET_KEY")

app.config.update(
    PERMANENT_SESSION_LIFETIME=timedelta(days=1),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax"
)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Manager.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email','')
        password = request.form.get('password','')
        email_exists = Manager.query.filter_by(email=email).first()
        if email_exists:
            flash("Email Already exists")
            return redirect(url_for('register'))
        else:
            hashed_password = generate_password_hash(password)
            manager = Manager(name=name,email=email,password=hashed_password)
            db.session.add(manager)
            db.session.commit()
            flash("Account Registered Succesfully")
            return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email','')
        password = request.form.get('password')
        user = Manager.query.filter_by(email=email).first()
        if not user:
            flash("Email not Found")
            return redirect(url_for('login'))
        if  check_password_hash(user.password,password):
                login_user(user,remember=True)
                return redirect(url_for('emp'))
        else:
                flash("You Have Entered Incorrect Password")
                return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/employee',methods=['POST','GET'])
@login_required
def emp():
    if request.method =='POST':
        emp_name = request.form.get('name','')
        emp_email = request.form.get('email','')
        emp_department = request.form.get('department','')
        emp_salary = request.form.get('salary','')
        user = Employee(name=emp_name,email=emp_email,department=emp_department,salary=emp_salary,manager_id=current_user.id)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('emp'))
    employees = Employee.query.filter_by(manager_id=current_user.id).all()
    emp_id = request.args.get("id")
    selected = None
    if emp_id :
        selected = Employee.query.filter_by(id=int(emp_id),manager_id=current_user.id).first_or_404()

    return render_template('emp.html',emps=employees,selected=selected)

@app.route('/employee/update/<int:id>/',methods=['GET','POST'])
@login_required
def update(id):
    emp = Employee.query.filter_by(id=id, manager_id=current_user.id).first_or_404()
    if request.method=='POST':
        emp.name = request.form['name']
        emp.email = request.form['email']
        emp.department = request.form['department']
        emp.salary = request.form['salary']
        db.session.commit()
        return redirect(url_for('emp'))

    return redirect(url_for('emp'))


@app.route('/employee/delete/<int:id>/')
@login_required
def delete(id):
    emp = Employee.query.filter_by(id=id, manager_id=current_user.id).first_or_404()
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('emp'))

@app.route('/employee/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out Successfully")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run()
