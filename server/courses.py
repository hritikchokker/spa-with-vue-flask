import uuid

COURSES = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript ',
        'author': 'David Herman',
        'paperback': True,
        'price': '46.99'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'JavaScript: The Good Parts',
        'author': 'Douglas Crockford',
        'paperback': False,
        'price': '29.23'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Eloquent JavaScript: A Modern Introduction to Programming',
        'author': 'Marijn Haverbeke',
        'paperback': True,
        'price': '26.23'
    }
]
