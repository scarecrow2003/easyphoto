'use strict';

function AlertUtil() {
    var request = require('reqwest');
    var when = require('when');
    var Alert = require('./AlertUtil');
    var cookie = require('react-cookie');
    var $ = require('jquery');
    var self = this;

    self.ajax = function(url, method, payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage) {
        var message = "";
        var data = {
            url: url,
            method: method,
            crossOrigin: true,
            type: 'json',
            headers: {
                'X-CSRFToken': cookie.load('csrftoken'),
                'Content-Type': 'application/json'
            }
        };
        if (payload) {
            $.extend(data, {data: JSON.stringify(payload)});
        }
        return when(request(data)).then(function(response) {
            if (response.result === 'failed') {
                if (requestFailedCallback) {
                    requestFailedCallback();
                }
                message = response.message;
                if (failMessage && failMessage != "") {
                    message = failMessage;
                }
                if (message === null || message === "") {
                    message = "Failed";
                }
                Alert.promptError(message);
            } else {
                if (successCallback) {
                    successCallback(response);
                }
                if (hideMessage == null || !hideMessage) {
                    message = "Successful";
                    if (successMessge && successMessge != "") {
                        message = successMessge;
                    }
                    Alert.promptSuccess(message);
                }
            }
        }).catch(function(e) {
            if (errorCallback) {
                errorCallback();
            }
            if (hideMessage == null || !hideMessage) {
                message = "Server error";
                if (errorMessage && errorMessage != "") {
                    message = errorMessage;
                }
                Alert.promptError(message);
            }
        });
    };

    self.ajaxGet = function(url, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage) {
        return self.ajax(url, "GET", null, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage);
    };

    self.ajaxPost = function(url, payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage) {
        return self.ajax(url, "POST", payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage);
    };

    self.ajaxPut = function(url, payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage) {
        return self.ajax(url, "PUT", payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage);
    };

    self.ajaxDelete = function(url, payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage) {
        return self.ajax(url, "DELETE", payload, successCallback, errorCallback, requestFailedCallback, hideMessage, successMessge, errorMessage, failMessage);
    };
}

module.exports = new AlertUtil();