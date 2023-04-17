import  random
def math():
    alist = []
    for i in range(9):
        a = random.randint(11,111)
        i = a
        alist.append(i)
    b = sum(alist)
    print(b,'所有随机数的和')
    print(alist,'所有的随机数 ')
math()


def list():
    a = [1, 2, 3, 4,]
    for i ,k in enumerate(a):
        a[i] = k+1
    print(a)
list()



def write():
    f= open("text.txt","w",encoding="utf-8")
    f.write('hello world\n hello python')
    f.close()


def list():
    h = ["张三", "张四", "张五", "王二"]
    for i in h:
        if i[0] == '张':
            h.remove(i)
    return h
print(list())

def fun15(b):
    return b










