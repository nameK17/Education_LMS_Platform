from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from models import db, User, Student, Instructor, Course, Lesson, Video

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    courses = Course.query.filter_by(status='approved').limit(6).all()
    return render_template('index.html', courses=courses)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'student')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('main.register'))
            
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        if role == 'student':
            profile = Student(user_id=new_user.id)
            db.session.add(profile)
        elif role == 'instructor':
            profile = Instructor(user_id=new_user.id)
            db.session.add(profile)
            
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('auth/register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        students_count = Student.query.count()
        instructors_count = Instructor.query.count()
        courses_count = Course.query.count()
        return render_template('dashboards/admin.html', 
                               students=students_count, 
                               instructors=instructors_count, 
                               courses=courses_count)
    elif current_user.role == 'instructor':
        courses = Course.query.filter_by(instructor_id=current_user.instructor_profile.id).all()
        return render_template('dashboards/instructor.html', courses=courses)
    else:
        courses = Course.query.filter_by(status='approved').all()
        return render_template('dashboards/student.html', courses=courses)

@bp.route('/course/<int:course_id>')
def course_details(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('courses/details.html', course=course)

@bp.route('/lesson/<int:lesson_id>')
@login_required
def lesson_view(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    return render_template('courses/lesson.html', lesson=lesson)
