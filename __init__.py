from aqt import mw
from aqt.utils import showInfo, qconnect
import aqt.qt as qt


def testFunction() -> None:
    cardCount = mw.col.cardCount()
    showInfo("💳 Card count: %d" % cardCount)


action = qt.QAction("Jisho auto-add", mw)
qt.qconnect(action.triggered, testFunction)
menu = qt.QMenu('&Jisho auto-add', mw)
action = menu.addAction("&Count all cards")
mw.form.menuTools.addMenu(menu)
