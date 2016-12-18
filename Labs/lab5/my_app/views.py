from django.shortcuts import render


def index(request):
    data = {
        'flight_list': [
            {'info': 'Рейс 14/88. Москва-Бишкек 99999 руб.', 'id': 6677},
            {'info': 'Рейс 14/89. Москва-Казань 99099 руб.', 'id': 6097},
            {'info': 'Рейс 14/88. Москва-Бишкек 99999 руб.', 'id': 6570}
        ]
    }
    return render(request, 'objects_list.html', data)

def flight(request, id):
    data = {
        'flight': {
            'id': id
        }
    }
    return render(request,'object.html', data)