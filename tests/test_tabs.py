from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect
from config import settings 
import logging
from utils.asserts import check

def test_tabs(page: Page):
    page.goto(settings.TABS_URL)
    with page.context.expect_page() as tab:
        page.get_by_text('Переход к Dashboard').click()
    
    new_tab = tab.value
    check(new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?", f"Проверка url вкладки Dashboard")
    #assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sing_out = new_tab.get_by_text('Sign out')
    check(sing_out.is_visible(), f"На вкладке Dashboard Sign out")
    assert sing_out.is_visible()
    