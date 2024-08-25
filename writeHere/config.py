import os

class Config:
    SECRET_KEY = '066bb57df532020449df021398de2628'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # MAIL_SERVER = 'smpt.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USER_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')