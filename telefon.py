import codecs


def cop():
    fs = codecs.open('1.txt', 'r', encoding='utf-8')
    fn = codecs.open('tel.txt', 'a')
    for line in fs:
        fn.write(line.rstrip('\n'))
    fn.close()
    print(1)


fn = codecs.open('tel.txt', 'w')
with codecs.open('mag.txt', encoding='utf-8') as file:
    mag = file.read().splitlines()

dic = {}  # Создаем пустой словарь

for line in mag:  # Проходимся по каждой строчке
    key, value = line.split(': ')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
    dic.update({key: value})

#print(dic)

j = 0

while j <= len(dic):
    j += 1
    a = cop()

print(len(dic))
