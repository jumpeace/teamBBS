class props:

    register = {
        'body': {
            'bodyer': {
                'heading': '新規ユーザー登録',
                'form_items': [
                    {
                        'type': 'email',
                        'name': 'email',
                        'placeholder': 'メールアドレス',
                    },
                    {
                        'type': 'password',
                        'name': 'password1',
                        'placeholder': 'パスワード',
                    },
                    {
                        'type': 'password',
                        'name': 'password2',
                        'placeholder': 'パスワード（確認）',
                    },
                    {
                        'type': 'submit',
                        'name': 'register',
                        'value': '登録',
                    },
                ],
                'links': [
                    {
                        'to_url': 'user:login',
                        'content': 'ログインフォームへ',
                    },
                ],
            },
        },
    }


    login = {
        'body': {
            'bodyer': {
                'heading': 'ログイン',
                'form_items': [
                    {
                        'type': 'email',
                        'name': 'email',
                        'placeholder': 'メールアドレス',
                        'autofocus': True,
                    },
                    {
                        'type': 'password',
                        'name': 'password',
                        'placeholder': 'パスワード',
                    },
                    {
                        'type': 'submit',
                        'name': 'login',
                        'value': 'ログイン',
                    },
                ],
                'links': [
                    {
                        'to_url': 'user:register',
                        'content': '新規ユーザー登録フォームへ',
                    }
                ],
            },
        },
    }

    delete = {
        'body': {
            'bodyer': {
                'heading': 'ユーザー退会',
                'form_items': [
                    {
                        'type': 'password',
                        'name': 'password',
                        'placeholder': 'パスワード',
                    },
                    {
                        'type': 'submit',
                        'name': 'user_delete',
                        'value': '退会',
                    },
                ],
                'links': [
                    {
                        'to_url': 'index',
                        'content': 'キャンセル',
                    },
                ],
            },
        },
    }
