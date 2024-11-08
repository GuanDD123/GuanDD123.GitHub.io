## 1. HTTP/1.1 首部字段

HTTP 首部字段将定义成缓存代理和非缓存代理的行为，分成 2 种类型。

**端到端首部（End-to-end Header）**：分在此类别中的首部会转发给请求/响应对应的最终接收目标，且必须保存在由缓存生成的响应中，另外规定它必须被转发。

**逐跳首部（Hop-by-hop Header）**：分在此类别中的首部只对单次转发有效，会因通过缓存或代理而不再转发。
HTTP/1.1 和之后版本中，如果要使用 hop-by-hop 首部，需提供 Connection 首部字段。
除以下 8 个首部字段外，其他所有字段都属于端到端首部（Connection、Keep-Alive、Proxy-Authenticate、Proxy-Authorization、Trailer、TE、Transfer-Encoding、Upgrade）

### 1.1. 通用首部字段

Cache-Control：控制缓存的行为
Connection：逐跳首部、连接的管理
Date：创建报文的日期时间
Pragma：报文指令（仅作为与 HTTP/1.0 的向后兼容而定义）
Trailer：报文末端的首部一览
Transfer-Encoding：指定报文主体的传输编码方式
Upgrade：升级为其他协议
Via：代理服务器的相关信息
Warning：错误通知

#### 1.1.1. Cache-Control 指令

**缓存请求指令**
no-cache：强制向源服务器再次验证
no-store：不缓存请求或响应的任何内容
max-age=[秒]：响应的最大 Age 值
max-stale(=[秒])：接收已过期的响应
min-fresh=[秒]：期望在指定时间内的响应仍有效
no-transform：代理不可更改媒体类型
only-if-cached：从缓存获取资源
cache-extension：新指令标记（token）

**缓存响应指令**
public：可向任意方提供响应的缓存
private：仅向特定用户返回响应
no-cache：缓存前必须先确认其有效性
no-store：不缓存请求或响应的任何内容
no-transform：代理不可更改媒体类型
must-revalidate：可缓存但必须再向源服务器进行确认
proxy-revalidate：要求中间缓存服务器对缓存的响应有效性再进行确认
max-age=[秒]：响应的最大 Age 值
s-maxage=[秒]：公共缓存服务器响应的最大 Age 值
cache-extension：新指令标记（token）

#### 1.1.2. HTTP/1.1 Warning 警告码

110：Response is stale（响应已过期）：代理返回已过期的资源
111：Revalidation failed（再验证失败）：代理再验证资源有效性时失败（服务器无法到达等原因）
112：Disconnection operation（断开连接操作）：代理与互联网连接被故意切断
113：Heuristic expiration（试探性过期）：响应的使用期超过 24 小时（有效缓存的设定时间大于 24 小时的情况下）
199：Miscellaneous warning（杂项警告）：任意的警告内容
214：Transformation applied（使用了转换）：代理对内容编码或媒体类型等执行了某些处理时
299：Miscellaneous persistent warning（持久杂项警告）：任意的警告内容

### 1.2. 请求首部字段

Accept：用户代理可处理的媒体类型
Accept-Charset：优先的字符集
Accept-Encoding：优先的内容编码
Accept-Language：优先的语言（自然语言）
Authorization：Web 认证信息
Expect：期待服务器的特定行为
From：用户的电子邮箱地址
Host：请求资源所在服务器
If-Match：比较实体标记（ETag）
If-Modified-Since：比较资源的更新时间
If-None-Match：比较实体标记（与 If-Match 相反）
If-Range：资源未更新时发送实体 Byte 的范围请求
If-Unmodified-Since：比较资源的更新时间（与 If-Modified-Since 相反）
Max-Forwards：最大传输逐跳数
Proxy-Authorization：代理服务器要求客户端的认证信息
Range：实体的字节范围请求
Referer：对请求中 URI 的原始获取方
TE：传输编码的优先级
User-Agent：HTTP 客户端程序的信息

### 1.3. 响应首部字段

Accept-Ranges：是否接受字节范围请求
Age：推算资源创建经过时间
ETag：资源的匹配信息
Location：令客户端重定向至指定 URI
Proxy-Authenticate：代理服务器对客户端的认证信息
Retry-After：对再次发起请求的时机要求
Server：HTTP 服务器的安装信息
Vary：代理服务器缓存的管理信息
WWW-Authenticate：服务器对客户端的认证信息

### 1.4. 实体首部字段

Allow：资源可支持的 HTTP 方法
Content-Encoding：实体主体适用的编码方式
Content-Language：实体主体的自然语言
Content-Length：实体主体的大小（单位：字节）
Content-Location：替代对应资源的 URI
Content-MD5：实体主体的报文摘要
Content-Range：实体主体的位置范围
Content-Type：实体主体的媒体类型
Expires：实体主体过期的日期时间
Last-Modified：资源的最后修改日期时间

## 2. 为 Cookie 服务的首部字段

Set-Cookie：开始状态管理所使用的 Cookie 信息（响应首部字段）
Cookie：服务器接收到的 Cookie 信息（请求首部字段）

### 2.1. Set-Cookie 字段的属性

NAME=VALUE：赋予 Cookie 的名称和其值（必需项）
expires=DATE：Cookie 的有效期（若不明确指定则默认为浏览器关闭前为止）
path=PATH：将服务器上的文件目录作为 Cookie 的适用对象（若不指定则默认为文档所在的文件目录）
domain=域名：作为 Cookie 适用对象的域名 （若不指定则默认为创建 Cookie 的服务器的域名）
Secure：仅在 HTTPS 安全通信时才会发送 Cookie
HttpOnly：加以限制，使 Cookie 不能被 JavaScript 脚本访问
