import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-premium-key-123'
    # Use SQLite by default for easy portfolio setup. 
    # To use MySQL, uncomment the line below and update credentials:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/education_platform'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'education_platform.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
