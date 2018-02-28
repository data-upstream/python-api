from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1.0/pandas/ts/downsample', methods=['POST'])
def convert_timeseries():
    if not request.json:
        abort(400)
    
    ts = pd.Series(request.json.get('data'), index=request.json.get('index'))
    return ts.to_json(), 200


if __name__ == '__main__':
    app.run(
	debug=True,
	host = '0.0.0.0', port=5000
	)

