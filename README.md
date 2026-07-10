# 1. Перейдите в папку с проектом
cd ~/h_parser

# 2. Инициализируйте Git-репозиторий
git init

# 3. Добавьте все файлы
git add .

# 4. Сделайте первый коммит
git commit -m "Первый коммит: парсер вакансий с Habr Career"

# 5. Привяжите локальный репозиторий к удалённому на GitHub
# (Замените USERNAME на ваше имя пользователя, REPO на название репозитория)
git remote add origin https://github.com/USERNAME/hh-parser.git

# 6. Отправьте код на GitHub
git push -u origin main
