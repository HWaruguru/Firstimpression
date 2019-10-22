import os
from app import create_app, db
from flask_script import Manager
from app.models import User
from config import config_options
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.environ['ENV'])
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
