Из директории с проектом:
1. Создание виртуального окружения: 
    - Windows: python.exe -m venv venv
    - Linux: python -m venv venv
2. Активация виртуального окружения: 
    - Windows: .\venv\Scripts\Activate.ps1
    - Linux: source/bin/activate
3. Установка в режиме разработки:
    - Windows: python.exe setup.py develop
    - Linux: python setup.py develop
4. Положить вебдрайвер в директорию проекта
5. Запуск тестов:
    - Windows: pytest.exe src\autotests\tests
    - Linux: pytest src/autotests/tests
