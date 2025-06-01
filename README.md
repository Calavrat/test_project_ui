# Playwright Python Project

### Активация виртуальной среды
cd /home/hama/Документы/playwright_project_1/venv
source playwright_project_1_env/bin/activate
### Деактивация виртуальной среды
deactivate

### Если ты установил библиотеки в виртуальном окружении, можно сохранить текущие зависимости командой:
pip freeze > requirements.txt 

## Если ты используешь VS Code, он может смотреть на системный Python, а не на твой venv.
Открой Command Palette: Ctrl+Shift+P → "Python: Select Interpreter"
Выбери путь к своему окружению (должно быть что-то вроде ./venv/bin/python или .\venv\Scripts\python.exe)
!!!Перезапусти VSCode

PWDEBUG=1 pytest -s test_drag_drop.py
pytest --tracing=retain-on-failure
playwright show-trace path/trace.zip
playwright codegen https://zimaev.github.io/pom/
allure serve /home/hama/Документы/PythonTests/playwright_project_1/reports
# Если в vsCode при формировании отчета возникнет ошибка symbol lookup error: /snap/core20/current/lib/x86_64-linux-gnu/libpthread.so.0: undefined symbol: __libc_pthread_init, version GLIBC_PRIVATE
# Используй это  unset GTK_PATH , в терминале введи и все 
Для allure нужно скачать brew и сам allure
brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
allure: brew install allure


