import time
import sys
import hashlib


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
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user
        # print(self.users,' - self.users - from init' )  # почему не выводит

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(self.current_user)


    def register(self, nickname, password, age):
        for user in self.users:
            # print(user.nickname)
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print('уже есть такой фильм')
                continue

    def get_videos(self, search_word):
        finded_film = []
        word = search_word.lower()
        for i in self.videos:
            name_film = i.title.lower()
            if word in name_film:
                finded_film.append(name_film)
        return finded_film

    def watch_video(self, name_film):
        for i in self.videos:
            # print(i.title, name_film)
            if name_film == i.title:
                # print(i.title, ' - Нашел! Время пошло: ')
                total_seconds = 0
                film_duration = i.duration
                while total_seconds < film_duration:
                    time.sleep(1)  # Приостанавливаем выполнение программы на 1 секунду
                    total_seconds += 1
                    sys.stdout.write(f"\rПрошло {total_seconds} секунд из {film_duration} секунд")
                    sys.stdout.flush()
                else:
                    total_seconds = 0
                    print(total_seconds)
                print(f"{total_seconds} секунд")


# создаем фильмы
film1 = Video('urban', 120)
film2 = Video('The best forest', 10)
film3 = Video('The forest', 50)
film4 = Video('The river', 90)

# создаем объекта класса User
user1 = User('Den', 5, 19)
user3 = User('Nick', 9, 55)

# создаем объект класса UrTube
j = UrTube([user1, user3], [film2, film3, film1])

j.register('Jonn', 7, 45)
# print(j.users)
j.add(film4)
# for i in j.videos:
#     print(i.title, i.duration)
# print(j.get_videos('urban'))
# print(j.get_videos('forest'))
# j.watch_video('The best forest')
j.log_in('Den', 5)
