#!/usr/bin/python3
import vk_api
import sys
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


def main():
    #group token with messages
    vk_session = vk_api.VkApi(token='8761eb63a4ab4a1537c2627461a11fbcdafbae6175894cb0ef95dded03a3e0f403e7cff97ac7982ce9cda')
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, 174628515) # group id

    trigger_1 = ['соси', "сос", "сОс", "Сос", "соС"]
    trigger_2 = ['иди нахуй', 'иди НАХУЙ', 'ИДИ НАХУЙ', 'ИДИ нахуй']

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            new = event.obj.text
            fuck = False
            cock = False
            for i in range(0, 4):
                if new.find(trigger_1[i]) != -1:
                    fuck = True
                    break
            for j in range(0,3):
                if new.find(trigger_2[j]) != -1:
                    cock = True
                    break
            is_group = False
            try:
                response = vk.users.get(user_ids=event.obj.from_id)
            except vk_api.exceptions.ApiError:
                is_group = True
                response = vk.groups.getById(group_id=event.obj.from_id)
            if is_group == True and response[0]['id'] == 174628515:
                if fuck == True:
                    fuck == False
                if cock == True:
                    cock == False
                is_group == False
            
            if new == 'превет':
                vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='здарова!')
            elif new == 'здарова':
                vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='превет')
            elif fuck == True:
                if is_group == True:
                    vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='Сам соси, ' + '@public' + str(response[0]['id']) + '(' + response[0]['name'] + ')')
                    continue
                vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='Сам соси, ' + '@id' + str(event.obj.from_id) + '(' + response[0]['first_name'] + ')')
            elif cock == True:
                if is_group == True:
                    vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='Сам иди НАХУЙ ' + '@public' + str(response[0]['id']) + '(' + response[0]['name'] + ')')
                    continue
                vk.messages.send(peer_id=event.obj.peer_id, user_id=event.obj.user_id, random_id=get_random_id(), message='Сам иди НАХУЙ ' + '@id' + str(event.obj.from_id) + '(' + response[0]['first_name'] + ')')
            

if __name__ == "__main__":
    main()