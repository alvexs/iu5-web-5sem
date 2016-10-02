from base_client import BaseClient
from collections import Counter
from datetime import date, datetime
import requests


class MyClient(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    user_id = None
    user_friends = None

    def _get_data(self, method, http_method):
        return requests.get(self.generate_url(method))

    def __init__(self, user_name):
        self.user_id = self._get_id(user_name)
        self.user_friends = self._get_friends(self.user_id)

    def _get_id(self, user_name):
        self.method = 'users.get?user_ids=' + str(user_name) + '&v=5.57'
        user_id = self.get_json(self.execute())
        user_id = user_id['response']
        user_id = user_id[0].get('id')
        return user_id

    def _get_friends(self, user_id):
        self.method = 'friends.get?user_id=' + str(user_id) + '&fields=bdate&v=5.57'
        user_friends = self.get_json(self.execute())
        user_friends = user_friends['response']
        user_friends = user_friends['items']
        return user_friends

    def _get_age(self, friend_bdate):
        day = int(friend_bdate[0])
        month = int(friend_bdate[1])
        year = int(friend_bdate[2])
        bdate = date(year, month, day)
        today = date.today()
        age = today.year - bdate.year
        if today.month < bdate.month:
            age -= 1
        elif today.month == bdate.month and today.day < bdate.day:
            age -= 1
        return age

    def get_age_list(self):
        user_age_list = []
        for friend in self.user_friends:
            if friend.get('bdate'):
                bdate = friend['bdate'].split('.')
                if len(bdate) == 3:
                    age = self._get_age(bdate)
                    user_age_list.append(age)
        user_age_list = Counter(user_age_list)
        return user_age_list

user_name = input()
obj = MyClient(user_name)
age_list = obj.get_age_list()
keys = age_list.keys()
keys = list(keys)
keys.sort()
for i in keys:
    print(i, ':', '#' * age_list[i])
