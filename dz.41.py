from jinja2 import Environment, FileSystemLoader

city = ['Адлер', 'Сочи', 'Грузия', 'Абхазия', 'Геленджик', 'Анапа', 'Кабардино‑Балкария', 'Кармадон', 'Нальчик', 'Светлогорск']

file_loader = FileSystemLoader('templates1')
env = Environment(loader=file_loader)

tm = env.get_template("page.html")
msg = tm.render(cities=city, title="Домашнее задание")

print(msg)