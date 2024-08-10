class User:
    users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        users = self.users.append(self)
        # print(users)

    # print(users)  # почему сразу выводит пустой список, если я не создаю экземпляр класса?


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = [{'name':222}, {'dd':5}]
        self.videos = []
        self.current_user = None
        # print(self.users,' - self.users - from init' )  # почему не выводит

    def log_in(self, nickname, password): # метод работает корректно!
        for user in self.users:
            if nickname in user and user[nickname] == password:
                self.current_user = user
                print(self.current_user, ' - пользователь существует, может залогиниться')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user



s = User('name', 222, 30)
# print(s)
h = UrTube()
h.log_in('name', 222)
# h.register('name', 222, 30)
j = UrTube()
j.log_in('dd', 5)
