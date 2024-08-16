# Пишем код сюда
import time
import sys
import hashlib


class User:
    users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        # print(self.password)
        self.age = age
        User.users.append(self)  # Обращение к списку класса User
        # print(User.users)
    def __repr__(self):
        return f"Пользователь - {self.nickname}, пароль: {self.password}, возраст: {self.age}"

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Фильм - {self.title}, продолжительность={self.duration}, для взрослых={self.adult_mode}"

class UrTube:
    def __init__(self, users=None, videos=[], current_user=None):
        self.users = [users]
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        # print(self.users)
        for user in self.users:
            if user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                print(self.current_user.nickname, ' - этот пользователь залогинился')
                return
        print('Введено неверное имя пользователя или пароль')
        return False

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
        if self.current_user == None:
            print('Нужно залогиниться')
            return
        else:
            print(self.current_user.age)
        for i in self.videos:
            print(i.adult_mode, name_film)
            if name_film == i.title:
                if (i.adult_mode and self.current_user.age >= 18) or (i.adult_mode == False):
                    total_seconds = 0
                    film_duration = i.duration
                    while total_seconds < film_duration:
                        time.sleep(1)  # Приостанавливаем выполнение программы на 1 секунду
                        total_seconds += 1
                        sys.stdout.write(f"\rПрошло {total_seconds} секунд из {film_duration} секунд")
                        sys.stdout.flush()
                    else:
                        total_seconds = 0
                        print("\nКонец видео")
                    print(f"{total_seconds} секунд")


# создаем фильмы
film1 = Video('urban', 120)
film2 = Video('The best forest', 10, adult_mode=True)
film3 = Video('The forest', 50)
film4 = Video('The river', 90)
# print(repr(film1))
# создаем объекта класса User
user1 = User('Den', 'password123', 25)
user3 = User('Nick', 'password45', 55)
# print(repr(user1))
# создаем объект класса UrTube
j = UrTube(user1)
j.add(film2)

# print(j.get_videos('k'))

# j.register('Jonn', 'password67', 45)
# print(j.users)
# j.add(film4)

j.log_in('Den', 'password123', )
# j.log_out()

j.watch_video('The best forest')
