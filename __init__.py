from aqt.qt import QAction

from anki.hooks import addHook


def reset_selected_cards(browser):
    cards = browser.model.browser.selectedCards()
    browser.col.sched.resetCards(cards)
    browser.col.sched.removeLrn(cards)
    browser.model.reset()
    browser.mw.requireReset()


def add_menu_item(browser, m):
    action = QAction("Reset cards", browser.mw)
    action.triggered.connect(lambda: reset_selected_cards(browser))
    m.addAction(action)


addHook('browser.onContextMenu', add_menu_item)
