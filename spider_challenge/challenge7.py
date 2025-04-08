import time
import requests
import urllib3
from requests import Session
session = Session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cookies = {
    'sessionid': 't54wg8mu0o6iq5d48fiejdtugzw1y502',
}

headers = {
    'referer': 'https://www.python-spider.com/challenge/7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
# session.headers.clear()
# session.headers.update(headers)
for p in range(1, 101):
    data = {
        'page': p,
    }
    session.post('https://www.python-spider.com/cityjson', cookies=cookies, headers=headers, data=data, verify=False)
    response = session.post('https://www.python-spider.com/api/challenge7', cookies=cookies, headers=headers, data=data, verify=False)
    # time.sleep(2)
    json_data = response.json()
    print(json_data)
