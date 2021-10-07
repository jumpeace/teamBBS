from django.shortcuts import render
from django.contrib.auth.hashers import check_password
        
def add_default_context(context, self, props):
    context.update({
        'url': self.request.path,
        'props': props,
        'kwargs': self.kwargs,
    })
    return context
