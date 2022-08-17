import json
import re
import os

from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

from anki.buildinfo import version
from anki.hooks import addHook

from . import utils


def testFunction() -> None:
    cardCount = mw.col.cardCount()
    showInfo("💳 Card count: %d" % cardCount)


def setupGuiMenu() -> None:
    action = QAction("Jisho auto-add", mw)
    mw.form.menuTools.addSeparator()
    mw.form.menuTools.addAction(action)


def addButtons(buttons, editor):
    editor._links["generateFurigana"] = lambda ed=editor: doIt(
        ed, generate)
    return buttons + [
        editor._addButton(os.path.join(os.path.dirname(__file__), "icons",
                          "japanese.png"), "generate", tip=u"automatic generate form Jisho")
    ]


def doIt(editor, action):
    utils.Selection(editor, lambda s: action(editor, s))


def generate(editor, s):
    return


setupGuiMenu()
addHook("setupEditorButtons", addButtons)
# qconnect(action.triggered, testFunction)
