import time
from functools import  lru_cache

@lru_cache(maxsize=10)
def somework(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("printing somework")
    somework(3)
    somework(2)
    somework(1)
    somework(5)
    print("done, calling again")
    somework(5) #turant return tabhi hoga jab usko koi same value dikhegi(jo upper sleep likhe hai unme se).

    # somework(4) #isme computer 4 seconds ka lag lega called again print krne se phle kyuki 4 seconds ka func phle call nhi hua hai
    # kabhi
    print("called again")
    