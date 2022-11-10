translations = {
    'commands': {
        'answers': {
            'start': 'Welcome, {user_name}!\nI am - *{bot_name}*, i will help you to get notifications from rocket. ' +
            'Press /help to get an instruction',
            'help': '/help command',
            'settings': 'Choose a setting',
            'role': {
                'root': "You'r a boss!",
                'admin': "You'r an admin!",
                'user': "You'r an usual user, access denied((("
            }
        }
    },
    'answers': {
        'dont-understand': "Sorry, i don't understand, type /start or /help"
    },
    'keyboards': {
        'answers': {
            'hello': 'Hi Hello',
            'joke': '<<Funny Joke>>',
            'another-keyboard': 'Open another keyboard',
            'write-to-dev': 'Enter below the message you want to send to the developers',
            'wrote-to-dev': 'Message sent to developers',
            'write-to-all-users': 'Enter below the message you want to send to all users',
            'wrote-to-all-users': 'Message sent to all users',
            'message-from-user': 'Message from user [ <a href=\'https://t.me/{username}\'>' +
            '{username}</a> ]:\n\n{message}',
            'message-from-admin-to-all-users': 'Message from admins:\n\n{message}',
        },
        'buttons': {
            'hi': 'Hi',
            'joke': 'Joke',
            'another-keyboard': 'Another keyboard',
            'write-to-dev': 'Write to the developer📝',
            'write-to-all-users': 'Write to all users📝',
        }
    },
    'callbacks': {
        'answers': {
            'number-value': "Number value: {value}",
            'letter-value': "Letter value: {value}",
            'choose-language': 'Choose language',
            'language-updated-to': 'Language updated to {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Language'
            },
            'example': {
                '1': '1',
                '2': '2',
                '3': '3',
                'a': 'A',
                'b': 'B',
                'c': 'C'
            }
        }
    }
}
