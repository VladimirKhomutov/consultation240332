import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import acces_token, comunity_token



class BotInterface: 

    def __init__(self, token):
        self.bot = vk_api.VkApi(token=token)


    def message_send(self, user_id, message=None, attachment=None):
        self.bot.method('messages.send',
                        {'user_id': user_id,
                         'message': message,
                         'random_id': get_random_id(),
                         'attachment': attachment
                        }
                        )
        

    def handler(self):
        longpull = VkLongPoll(self.bot)
        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me: 
                if event.text.lower() == 'привет':
                    self.message_send(event.user_id, 'Добрый день')
                elif event.text.lower() == 'поиск':    
                    pass
                elif event.text.lower() == 'далее':    
                    pass        
                else: 
                    self.message_send(event.user_id, 'неизвестная команда')

                
if __name__ == '__main__':
    bot = BotInterface(comunity_token) 
    bot.handler()
    # media = 'photo709972942_457239017}'
    # bot.message_send(789657038, 'фото', attachment=media)





