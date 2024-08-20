def all_variants(text):
    length = len(text)
    step = 1
    for j in range(length):
        for k in range(length-j):
            word = ''
            ptr = k
            for z in range(step):
                word += text[ptr+z]
            yield word
        step += 1
        print('')


a = all_variants("abcdef")
for i in a:
    print(i, end=' ')
