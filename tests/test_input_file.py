from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect

from config import settings 
import logging

def test_input_file(page: Page):
    logging.info("Открываем страницу")
    page.goto(settings.INPUT_FILE_URL)
    title = page.title()
    logging.debug(f'Заголовок страницы {title}')
    page.on('filechooser', lambda file_chooser: file_chooser.set_files("/home/hama/Документы/PythonTests/playwright_project_1/data/testFile.txt"))
    assert "Upload demo" in title
