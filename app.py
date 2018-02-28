from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return "Python API online!"

# {"index": [], "data": []}; range: e.g. "1h", 2d" "20m", etc..
@app.route('/api/v1.0/pandas/ts/downsample/<range>', methods=['POST'])
def downsample(range):
    if not request.json:
        abort(400)

    try:
        index = request.json.get('index')
        ts = pd.Series(request.json.get('data'), list(map(lambda x: pd.to_datetime(x), index)))
        tsResample = ts.resample(range)
        if 'mean' in request.args:
            tsResample = ts.resample(range).mean()
    except:
        abort(400)

    return tsResample.to_json(), 200


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', port=5000
    )

