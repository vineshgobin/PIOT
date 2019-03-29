import requests

class pushbulletMessage:
    def push_note(self, title, message):
        url = 'https://api.pushbullet.com/v2/pushes'
        headers = { 'Access-Token': 'o.3BURPKcWSiMAJlQpFzw0EwxS7A5fWk7P' }
        data = {'title': title, 'body': message, 'type': 'note'}
        r = requests.post(url, data=data, headers=headers).json()
        print('Pushed: '+ message)