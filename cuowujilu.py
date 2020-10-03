from collections import defaultdict

dic = defaultdict(int)
res = []

while True:
    try:
        s = input()
        if s == '': break
        s = s.split(' ')
        fn = s[0].split('\\')[-1][-16:]
        ln = s[-1]
        dic[fn+ln] += 1
        res.append([fn, ln, str(dic[fn+ln])])
    except:
        break

for i in res[-8:]:
    print(' '.join(i))
