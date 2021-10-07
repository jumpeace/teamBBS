from team.models import Team
from channel.models import Channel

class props:
    list_ = {
        'body': {
            'bodyer': {
                'function_nav': {
                    'type': 'normal',
                    'links': [
                        # {
                        #     'type': 'team',
                        #     'url_name': 'team:detail',
                        #     'content': 'チーム概要',
                        # },
                        # {
                        #     'type': 'team',
                        #     'url_name': 'team:channel_create',
                        #     'content': 'チャンネル新規作成',
                        # },
                    ]
                }
            }
        }
    }


    create = {
        'body': {
            'bodyer': {
                'heading': 'チャンネル新規作成',
                'form_items': [
                    {
                        'type': 'text',
                        'name': 'name',
                        'placeholder': 'チャンネル名',
                        'autofocus': True,
                    },
                    {
                        'type': 'submit',
                        'name': 'team_channel_create',
                        'value': '作成',
                    },
                ],
                'links': [
                    {
                        'type': 'team',
                        'url_name': 'team:channel_list',
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
                    'type': 'normal',
                    'links': [
                    ]
                }
            }
        }
    }
