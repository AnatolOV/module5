# Пишем код сюда
import time
import sys
import hashlib


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Фильм - {self.title}, продолжительность={self.duration}, для взрослых={self.adult_mode}"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):

        for user in self.users:
            if user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                print(self.current_user.nickname, ' - этот пользователь залогинился')
                return
        print('Введено неверное имя пользователя или пароль')
        return False

    def register(self, nickname, password, age):
        # print(nickname, password, age)
        for user in self.users:
            # print(user.nickname)

            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        # print(new_user)
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
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in self.videos:
            if name_film == i.title:
                if (i.adult_mode and self.current_user.age >= 18) or (i.adult_mode == False):
                    total_seconds = 0
                    film_duration = i.duration
                    while total_seconds < film_duration:
                        time.sleep(1) # Приостанавливаем выполнение программы на 1 секунду
                        total_seconds += 1
                        sys.stdout.write(f"\rПрошло {total_seconds} секунд из {film_duration} секунд")
                        sys.stdout.flush()
                    else:
                        total_seconds = 0
                        print("\nКонец видео")
                    # print(f"{total_seconds} секунд")
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')