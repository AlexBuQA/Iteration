# MEPHI RL26 — Домашнее задание №1

**Автор:** Alexandra Bujor  
**Тема:** Value Iteration и Policy Iteration

Готовый и выполненный ноутбук с реализацией:

- Value Iteration и извлечения оптимальной политики для Grid World;
- Policy Evaluation, Policy Improvement и общего цикла Policy Iteration;
- Policy Iteration для детерминированной и стохастической версий Frozen Lake;
- визуализации функций ценности и оптимальных политик.

Все встроенные `assert`-проверки заданий 1–3 пройдены. В итоговом ноутбуке сохранены результаты выполнения и 6 графиков.

## Состав проекта

- `MEPHI_RL26_hw1_VI_PI_Bujor_Alexandra.ipynb` — готовый ноутбук;
- `validate_notebook.py` — последовательный запуск всего ноутбука и проверка результатов;
- `requirements.txt` — зависимости Python;
- `.vscode/` — рекомендуемые расширения и настройки VS Code;
- `.github/workflows/validate.yml` — автоматическая проверка на GitHub.

## Локальный запуск в VS Code (Windows)

Требуется Python 3.12 или новее и VS Code. Проект проверен на Python 3.12.16 и 3.13.6; GitHub Actions использует Python 3.12. Откройте папку проекта в VS Code и примите рекомендуемые расширения **Python** и **Jupyter**.

В терминале PowerShell выполните:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Откройте `MEPHI_RL26_hw1_VI_PI_Bujor_Alexandra.ipynb`, выберите интерпретатор `.venv` в правом верхнем углу ноутбука и нажмите **Run All**.

Если PowerShell запрещает активацию окружения, установку и проверку можно выполнить без активации:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe validate_notebook.py
```

## Автоматическая проверка

После активации окружения выполните:

```powershell
python validate_notebook.py
```

Скрипт заново выполняет все ячейки, останавливается при любой ошибке, проверяет сообщения встроенных тестов и сохраняет выводы и графики в ноутбуке. Успешное завершение заканчивается сообщением:

```text
OK: MEPHI_RL26_hw1_VI_PI_Bujor_Alexandra.ipynb
Все встроенные assert-проверки заданий 1–3 пройдены.
```

## Загрузка на GitHub

Создайте пустой репозиторий на GitHub без README, затем выполните в папке проекта:

```powershell
git init
git add .
git commit -m "Complete Value Iteration and Policy Iteration homework"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPOSITORY>.git
git push -u origin main
```

Замените `<USERNAME>` и `<REPOSITORY>` на свои значения. После отправки на вкладке **Actions** автоматически запустится та же проверка ноутбука.

Для сдачи через Colab загрузите готовый `.ipynb`, при необходимости выполните все ячейки ещё раз и откройте доступ по ссылке в режиме читателя.
