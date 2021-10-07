class props:
    list_ = {
        'body': {
            'bodyer': {
                'function_nav': {
                    'type': 'normal',
                    'links': [
                        {
                            'type': 'normal',
                            'url_name': 'team:create',
                            'content': 'チーム新規作成',
                        },
                    ]
                }
            }
        }
    }

    create = {
        'body': {
            'bodyer': {
                'heading': 'チーム新規作成',
                'form_items': [
                    {
                        'type': 'text',
                        'name': 'name',
                        'placeholder': 'チーム名',
                        'autofocus': True,
                    },
                    {
                        'type': 'submit',
                        'name': 'team_create',
                        'value': '作成',
                    },
                ],
                'links': [
                    {
                        'type': 'normal',
                        'url_name': 'team:list',
                        'content': 'キャンセル',
                    }
                ],
            },
        },
    }

    detail = {
        'body': {
            'bodyer': {
                'function_nav': {
                    'type': 'owner_judge',
                    'links': {
                        'normal': [
                            # {
                            #     'type': 'normal',
                            #     'url_name': 'team:list',
                            #     'content': 'チーム一覧',
                            # },
                            # {
                            #     'type': 'team',
                            #     'url_name': 'team:channel_list',
                            #     'content': 'チャンネル一覧',
                            # },
                        ],
                        'owner': [
                            # {
                            #     'type': 'team',
                            #     'url_name': 'team:owner_delete',
                            #     'content': 'チーム脱退',
                            # },
                            # {
                            #     'type': 'team',
                            #     'url_name': 'team:delete',
                            #     'content': 'チーム削除',
                            # },
                            # {
                            #     'type': 'team',
                            #     'url_name': 'team:owner_move_authority',
                            #     'content': 'オーナー権限移動',
                            # },
                        ],
                        'not_owner': [
                            # {
                            #     'type': 'team',
                            #     'url_name': 'team:user_delete',
                            #     'content': 'チーム脱退',
                            # },
                        ],
                    }
                }
            }
        }
    }

    class user:
        list_ = {
            'body': {
                'bodyer': {
                    'function_nav': {
                        'type': 'normal',
                        'links': [
                            # {
                            #     'type': 'normal',
                            #     'url_name': 'team:create',
                            #     'content': 'チーム新規作成',
                            # },
                        ]
                    }
                }
            }
        }

        create = {
            'body': {
                'bodyer': {
                    'heading': 'チーム参加',
                    'form_items': [
                        {
                            'type': 'number',
                            'name': 'team',
                            'placeholder': 'チームID',
                            'autofocus': True,
                        },
                        {
                            'type': 'submit',
                            'name': 'user_team_create',
                            'value': '参加',
                        },
                    ],
                    'links': [
                        {
                            'type': 'normal',
                            'url_name': 'team:list',
                            'content': 'キャンセル',
                        }
                    ],
                },
            },
        }
