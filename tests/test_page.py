from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect

from config import settings 
import logging

def test_checkbox(page:Page):
    logging.info("Открываем страницу")
    page.goto(settings.CHECKBOX_URL)
    title = page.title()
    logging.debug(f'Заголовок страницы {title}')
    page.get_by_label('Default checkbox').check()
    page.get_by_label('Checked checkbox').check()
    page.get_by_label('Default radio').check()
    page.get_by_label('Default checked radio').check()
    page.get_by_label('Checked switch checkbox input').check()
    page.get_by_label('Default checkbox').click()
    page.get_by_label('Checked checkbox').click()
    page.get_by_label('Default radio').click()
    page.get_by_label('Default checked radio').click()
    page.get_by_label('Checked switch checkbox input').click()
    assert "Checks-radios demo" in title
