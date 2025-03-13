# Igor_class_work_L17.

# https://httpbin.org/
# https://requests.readthedocs.io/en/latest/user/quickstart/#
# http://grp.nalog.gov.by/grp/rest-api //free API.
# https://free-apis.github.io/#/categories
# https://flask.palletsprojects.com/en/2.2.x/
# https://getbootstrap.com/docs/5.3/getting-started/introduction/


# C:\Users\igor_zzz>pip install requests

# import json


import requests


r = requests.get("https://httpbin.org/get")
r.headers
{'Date': 'Wed, 12 Mar 2025 16:07:23 GMT', 'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
r.text
'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.32.3", \n    "X-Amzn-Trace-Id": "Root=1-67d1b13b-6777f76e553516781ed513aa"\n  }, \n  "origin": "46.53.250.241", \n  "url": "https://httpbin.org/get"\n}\n'
''

r = requests.get("https://httpbin.org/put", data={"key": "value"})
