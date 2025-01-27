print("hello word")

def gato():
    print("miau")

for i in range(1,5):
    print(i)

gato()

def ordenarLista(a):
    a = {2,3,4,5}
    for i in a:
        if (a[0] > a[1]):
            a[0], a[1] = a[1], a[0]
        