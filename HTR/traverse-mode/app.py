from flask import Flask, render_template, request, redirect, url_for, flash
from get_images import images_page, images_getter
from login import login_now
from util import get_root_dir
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from ipban import ip_ban
from flask_login import LoginManager, login_required, logout_user, current_user
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
db.init_app(app)

app.config['decode_query_strings'] = False

# set debug pin #
class MyDebuggedApplication(DebuggedApplication):
    def get_pin(self, environ):
        return '69420'

# login manager handdler #
from models import User

login_manager = LoginManager()
#login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

app.config['PUBLIC_IMG_FOLDER'] = f"{get_root_dir()}/static/img"
app.config['SECRET_KEY'] = 'jangankepomase'

@app.route("/")
def home():
    ip_address = request.remote_addr
    ip_ban.remove(ip_address)
    return render_template('home.html')

@app.route('/images', methods=['GET'])
def image():
    return images_page(request, app)

@app.route('/get-images', methods=['GET'])
def load_image():
    return images_getter(request, app)

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_now(request)

@app.route('/logout')
@login_required
def logout():
    flash('Logged out successfully!', category='success')
    logout_user()
    return render_template('home.html')

'''
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:login
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login_user(new_user, remember=True)
            flash('Account created!', category='success')
            #return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
'''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

