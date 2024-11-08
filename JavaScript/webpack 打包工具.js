/*
webpack 是一个 Js 应用程序的静态模块打包工具。
webpack 打包后的 Js 有 webpack_require 这一特征，且代码中有一个在自执行函数内的入口（这个入口可能在函数数组上边或其他文件夹中）。
*/

/**针对打包后 Js 文件的通用函数导出方法*/
var lx;
! function (e) {
    var report = {};
    function o(n) {
        if (report[n])
            return report[n].exports;
        var t = report[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return e[n].call(t.exports, t, t.exports, o),
            t.l = !0,
            t.exports
    }
    lx = o;
}({
    // 添加 webpack 模块
    // "method":function(e){}
});
// 调用模块函数
// var t = lx("method");

/*若实在调试困难，可使用 debundle 工具进行拆包还原，但会丢失一些元数据*/