from urllib import parse


def split():
    parse.urlparse(url=str,  # 解析为六部分：<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
                   scheme='https:' | ...,
                   allow_fragments=False)
    parse.urlunparse(components=(
        '(scheme)', '(netloc)', '(path)', '(params)', '(query)', '(fragment)'))

    parse.urlsplit(url=str,  # 解析为五部分：<scheme>://<netloc>/<path>?<query>#<fragment>
                   scheme='https:' | ...,
                   allow_fragments=False)
    parse.urlunsplit(components=(
        '(scheme)', '(netloc)', '(path)', '(query)', '(fragment)'))

    parse.urljoin(base=str, url=str,  # 将 base 解析为四部分：<scheme>://<netloc>/<path>#<fragment>，使用 scheme、netloc、path 三部分内容，对 url 缺失部分进行补充
                  allow_fragments=False)


def code():
    parse.urlencode(query=dict)
    parse.parse_qs(qs=str)
    parse.parse_qsl(qs=str)

    parse.quote(string=str)
    parse.unquote(string=str)
