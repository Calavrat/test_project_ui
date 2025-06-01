from playwright.sync_api import Page 
from playwright.sync_api import Playwright, sync_playwright, expect
from config import settings 
import logging

def test_todo(page:Page, browser_name):
    logging.debug("Проверка то что открыт конкретный URL")
    page.goto(settings.TODO_URL)
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")

    logging.debug("Проверка нахождения поля ввода и проверить то что оно пустое")
    input_field = page.get_by_placeholder("What needs to be done?")
    expect(input_field).to_be_empty()
    
    logging.debug("Проверка ввода задачи №1")
    input_field.fill("Задача №1")
    input_field.press('Enter')
    
    logging.debug("Проверка ввода задачи №2")
    input_field.fill("Задача №2")
    input_field.press('Enter')
    
    logging.debug("Проверка количества задач, в сумме должно быть 2")
    todo_item = page.get_by_test_id("todo-item")
    expect(todo_item).to_have_count(2)
    logging.debug("Проверка отмечина ли одна из задач выполненной")
    logging.debug("Проверка то что эта задача отмечена выполненной")
    todo_item.get_by_role('checkbox').nth(0).check()
    expect(todo_item.nth(0)).to_have_class('completed')
