from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect
from config import settings 
import logging

def test_drag_drop(page: Page):
    logging.info("Открываю страницу")
    page.goto(settings.DRAG_DROP_URL)
    title = page.title()
    logging.debug(f"Загаловок страницы {title}")
    page.drag_and_drop("#drag", "#drop")
    assert "FFF" in title
