from distutils.log import debug
from flask_app import app
from flask_app.controllers import dojos_controllers
from flask_app.controllers import ninjas_controllers

if __name__=="__main__":
    app.run(debug=True)