'''
题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入
复制
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出
复制
1 0 1 0 0 2 1
'''

from collections import defaultdict

def isValid(ip, mask):
    ip = list(filter(None, ip.split('.')))
    mask = list(filter(None, mask.split('.')))

    # check ip address and mask length
    if len(ip) < 4 or len(mask) < 4:
        return False
    
    # check mask
    mask = list(map(int, mask))
    mask_str = ''.join('{:08b}'.format(i) for i in mask)
    if not '0' in mask_str or mask_str[0] != '1':
        return False
    end = 0
    for i in range(len(mask_str)):
        if mask_str[i] == '0':
            end = i - 1
            break
    if '1' in mask_str[end+1: ]:
        return False
    
    return True

def sort_ip(ip):
    fi = int(ip.split('.')[0])
    if 1 <= fi <= 126:
        return 'A'
    elif 128 <= fi <= 191:
        return 'B'
    elif 192 <= fi <= 223:
        return 'C'
    elif 224 <= fi <= 239:
        return 'D'
    elif 240 <= fi <= 255:
        return 'E'
    else:
        return 'N'

def isPrivate(ip):
    ip_li = ip.split('.')
    fi = int(ip_li[0])
    sec = int(ip_li[1])
    if fi == 10:
        return True
    elif fi == 172 and 16 <= sec <= 31:
        return True
    elif fi == 192 and sec == 168:
        return True
    return False
    



ips, masks = [], []
while True:
    inp = input()
    if not inp:
        break
    inp = inp.split('~')
    ips.append(inp[0])
    masks.append(inp[1])

table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'wrong': 5, 'private': 6, }
res = [0] * 7
for i in range(len(ips)):
    ip, mask = ips[i], masks[i]
    # if the ip or the mask is wrong
    if not isValid(ip, mask):
        res[table['wrong']] += 1
    else:
        if sort_ip(ip) == 'N':
            continue
        else:
            res[table[sort_ip(ip)]] += 1
            if isPrivate(ip):
                res[table['private']] += 1
print(' '.join(list(map(str, res))))









