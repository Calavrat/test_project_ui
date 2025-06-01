from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect
from config import settings 
import logging

def test_dialog_promt(page: Page):
    page.goto(settings.DIALOG_URL)
    logging.info("Открываю страницу")
    title = page.title()
    value = '123'
    logging.debug(f"Загаловок страницы {title}")
    page.on('dialog', lambda dialog:dialog.accept(f"{value}"))
    page.get_by_text('Диалог Prompt').click()
    element = page.get_by_role('alert')
    print(element.text_content())
    print(element.inner_text())
    assert "You have entered number: 123" in element.text_content()
    assert "replit" in title
# def test_dialog_confirmation(page: Page):
#     page.goto(settings.DIALOG_URL)
#     logging.info("Открываю страницу")
#     title = page.title()
#     logging.debug(f"Загаловок страницы {title}")
#     page.on('dialog', lambda dialog:dialog.dismiss())
#     page.get_by_text('Диалог Confirmation').click()
#     assert "replit" in title
# def test_dialog_alert(page: Page):
#     page.goto(settings.DIALOG_URL)
#     logging.info("Открываю страницу")
#     title = page.title()
#     logging.debug(f"Загаловок страницы {title}")
#     page.on('dialog', lambda dialog:dialog.accept())
#     page.get_by_text('Диалог Alert').click()
#     assert "replit" in title
