# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:24:45 2017

@author: dzhao
"""

import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'zhaowj1001',
    db = 'pymysql')

try:
    with conn.cursor() as cursor:
        cursor.execute(
                "CREATE TABLE IF NOT EXISTS active_code(code varchar(30));")
        with open('C:/Users/赵伟健/OneDrive/Python/Python 练习册/Running_result.txt', 'r') as f:
            while True:
                s = f.readline()
                if s== "":
                    break
                cursor.execute("INSERT INTO active_code VALUE (%s)", [s])
        
        conn.commit()
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM active_code")
        data_2t = cursor.fetchall()
        for data_t in data_2t:
            for data in data_t:
                print(data)

finally:
    conn.close()