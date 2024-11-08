import base64
import hashlib
import hmac


def base64_(S: str):
    base64.b64encode(S.encode())  # base64 编码
    base64.b64decode(S.encode())  # base64 解码


def md5_(S: str):
    md5 = hashlib.md5()
    md5.update(S.encode())
    md5.hexdigest()


def SHA1(S: str):
    sha1 = hashlib.sha1()
    sha1.update(S.encode())
    sha1.hexdigest()


def HMAC(S: str):
    hmac_ = hmac.new(key=S.encode(), msg=S.encode(), digestmod=hashlib.sha256)
    hmac_.digest()  # 二进制格式
    hmac_.hexdigest()  # 十六进制格式
