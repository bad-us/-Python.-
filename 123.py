import codecs


def cop():
    fs = codecs.open('1.txt', 'r', encoding='utf-8')
    fn = codecs.open('tel.txt', 'a')
    for line in fs:
        fn.write(line.rstrip('\n'))
    fn.close()
    print(1)


# fs = codecs.open('1.txt', 'r', encoding='utf-8')
fn = codecs.open('tel.txt', 'w')
with codecs.open('mag.txt', encoding='utf-8') as file:
    mag = file.read().splitlines()

dic = {}  # Создаем пустой словарь

for i in file:
    key, value = i.strip(), split(': ')
    dic[key] = value
print(dic)

j = 0

# fn = codecs.open('tel.txt', 'a')

while j <= len(dic):
    j += 1
    a = cop()

print(len(dic))
# print(dic)
# print((dic1), end='\n')


'''for j in dic:
    rep = {'400': j, '132': dic[j]}
    for line in fs:
        out.write(line)
        #for i in rep.keys():
           #line.replace(i, rep[i])
           #print(i)
        #print(line)'''

'''for line in fs:
    for j in dic:
        rep = {'400': j, '132': dic[j]}
        for i in rep.keys():
            fs = fs.replace(i, rep[i])
            print(fs)
    out.write(fs)'''
'''for j in dic:
    rep = {'400': j, '132': dic[j]}
    for i in rep.keys():
        fs = fs.replace(i, rep[i])
        for line in fs:
            print((line),end='')
        out.write(fs)'''
