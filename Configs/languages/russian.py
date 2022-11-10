translations = {
    'commands': {
        'answers': {
            'start': 'Добро пожаловать, {user_name}!\nЯ - *{bot_name}*. ' +
            'Введи /help чтобы получить инструкцию',
            'help': '/get_all_messages - увидеть все загруженные сообщения\n' +
             '/get <число>, <число>, ... - получить выбранные сообщения\n' +
            '/delete <число>, <число>, ... - удалить выбранные сообщения',
            'settings': 'Выбери настройку',
            'role': {
                'root': 'Ты босс',
                'admin': 'Ты админ',
                'user': 'Ты пользователь, доступ закрыт((('
            }
        }
    },
    'answers': {
        'dont-understand': "Извините, я не понимаю, нажмите /start или /help"
    },
    'keyboards': {
        'answers': {
            'hello': 'Прив Привет',
            'joke': '<<Смешная шутка>>',
            'another-keyboard': 'Открываю другую клавиатуру',
            'write-to-dev': 'Введите ниже сообщение которое хотите отправить разработчикам',
            'wrote-to-dev': 'Сообщение отправлено разработчикам',
            'write-to-all-users': 'Введите ниже сообщение которое хотите отправить всем пользователям',
            'wrote-to-all-users': 'Сообщение отправлено всем пользователям',
            'message-from-user': 'Сообщение от пользователя [ <a href=\'https://t.me/{username}\'>' +
            '{username}</a> ]:\n\n{message}',
            'message-from-admin-to-all-users': 'Сообщение от админов:\n\n{message}',
        },
        'buttons': {
            'get-message': 'Получить сообщение',
            'hi': 'Приу',
            'joke': 'Шутка',
            'another-keyboard': 'Другая клавиатура',
            'write-to-dev': 'Написать разработчику📝',
            'write-to-all-users': 'Написать всем пользователям📝',
        }
    },
    'callbacks': {
        'answers': {
            'number-value': "Значение номера: {value}",
            'letter-value': "Значение буквы: {value}",
            'choose-language': 'Выбери язык',
            'language-updated-to': 'Язык обновлен на {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Язык'
            },
            'example': {
                '1': '1',
                '2': '2',
                '3': '3',
                'a': 'А',
                'b': 'Б',
                'c': 'В'
            }
        }
    }
}
