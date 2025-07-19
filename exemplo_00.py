from tinydb import TinyDB 

db = TinyDB('database.json')

result = db.insert(
    {'nome': 'Amir',
     'idade': 33,
     'hobbies': ['Ver live de Python', 'Codar'],
     'adm': False,
     }
)

print(result)