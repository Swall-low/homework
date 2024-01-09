people = [
    {'first_name': 'Raj', 'last_name': 'Nayyar'},
    {'first_name': 'Suraj', 'last_name': 'Sharma'},
    {'first_name': 'Karan', 'last_name': 'Kumar'},
    {'first_name': 'Jade', 'last_name': 'Canary'},
    {'first_name': 'Raj', 'last_name': 'Thakur'},
    {'first_name': 'Raj', 'last_name': 'Sharma'},
    {'first_name': 'Kiran', 'last_name': 'Kamla'},
    {'first_name': 'Armaan', 'last_name': 'Kumar'},
    {'first_name': 'Jaya', 'last_name': 'Sharma'},
    {'first_name': 'Ingrid', 'last_name': 'Galore'},
    {'first_name': 'Jaya', 'last_name': 'Seth'},
    {'first_name': 'Armaan', 'last_name': 'Dadra'},
    {'first_name': 'Ingrid', 'last_name': 'Maverick'},
    {'first_name': 'Aahana', 'last_name': 'Arora'},
]
sorted_people = sorted(people, key=lambda x: (x['first_name'], x['last_name']))
for person in sorted_people:
      print(f"{person['first_name']} {person['last_name']}")
      