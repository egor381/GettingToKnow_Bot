hobbies = [
    {
        'name': 'Имя',
        'value': 'Чебурашка'
    },
    {
        'name': 'Фамилия',
        'value': 'отсутствует'
    },
    {
        'name': 'Возраст',
        'value': 'не определен'
    },
    {
        'name': 'Характер',
        'value': 'забавный, трогательный и доверчивый'
    },
    {
        'name': 'Внешность',
        'value': 'пушистый зверёк, добрые глаза, коричневая шерсть, огромные круглые уши, '
                 'каждое из которых размером с голову этого чудного существа, может быть едет в любую одежду'
    },
    {
        'name': 'Хобби',
        'value': 'Любит петь песни'
    },
    {
        'name': 'Любимая еда',
        'value': 'Мандарины 🍊'
    },
]


def hobbies_to_string():
    result = ''
    for item in hobbies:
        result += f"*{item['name']}*: {item['value']}\n"
    return result


def get_photo():
    return open('cheburashka.jpg', 'rb')
