import time
import os

def clock():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0) % 5 == 0:
            print('5 sec')
            time.sleep(1)

def query():
    for i in os.walk('/'):
        print(i[0])

def main():
    query()
    clock()

main()