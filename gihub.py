from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import datetime
import random
import time
import calendar
import mysql.connector
import pytz

token ='9a1ded9efde06e828a4c2f3376cb969f6c939448bf45f35f757bf225f5b8ff4e839f305b0eecb170dd85b'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response=event.text.lower()
            if  event.from_user and not event.from_me:
                if response=="начать":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Вы еще не зарегистрированы!', 'random_id': 0})
                    
