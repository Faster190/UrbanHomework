def custom_write(file_name, strings):
    dict_ = {}
    file = open(file_name, 'w', encoding="utf-8")
    ctr = 0
    for i in range(len(strings)):
        ctr += 1
        dict_[(ctr, file.tell())] = strings[i]
        file.write(f"{strings[i]}\n")
    file.close()
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
