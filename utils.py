import json
import re

from aqt.utils import showInfo, qconnect
from aqt.qt import *

from anki.buildinfo import version


class Selection:
    js_get_html = u"""
        var selection = window.getSelection();
        var range = selection.getRangeAt(0);
        var div = document.createElement('div');
        div.appendChild(range.cloneContents());
        div.innerHTML;
    """

    def __init__(self, window, callback):
        self.window = window
        self.setHtml(None, callback)

    def isDeprecated(self):
        return int(version.replace('.', '')) < 2141

    def setHtml(self, elements, callback, allowEmpty=False):
        self.selected = elements
        if self.selected == None:
            if self.isDeprecated():
                self.window.web.eval("setFormat('selectAll');")
                self.window.web.page().runJavaScript(
                    self.js_get_html, lambda x: self.setHtml(x, callback, True))
            else:
                self.window.web.page().runJavaScript("getCurrentField().fieldHTML",
                                                     lambda x: self.setHtml(x, callback, True))
            return
        self.selected = self.convertMalformedSpaces(self.selected)
        callback(self)

    def convertMalformedSpaces(self, text):
        return re.sub(r'& ?nbsp ?;', ' ', text)

    def modify(self, html):
        html = self.convertMalformedSpaces(html)
        if self.isDeprecated():
            self.window.web.eval(
                "setFormat('insertHTML', %s);" % json.dumps(html))
        else:
            self.window.web.page().runJavaScript(
                "getCurrentField().fieldHTML = %s;" % json.dumps(html))
