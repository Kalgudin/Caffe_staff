[app]
# Название и домен (поменяйте под себя)
title = Cafe Stuff
package.name = cafe_stuff
package.domain = org.test

# Исходники
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения
version = 1.0

# ⚠️ КЛЮЧЕВАЯ СТРОКА: Фиксируем Python 3.13 для Android и Kivy 2.3.1
requirements = python3==3.13.9, hostpython3==3.13.9, kivy==2.3.1

# Настройки Android
android.api = 34
android.minapi = 21
android.ndk = 28c

# Разрешения (добавьте нужные, например INTERNET)
android.permissions = INTERNET

# Ориентация
orientation = portrait

# Отключаем лишние архитектуры для скорости (только arm64 для современных телефонов)
android.archs = arm64-v8a