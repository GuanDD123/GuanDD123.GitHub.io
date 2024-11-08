代码混淆本质是对代码标识符和结果的调整，从而达到不可读不可调试的目的。

## 1. eval 混淆

eval 是浏览器 v8 引擎定义的一个方法，具有执行 Js 代码的能力。

eval(String)：String 为要计算的 Js 表达式或要执行的语句

## 2. 常量的混淆

**十六进制字符串**：将字符串以 “十六进制” 形式表示 ('\x..')
**unicode 字符串**：将字符串以 “unicode” 形式表示 ('\u....')

**ASCII 码**：将字符串以 “字节数组” 的形式表示
```js
'x'.charCodeAt(0); //120
'b'.charCodeAt(0); //98
String.fromCharCode(120, 98); //xb
String.fromCharCode.apply(null, [120, 98]); //xb
```

## 3. 数组混淆、数组乱序

**数组混淆**：将脚本的所有字符串进行提取加密，在 js 脚本头部组成加密字符串数组，之后的字符串调用以获取数组的形式获取字符串。
**特征**：混淆脚本头部会存在一个较长的字符串加密数组。

**数组乱序还原函数的特征**：代码中包含 push 和 shift 字符串，用于打乱数组顺序。
```js
/**打乱数组顺序*/
(function (array, num) {
    var shuffer = function (nums) {
        while (--nums) {
            array.unshift(array.prototype());
        }
    };
    shuffer(++num)
})(Array, Number)

/**还原数组顺序*/
(function (array, num) {
    var shuffer = function (nums) {
        while (--nums) {
            array.push(array.shift());
        }
    };
    shuffer(++num)
})(Array, Number)
```

## 4. aa 混淆、jj 混淆

aa 混淆：将 Js 代码转换为常用的网络表情
jj 混淆：将 Js 代码转换为只有符号的字符串（代码中会有很多 “$”）

## 5. Jsfuck 混淆

在 Js 中，false 可表示为 “![]”，true 可表示为 “!![]”，NaN 可表示为 “+[![]]”。

Jsfuck混淆：使用 6 个字符 “[ ] ! ( ) +” 进行混淆

## 6. OLLVM 混淆

**OLLVM (Obfuscator-LLVM) 有三大功能：**
控制流平坦化 (Control Flow Flattening)
虚假控制流 (Bogus Control Flow)
指令替换 (Instructions Substitution)

**控制流平坦化**：主要是以基本块为单位，通过一个主分发器控制程序的执行流程。
在代码上体现出来可简要理解为 while+switch 结构，主分发器可以理解为 switch。
**优点**：可以模糊基本块之间的前后关系，增加分析难度
**缺点**：会降低代码运行速度，增加代码量
**特征**：存在一个 while 结构，其中包含多个以数字为判断条件的 case 结构，在它上面的变量声明一般为分发器。

**虚假控制流**：将原来的一个基本块膨胀成若干个虚假的基本块与该基本块的比较判断结构，通过一个控制变量保证控制流能运行到原来的那个基本块。
**缺点**：代码膨胀率较高。

**指令替换**：对标准二进制运算使用更复杂的指令序列进行功能等价替换，当存在多种等价指令序列时，随机选择一种。
提供一个伪随机数，可以使指令替换给二进制文件带来多样性。
**缺点**：通过重新优化可以很容易把替换的等价指令序列变回去。

**去 OLLVM 混淆的方法**：利用符号执行、使用 AST 语法树

## 7. base64 编码

base64 是一种基于 64 个可打印 ASCII 字符对任意字节数据进行编码的算法。
base64 编码后的字符串末尾通常为 “=”。

**在浏览器中使用：**
进行 base64 编码：btoa(String)
解码 base64 文本：atob(String)

**在 Nodejs 中使用：**
```js
// base64 编码
let base64_encode = Buffer.from(String).toString('base64');
// base64 解码
let base64_decode = Buffer.from(base64_encode, 'base64').toString('ascii');
```

## 8. MD5 加密

MD5 消息摘要算法 (MD5 Message-Digest Algorithm) 可以生成 128 位（16 字节）的散列值 (hash value)。
MD5 加密不可逆。

**加密过程中使用的固定数值常量**：0x67452301、0xefcdab89、0x98badcfe、0x10325476

```js
const CryptoJs = require('crypto-js');
CryptoJs.MD5(String).toString();
```

## 9. SHA1 加密

SHA1 (Secure Hash Algorithm) 安全哈希算法

SHA1 比 MD5 安全性更强。
对于长度小于 2^64 位的消息，SHA1 生成一个 160 位的消息摘要。
SHA1 加密的关键词一般为 Sha1。

**加密过程中使用的固定数值常量**：0x67452301、0xefcdab89、0x98badcfe、0x10325476、0xc3d2e1f0 (0xd1e6b788 ^ 0x12345678)

```js
const CryptoJs = require('crypto-js');
CryptoJs.SHA1(String).toString();
```

## 10. HMAC 加密

HMAC (Hash Message Authentication Code) 散列消息鉴别码

HMAC 是一种基于加密 hash 函数和共享密钥的消息认证协议。
**原理**：使用公开函数和密钥生成一个固定长度的值作为认证标识，用这个标识鉴别消息的完整性。

```js
const CryptoJs = require('crypto-js');
let hash = CryptoJs.HmacSHA256(String['message'], String['key']);
CryptoJs.enc.Hex.stringify(hash);
```

## 11. DES 加密

DES (Data Encryption Standard) 数据加密标准
DES 以 64 位为分组对数据加密，加密和解密使用同一个算法，属于对称加密算法。

密钥可以是任意的 56 位数（因为每个第 8 位都用作奇偶校验），而且可以任意时候改变。

**DES 加密的搜索关键词**：DES、mode、padding 等。

```js
const CryptoJs = require('crypto-js');
let password = CryptoJs.enc.Utf8.parse(String);
let key = CryptoJs.enc.Utf8.parse(String);
cfg = {
    mode: CryptoJs.mode.ECB,
    padding: CryptoJs.pad.Pkcs7
};
// DES 加密
let encPwd = CryptoJs.DES.encrypt(password, key, cfg).toString();
// DES 解密
let decPwd = CryptoJs.DES.decrypt(encPwd, key, cfg).toString(CryptoJs.enc.Utf8);
```

## 12. AES 加密

AES (Advanced Encryption Standard) 高级加密标准，又称 Rijndael 加密法
AES 是一种区块加密标准，属于对称加密算法。

**AES 常用填充模式**：NoPadding、ZeroPaadding、Pkcs7（默认值）
**AES 加密的搜索关键词**：AES、mode、padding 等

```js
const CryptoJs = require('crypto-js');
cfg = {
    mode: CryptoJs.mode.ECB,
    padding: CryptoJs.pad.Pkcs7
};
// AES 加密
let encPwd = CryptoJs.AES.encrypt(String['password'], String['key'], cfg).toString();
// AES 解密
let key = CryptoJs.enc.Utf8.parse(String['key']);
let decPwd = CryptoJs.AES.decrypt (encPwd, key, cfg).toString(CryptoJs.enc.Utf8);
```

## 13. RSA 加密

RSA (Rivest-Shamir-Adleman) 属于非对称加密算法

**RSA 常见标志**：setPublickey

```js
window = global;
const JSEncrypt = require ('jsencrypt');
let jse = new JSEncrypt();
// 加密
publickey = 'public_key.pem';
jse.setPublicKey(publickey);
let encStr = jse.encrypt(String['password']);
// 解密
privatekey = 'private_key.pem';
jse.setPrivateKey(privatekey);
let Str = jse.decrypt(encStr);
```

## 14. soJson 加密

soJson 是一个加密工具。
一般加密后的 Js 文件会有特征，如 soJson.com.v5、jsjiami.com.v6。

## 15. lsb 隐写

**原理**：将 Js 代码隐藏到特定的介质中，其通过最低有效位 (LSB) 算法嵌入到图片的 RGB 通道、隐藏到图片 EXIF 元数据或 HTML 空白字符中。
**破解方式**：在源码的上下文中劫持或替换关键函数的调用，将其修改为文本输出，即可得到载体中隐藏的代码。
