translations = {
    'commands': {
        'answers': {
            'start': 'Добро пожаловать, {user_name}!\nЯ - *{bot_name}*. ' +
                     'Введи /help чтобы получить инструкцию',
            'help': {
                'admin': 'Форма записи: /help <команда>\nНапример: /help get\n\nСписок доступных команд:\n' +
                         '/get\n/get_with_trash\n/delete\n/restore\n/get_all_messages\n' +
                         '/get_all_messages_with_trash\n/left_messages_count\n/get_unread_messages',
                'user': 'Просто нажимай на кнопку:):):)',
                'commands': {
                    'get': 'Получить содержание выбранных сообщений\n\nФорма записи:\n' +
                           '/get <ID сообщения>\nНапример: /get 1\n\n' +
                           '/get <ID сообщения>, <ID сообщения>, ...\nНапример: /get 1, 2, 6, 9\n\n'
                           '/get <ID сообщения> - <ID сообщения>\nНапример: /get 3 - 100',
                    'get_with_trash': 'Получить содержание выбранных сообщений (включая удаленные)\n\nФорма записи:\n' +
                                      '/get_with_trash <ID сообщения>\nНапример: /get 1\n\n' +
                                      '/get_with_trash <ID сообщения>, <ID сообщения>, ...\n' +
                                      'Например: /get 1, 2, 6, 9\n\n/get_with_trash <ID сообщения> - <ID сообщения>\n'
                                      'Например: /get 3 - 100',
                    'delete': 'Удалить выбранные сообщения\n\nФорма записи:\n' +
                              '/delete <ID сообщения>\nНапример: /delete 1\n\n' +
                              '/delete <ID сообщения>, <ID сообщения>, ...\nНапример: /delete 1, 2, 6, 9\n\n'
                              '/delete <ID сообщения> - <ID сообщения>\nНапример: /delete 3 - 100',
                    'restore': 'Восстановить выбранные сообщения\n\nФорма записи:\n' +
                               '/restore <ID сообщения>\nНапример: /restore 1\n\n' +
                               '/restore <ID сообщения>, <ID сообщения>, ...\nНапример: /restore 1, 2, 6, 9\n\n'
                               '/restore <ID сообщения> - <ID сообщения>\nНапример: /restore 3 - 100',
                    'get_all_messages': 'Получить список загруженных сообщений\n\nФорма записи:\n/get_all_messages',
                    'get_all_messages_with_trash': 'Получить список загруженных и удаленных сообщений\n\n' +
                                                   'Форма записи:\n/get_all_messages_with_trash',
                    'left_messages_count': 'Получить кол-во непрочитанных сообщений пользователя\n\nФорма записи:\n' +
                                           '/left_messages_count <ID пользователя>\n' +
                                           'Например: /left_messages_count 123456789',
                    'get_unread_messages': 'Получить непрочитанные сообщения пользователя\n\nФорма записи:\n' +
                                           '/get_unread_messages <ID пользователя>\n' +
                                           'Например: /get_unread_messages 123456789',
                },
                'command-not-found': 'Такой команды нет, нажми /help чтобы посмотреть список доступных команд'
            },
            'role': {
                'root': 'Ты босс',
                'admin': 'Ты админ',
                'user': 'Ты пользователь, доступ закрыт((('
            }
        }
    },
    'answers': {
        'dont-understand': "Извини, я не понимаю, нажми /start или /help"
    },
    'keyboards': {
        'answers': {
        },
        'buttons': {
            'get-message': '🥺 Мне грустно 👉👈',
        }
    },
    'callbacks': {
        'answers': {
        },
        'keyboards': {
        }
    }
}
