# -*- coding: UTF-8 -*-
import os
import csv
import sqlite3


# convert csv file to sql  table
def read_csv(filepath):
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        my_reader = csv.reader(f)
        for row in my_reader:
            data.append(row)
            # print(row)
    return data


# sqlite3
class DB:
    def __init__(self):
        self.db_name = "twitter_nba.db"

    def create_table(self, datalist, table_name):
        if self.db_name in os.listdir():
            os.remove(self.db_name)

        con = sqlite3.connect(self.db_name)
        c = con.cursor()

        columns= ", text".join(datalist[0])
        columns_length = len(datalist[0])
        c.execute(f'''CREATE TABLE {table_name}
                    ({columns})''')

        # ['user_id', 'name', 'username', 'description', 'url', 'location']
        question_mark = ",".join(["?" for _ in range(columns_length)])
        c.executemany(f'INSERT INTO {table_name} VALUES ({question_mark})', datalist[1:])
        con.commit()
        con.close()

    # create user table  and set up primary key
    def create_user_info_table(self, datalist, table_name):
        con = sqlite3.connect(self.db_name)
        c = con.cursor()

        # set primary key to user_id
        # '35936474', 'Kevin Durant', 'KDTrey5' ""
        columns = "user_id text PRIMARY KEY, name text, " \
                  "username text, description text, url text, location text"
        print(columns)
        columns_length = len(datalist[0])
        c.execute(f'''CREATE TABLE {table_name}
                            ({columns})''')

        # ['user_id', 'name', 'username', 'description', 'url', 'location']
        question_mark = ",".join(["?" for _ in range(columns_length)])
        c.executemany(f'INSERT INTO {table_name} VALUES ({question_mark})', datalist[1:])
        con.commit()
        con.close()


    # create following table and set FOREIGN KEY
    # https://www.sqlite.org/foreignkeys.html
    def create_following_table(self, datalist, table_name):
        con = sqlite3.connect(self.db_name)
        c = con.cursor()

        columns_length = len(datalist[0])
        c.execute(f'''CREATE TABLE {table_name}(
                      player_id text, 
                      following_user_id text,
                      following_name text,
                      following_username text,
                      FOREIGN KEY(player_id) REFERENCES user_info(user_id)
                );''')
        question_mark = ",".join(["?" for _ in range(columns_length)])
        c.executemany(f'INSERT INTO {table_name} VALUES ({question_mark})', datalist[1:])
        con.commit()
        con.close()

    def show_table(self, table_name):
        print(f"show data from : {table_name}")
        con = sqlite3.connect(self.db_name)
        c = con.cursor()
        c.execute(f'SELECT * FROM {table_name}')
        info = c.fetchall()

        # print(info)

        print([i[0] for i in info])
        print([i[1] for i in info])
        print([i[2] for i in info])

        # c.close()
        return info

    def show_all_tables(self):
        con = sqlite3.connect(self.db_name)
        cursor = con.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        tables = [x[0] for x in cursor.fetchall()]
        print(tables)
        return tables


if __name__ == '__main__':
    d = DB()

    # x1 = read_csv("user_info.csv")
    # d.create_user_info_table(x1, "user_info")

    d.show_table("user_info") ### 111

    # x2 = read_csv("user_with_follwing.csv")
    # d.create_following_table(x2, "user_with_follwing")

    # d.show_table("user_with_follwing") ## 2222


    # x3 = read_csv("user_tweets.csv")
    # d.create_table(x2, "user_tweets")
    # d.show_table("user_tweets")

    # d.show_all_tables()


