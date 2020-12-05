from microblog.app.models import User, Post, Message, Notification
from microblog.app import cli, create_app, db

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}


# Go to directory and put in command below
# .\bin\elasticsearch.bat
