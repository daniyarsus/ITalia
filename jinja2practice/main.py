from jinja2 import Template

cities = [{'id': 1, 'city': 'Almaty'},
          {'id': 2, 'city': 'Bishkek'},
          {'id': 3, 'city': 'Minsk'}]

link = '''<select name = "cities">

{% for i in cities %}
    <option vale = "{{i['id']}}">{{i['city']}}</option>
{% endfor %}

</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)