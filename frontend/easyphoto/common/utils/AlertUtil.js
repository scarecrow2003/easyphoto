'use strict';

function AlertUtil() {
    var toastr = require("toastr");
    toastr.options.timeOut = 3000;
    toastr.options.extendedTimeOut = 10000;

    var self = this;

    self.toastAlert = function(funcName, message) {
        var fn = toastr[funcName];
        if (typeof fn === 'function') {
            fn(message);
        }
    };

    self.promptSuccess = function(message) {
        self.toastAlert('success', message);
    };

    self.promptError = function(msg) {
        self.toastAlert('error', msg);
    };

    self.promptInfo = function(msg) {
        self.toastAlert('info', msg);
    };

    self.promptWarning = function(msg) {
        self.toastAlert('warn', msg);
    };

}

module.exports = new AlertUtil();