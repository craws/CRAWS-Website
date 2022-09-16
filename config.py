# Don't edit this file. To override settings please use instance/production.py

DEBUG = False

# Security
SESSION_COOKIE_SECURE = False  # Should be True in production.py if using HTTPS
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
