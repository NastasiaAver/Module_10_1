from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_1 = datetime.now()
time_1 = time_end_1 - time_start_1
print(time_1)

time_start_2 = datetime.now()
example5 = Thread(target=write_words, args=(10, "example5.txt"))
example6 = Thread(target=write_words, args=(30, "example6.txt"))
example7 = Thread(target=write_words, args=(200, "example7.txt"))
example8 = Thread(target=write_words, args=(100, "example8.txt"))

example5.start()
example6.start()
example7.start()
example8.start()

example5.join()
example6.join()
example7.join()
example8.join()
time_end_2 = datetime.now()
time_2 = time_end_2 - time_start_2
print(time_2)
