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
