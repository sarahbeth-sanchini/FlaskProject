from app import create_app, db  # app/__init__ (ROOT PACKAGE)
#from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev') #pass either test,prod or dev config settings
    with flask_app.app_context():
        db.create_all()
        #if not User.query.filter_by(user_name='harry').first():
         #   User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    flask_app.run()


## NOTES ##
#app.context() is a method so Flask knows which context (or app, because
        #multiple apps with different configurations could be running) The default is current app