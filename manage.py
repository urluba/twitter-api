'''
DB Management wrapper
'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

application = create_app()
migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
