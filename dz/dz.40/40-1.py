from jinja2 import Template

num = [
    {'href': '/index', 'text': 'Главная'},
    {'href': '/news', 'text': 'Новости'},
    {'href': '/about', 'text': 'О компании'},
    {'href': '/shop', 'text': 'Магазин'},
    {'href': '/contacts', 'text': 'Контакты'},
]

link = """<ul>
{% for s in num -%}
{% if s.text == 'Главная' -%}
    <li><a href="{{ s['href'] }}" class="active">{{ s['text'] }}</a></li>
{% else -%}
    <li><a href="{{ s['href'] }}">{{ s['text'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(num=num)

print(msg)