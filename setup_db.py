from app import create_app
from models import db, User, Student, Instructor, Course, Lesson, Video

app = create_app()

def seed_data():
    with app.app_context():
        # Create all tables
        db.drop_all()
        db.create_all()
        print("Database tables created.")

        # Create Admin
        admin = User(username='admin', email='admin@lms.com', role='admin')
        admin.set_password('password123')
        db.session.add(admin)

        # Create Instructor
        instructor_user = User(username='john_doe', email='instructor@lms.com', role='instructor')
        instructor_user.set_password('password123')
        db.session.add(instructor_user)
        db.session.commit()

        instructor_profile = Instructor(user_id=instructor_user.id, title='Senior Developer', bio='Expert in Python and JS.')
        db.session.add(instructor_profile)
        db.session.commit()

        # Create Student
        student_user = User(username='jane_doe', email='student@lms.com', role='student')
        student_user.set_password('password123')
        db.session.add(student_user)
        db.session.commit()

        student_profile = Student(user_id=student_user.id, bio='Learning to code.')
        db.session.add(student_profile)
        db.session.commit()

        # Create Dummy Course
        course = Course(
            title='Mastering Full Stack Development',
            description='Learn to build amazing web applications from scratch.',
            category='Development',
            price=49.99,
            status='approved',
            instructor_id=instructor_profile.id
        )
        db.session.add(course)
        db.session.commit()

        # Create Dummy Lesson & Video
        lesson1 = Lesson(course_id=course.id, title='Introduction to Web Architecture', order=1)
        db.session.add(lesson1)
        db.session.commit()

        video1 = Video(lesson_id=lesson1.id, title='Client-Server Model', video_url='https://www.w3schools.com/html/mov_bbb.mp4', duration='10:05')
        db.session.add(video1)
        db.session.commit()

        print("Dummy data seeded successfully.")

if __name__ == '__main__':
    seed_data()
