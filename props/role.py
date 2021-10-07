class props:
    list_ =  {
        'bodyer': {
            'function_nav': {
                'type': 'normal',
                'links': [
                ]
            }
        }
    }

    create = {
        'body' : {
            'bodyer': {
                'heading': 'チーム役職新規作成',
                'form_items': [
                    {
                        'type': 'text',
                        'name': 'name',
                        'placeholder': '役職名',
                        'autofocus': True,
                    },
                    {
                        'type': 'submit',
                        'name': 'team_role_create',
                        'value': '作成',
                    },
                ],
                'links': [
                    # {
                    #     'type': 'normal',
                    #     'url_name': 'team:role:list',
                    #     'content': 'キャンセル',
                    # }
                ],
            },
        }
    }

    detail = {
        'bodyer': {
            'function_nav': {
                'type': 'normal',
                'links': [
                ]
            }
        }
    }

    class user:
        list_ =  {
            'bodyer': {
                'function_nav': {
                    'type': 'normal',
                    'links': [
                    ]
                }
            }
        }
