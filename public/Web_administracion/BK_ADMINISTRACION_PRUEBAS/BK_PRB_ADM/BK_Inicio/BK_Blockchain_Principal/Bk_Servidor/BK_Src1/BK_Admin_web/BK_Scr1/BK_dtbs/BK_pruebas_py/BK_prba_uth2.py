# from flask import session, redirect, url_for
# from functools import wraps

# def login_required(f):
   # @wraps(f)
    # def decorated_function(*args, **kwargs):
       # if 'logged_in' not in session:
            # return redirect(url_for('login'))
       # return f(*args, **kwargs)
  #  return decorated_function

# def login_user(username, password):
    # Lógica para autenticar al usuario
   # pass

# def logout_user():
    # session.pop('logged_in', None)
