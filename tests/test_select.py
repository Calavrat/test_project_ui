from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect

from config import settings 
import logging

def test_select(page:Page):
    logging.info("Открываю страницу")
    page.goto(settings.SELECT_URL)
    title = page.title()
    logging.debug(f'Заголовок страницы {title}')
    
    page.get_by_label('Floating label select example').select_option(value="3")
    page.get_by_label("Floating label select example").select_option(index=0)
    page.get_by_label("Floating label select example").select_option(label="Предложил новую функцию")
    page.get_by_label("size 4 select example").select_option(value=["Playwright", "Python"])
    page.get_by_label("size 4 select example").select_option("Docker")
    assert "Select demo" in title

