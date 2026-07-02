# Premium Education Platform (LMS)

A robust, modern Learning Management System built for showcasing in a software developer portfolio.

## Tech Stack
- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite (configured for easy transition to MySQL)
- **Frontend:** Vanilla HTML5, CSS3, JavaScript
- **Design:** Custom Glassmorphism, Dark Theme, Fully Responsive

## Features
- **Role-based Authentication:** Admin, Instructor, Student accounts.
- **Admin Dashboard:** Platform analytics, user management, and course approval (mock UI implemented).
- **Instructor Dashboard:** Course creation, lesson management, and student tracking.
- **Student Dashboard:** Course browsing, video lectures, assignments, and progress tracking.
- **Premium UI:** Smooth animations, backdrop blur (glassmorphism), and gradient aesthetics without external CSS frameworks like Bootstrap.

## Setup Instructions

1. **Create Virtual Environment & Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Initialize Database and Seed Dummy Data:**
   This script creates the database tables and populates them with an admin account, an instructor, a student, and a sample course.
   ```bash
   python setup_db.py
   ```

3. **Run the Application:**
   ```bash
   python app.py
   ```
   
4. **Access the LMS:**
   Open your browser and navigate to `http://localhost:5000`

### Test Accounts:
- **Admin:** admin@lms.com / password123
- **Instructor:** instructor@lms.com / password123
- **Student:** student@lms.com / password123

## Database Migration to MySQL
To use MySQL instead of SQLite:
1. Ensure MySQL is running on your machine.
2. Edit `config.py` and uncomment the MySQL URI line.
3. Update the credentials (`username:password@localhost/dbname`).
4. Re-run `python setup_db.py`.
