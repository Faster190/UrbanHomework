import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, 'r')
    for line in file:
        all_data.append(line)


# start = datetime.datetime.now()
# for i in range(1, 5):
#     read_info(f"file {i}.txt")
# end = datetime.datetime.now()
# print(end - start, "линейный")

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, "мултипроцессорный")
