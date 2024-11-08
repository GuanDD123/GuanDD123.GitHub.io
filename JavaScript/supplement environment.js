function window() {
    window = global;
    window = {};
}

function plugin() {
    navigator.plugin = {
        plugins: {
            0: {
                0: { description: "", type: "" },
                name: "",
                length: 1,
                filename: "",
                description: "",
                length: 1
            }
        }
    };
    navigator.plugins[Symbol.toStringTag] = "PluginArray";
    navigator.plugins[0][Symbol.toStringTag] = "Plugin";
}

function getElementByTagName() {
    //参数和方法中具体实现、返回内容，需要根据调试结果来进行补充
    document = {
        getElementsByTagName: function (x) {
            return {}
        },
        createElement: function (x) {
            return {}
        }
    }
}

function canvas() {
    var document = {
        createElement: function createElement(x) {
            if (x == "canvas") {
                return {
                    toDataURL: function toDataURL() {
                        return "data:image/png;base64,* * * * * * ";
                    }
                }
            }
        }
    }
}

function JSDOM() {
    const jsdom = require('jsdom');
    const { JSDOM } = jsdom;
    const userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    const resourceLoader = new jsdom.ResourceLoader({
        userAgent: userAgent
    });
    const NewjsDom = new JSDOM(
        `
        <! DOCTYPE html>
        <html>
        <body>
        <div>
        <p> 爬虫逆向开发实战</p>
        </div>
        </body>
        </html>
        `,
        {
            resources: resourceLoader
        }
    );
    const window = NewjsDom.window; // window 对象
    const document = window.document; // document 对象
    console.log(window.navigator.userAgent)
}