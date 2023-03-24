import requests
import schedule
import time


def send_message():

    resp = requests.post('https://textbelt.com/text', {
        'phone': '3375178879',
        'message': 'Hello world',
        'key': 'textbelt',
    })
    print(resp.json())


schedule.every().day.at('11:09').do(send_message)