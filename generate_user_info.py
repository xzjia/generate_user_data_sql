# coding: utf-8

import random
import time, string
from gimei import Gimei

def count(start=1):
    n=start
    while True:
        yield n
        n +=1

def randomDate(start, end, format):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + random.random() * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomTel():
    prefix = random.choice(['080', '090', '03', '05'])
    return prefix + ''.join(random.choice(string.digits) for _ in range(8))

def main():
    OUTPUT_FILE = "TestData.sql"

    RECORD_COUNT = 1000
    START_FROM = 2000

    sqlCommands = ""

    for i in range(START_FROM, RECORD_COUNT+START_FROM):

        user_id = next(count(i))
        user_name = Gimei().name
        user_birthday = randomDate("1930-1-1", "2010-12-31", '%Y-%m-%d')
        user_addr = Gimei().address 
        user_tel = randomTel()
        updated_at = randomDate("2015-6-28 00:00:00", "2016-6-28 00:00:00", '%Y-%m-%d %H:%M:%S')
        user_roles = random.choice([1,2,3])
        user_status = random.choice(['INIT', 'ACTV', 'RMVD'])

        sqlCommands += "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', {});\n"\
                       .format(user_id, user_name, user_birthday, user_addr, user_tel, \
                                    user_status, updated_at, user_roles)

    with open(OUTPUT_FILE, "w") as f:
        f.write(sqlCommands)

if __name__ == '__main__':
    main()

