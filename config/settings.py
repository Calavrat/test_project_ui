import os
from dotenv import load_dotenv

load_dotenv()

CHECKBOX_URL = os.getenv("BASE_URL", "https://zimaev.github.io/checks-radios/")
SELECT_URL = os.getenv("SELECT_URL", "https://zimaev.github.io/select/")
DRAG_DROP_URL = os.getenv("DRAG_DROP_URL", "https://zimaev.github.io/draganddrop/")
DIALOG_URL = os.getenv("DIALOG_URL", "https://zimaev.github.io/dialog/") 
INPUT_FILE_URL = os.getenv("INPUT_FILE_URL", "https://zimaev.github.io/upload/")
TABS_URL = os.getenv("TABS_URL", "https://zimaev.github.io/tabs/")
TODO_URL = os.getenv('TODO_URL','https://demo.playwright.dev/todomvc/#/')
LISTEN_NETWORK_URL =os.getenv('LISTEN_NETWORK_URL', 'https://osinit.com/#home') 
NETWORK_URL=os.getenv('NETWORK_URL', 'https://reqres.in/')
LOGIN_URL=os.getenv('LOGIN_URL', 'https://zimaev.github.io/pom/') 
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
