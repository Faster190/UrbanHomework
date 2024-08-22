from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    file = open(file_name, 'w', encoding="utf-8")
    for i in range(word_count):
        file.write(f"Какое-то слово № {i + 1}\n")
        sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_end = datetime.now()
res = time_end - time_start
print(f"Работа функций {res}")

time_start = datetime.now()

file_5 = Thread(target=wite_words, args=(10, "example5.txt"))
file_6 = Thread(target=wite_words, args=(30, "example6.txt"))
file_7 = Thread(target=wite_words, args=(200, "example7.txt"))
file_8 = Thread(target=wite_words, args=(100, "example8.txt"))

file_5.start()
file_6.start()
file_7.start()
file_8.start()

file_5.join()
file_6.join()
file_7.join()
file_8.join()

time_end = datetime.now()
res = time_end - time_start
print(f"Работа потоков {res}")
