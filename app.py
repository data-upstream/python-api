from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1.0/pandas/ts', methods=['POST'])
def convert_timeseries():
    if not request.json:
        abort(400)
    
    rng = pd.date_range('1/1/2011', periods=72, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    return ts.to_json(), 200


if __name__ == '__main__':
    app.run(
	debug=True,
	host = '0.0.0.0', port=5000
	)

