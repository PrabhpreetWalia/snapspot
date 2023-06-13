from flask import Flask

app = Flask(__name__)

import mainPage, adminPage

app.run(debug = True)