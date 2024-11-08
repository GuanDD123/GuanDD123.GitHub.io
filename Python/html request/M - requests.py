import requests
from io import TextIOWrapper


def send_request():
    requests.request(method='get' | 'post' | ..., url=str)

    requests.get(url=str,
                 params=dict,
                 headers=dict,
                 timeout=float | (float, float),  # tuple 类型分别指定了连接和读取的 timeout
                 proxies=dict,  # socks 代理需安装 requests[socks] 包
                 verify=False)  # 不验证网站的 CA 证书
    requests.post(url=str,
                  data=dict,  # content-type 为 application/x-www-form-urlencoded 时使用
                  json=dict,  # content-type 为 application/json 时使用
                  files=dict[str, TextIOWrapper],  # content-type 为 multipart/form-data 时使用
                  headers=dict,
                  timeout=float | (float, float),
                  proxies=dict,
                  verify=False,
                  allow_redirects=False)  # 不自动重定向


def response_info(resp: requests.Response):
    resp.headers
    resp.url
    resp.history  # 返回请求历史的响应对象列表
    resp.encoding
    resp.encoding = 'utf-8' | ...  # 设置 Response 编码


def response_content(resp: requests.Response):
    resp.text
    resp.content
    resp.json()


def http_status_code(resp: requests.Response):
    resp.status_code

    200 == requests.codes.ok
    206 == requests.codes.partial_content
    403 == requests.codes.forbidden
    404 == requests.codes.not_found


def get_cookie(resp: requests.Response):
    resp.cookies
    resp.cookies.get_dict()
    resp.cookies.items()
    resp.cookies.keys()
    resp.cookies.values()


def use_cookie():
    from requests.cookies import RequestsCookieJar

    requests.get(url=str, headers={'Cookie': str})

    cookiejar = RequestsCookieJar()
    cookiejar.set(name=str, value=str | dict[str, str])
    requests.get(url=str, cookies=cookiejar)


def http_basic_auth():
    from requests.auth import HTTPBasicAuth

    requests.get(url=str, auth=(str['username'], str['password']))

    auth = HTTPBasicAuth(username=str, password=str)
    requests.get(url=str, auth=auth)


def session_():
    from requests import Session

    session = Session()
    session.cookies
    session.cookies.set(name=str, value=str | dict[str, str])
    session.get(url=str)


def Request_():
    from requests import Session, Request

    request = Request(url=str, method='get' | 'post' | ...)
    session = Session()
    prepared_request = session.prepare_request(request=request)
    session.send(request=prepared_request)
