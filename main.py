from pathlib import Path
from domain import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def init():

    user1=User("fir","fer","foor,")
    user2 = User("fir", "fer", "foor,")
    user3 = User("fir", "fer", "foor,")

    contact1 = Contact(user1,34,1010)
    contact2=Contact(user2,89,202)
    contact3=Contact(user3,39,9090)

    user1.add(contact2,"Рабочая")
    user2.add(contact3,"Домашняя")
    user3.add(contact1,"Личная")

    user1.add_friend(user2)
    user2.add_friend(user3)
    user3.add_friend(user1)

    user1.share(user2,"Рабочая")
    user1.share(user3,"Рабочая")


def operation(x,y,operand=lambda x,y:x+y):
    return operand(x,y)
def print_hi(x):
    if type(x)==int:
        return x
    elif type(x)==str:
        return ord(x[0])
    else:
        return ord(x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''lst=[4,7,12,364,1514,'hello']
    lst2 = ['This', 'is', 'a', 'hello']
    lst3 = [-4,7,12,364,-1514]
    lst4=[[1,2,3],[1,0,7],[0,5,3]]
    lst.sort(key=print_hi)
    lst2.sort(key=len)
    lst3.sort(key=abs)
    lst4.sort(key=lambda x: x[0])
    r=operation(5,10,operand=lambda x,y:x*y)
    lst5=[x*x for x in range(10)]'''
    for file in Path("").iterdir():
        print(file)
    init()
    print(".")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
