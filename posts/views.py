from django.shortcuts import render

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'Picture from Nietzy',
        'user': {
            'name': 'Nietzy Cardoza',
            'picture': 'https://i.picsum.photos/id/404/60/60.jpg?hmac=lwzhD_dCmmfxmIzRzpe6zlpqaTDqkWYTB5WY--m-u6k'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Crecencio',
        'user': {
            'name': 'Crecencio Gameros',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Brenda',
        'user': {
            'name': 'Brenda Gutierrez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Luis',
        'user': {
            'name': 'Luis Hernandez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    },
    {
        'title': 'Picture from Vianey',
        'user': {
            'name': 'Vianey Lopez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/300/300',
    }
]


def list_post(request):
    return render(request,'feed.html',{'posts': posts})