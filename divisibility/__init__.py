from flask import Flask

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt'])

import divisibility.views
