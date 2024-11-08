from json import dumps
from requests import post

value = ''
url = "http://127.0.0.1:12080/go"
data = {
    "group": "zzz",
    "action": "getData",
    "param": dumps({
        "key": value
    })
}

res = post(url=url, data=data)
print(res.text)
