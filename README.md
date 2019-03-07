# python-api

* cd DIR
* python3.X -m virtual-env .
* sourde bin/activate
* pip install -r requirements.txt
* python app.py

## deployed at

https://python-api.data-upstream.ch/


## POST '/api/v1.0/pandas/ts/downsample/<range>'

payload={"index": [], "data": []};
range: e.g. "1h", 2d" "20m", etc..

optional ?mean=1 parameter for mean output

## more functions see app.py