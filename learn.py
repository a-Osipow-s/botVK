import time
import vk_api

class VK_User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def auth_bot(self):
        vk_session = vk_api.VkApi(self.login, self.password)
        vk_session.auth()

        return vk_session

    def send_mess(self, id, message, random_id, vk):
        vk.method('messages.send', {'user_id': id, 'random_id': random_id, 'message': message})



random_id = 3
message = ""
Anton = VK_User("375336615148", "3034850Minsk")
Anton.send_mess(262223951, message, random_id, Anton.auth_bot())