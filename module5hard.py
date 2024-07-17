import time

class UrTube:
    def __init__(self):
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None

    def log_in(self, nickname, password):
        if len(self.users) == 0:
            print("Нет пользователя с таким ником")
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                if self.users[i].password == hash(password):
                    self.current_user = nickname
                    print("Успешный вход!")
                else:
                    print("Неверный пароль")
            else:
                print("Нет пользователя с таким ником")

    def register(self, nickname, password, age):
        verify = True
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                verify = False
                break
        if verify:
            ob = User(nickname, password, age)
            self.users.append(ob)
            self.current_user = nickname
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in range(len(args)):
            verify = True
            for k in range(len(self.videos)):
                if args[i].title == self.videos[k].title:
                    verify = False
                    # print(self.videos[k].title, "- уже существует!")
                    break
            if verify:
                self.videos.append(args[i])
                # print(args[i].title, "- добавлен")

    def get_videos(self, s):
        string = s.lower()
        list_ = []
        for i in range(len(self.videos)):
            title = self.videos[i].title.lower()
            for k in range(len(title)):
                if title[k] == string[0]:
                    verify = True
                    for j in range(len(string)):
                        if title[k + j] != string[j]:
                            verify = False
                            break
                    if verify:
                        list_.append(self.videos[i].title)
                        break
        return list_

    def watch_video(self, name):
        if self.current_user is not None:
            age = 0
            for i in range(len(self.users)):
                if self.users[i].nickname == self.current_user:
                    age = self.users[i].age
                    break
            for i in range(len(self.videos)):
                if name == self.videos[i].title:
                    if self.videos[i].adult_mode is False or age >= 18:
                        for j in range(self.videos[i].time_now, self.videos[i].duration + 1):
                            time.sleep(1)
                            print(j, end=' ')
                            self.videos[i].time_now += 1
                        self.videos[i].time_now = 0
                        print("Конец видео")
                        break
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nick, password, age):
        self.nickname = nick
        self.age = int(age)
        self.password = hash(password)


if __name__ == "__main__":
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
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
