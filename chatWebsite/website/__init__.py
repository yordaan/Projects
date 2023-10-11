from flask_socketio import SocketIO
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

socketio = SocketIO()
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(debug=False):
    app: Flask = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjahjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    socketio.init_app(app)




    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def messageReceived(methods: ['GET', 'POST']):
        print('message was received!')

    @socketio.on("my event")
    def handle_my_custom_event(json, methods=['GET', 'POST']):
        print('received my event: ' + str(json))
        socketio.emit('my response', json, callback=messageReceived)

    return app


