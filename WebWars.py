from flask import Flask
from database import *
from controllers import *

if __name__ == '__main__':
    DB.create_all()
    APP.run(debug=True)
