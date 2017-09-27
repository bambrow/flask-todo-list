
from flask_script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("run", Server(host='0.0.0.0', port=5000, use_debugger=True))

if __name__ == '__main__':
    manager.run()