# -*- coding: UTF-8 -*-
import sqlite3


class Node:
    def __init__(self):
        self.data = None
        self.children = []

# todo
"""
                                Root
                      /          |             \
                    /            |              \
                  /              |               \
            "KDTrey5",      "JHarden13",        "russwest44",      ... "player_12"
         /      |      \
        /       |        \
      /         |         \
following_1 following_2,  following_3,  ...  following_100
"""

#  Tree: 12 players ---> their following user

class PlayerTree:
    def __init__(self):
        self.db_name = "twitter_nba.db"
        self.table_name = "user_with_follwing"
        self.root = Node("Base", [])  # 1. first level

    def get_data(self):
        con = sqlite3.connect(self.db_name)
        c = con.cursor()
        c.execute(f'SELECT * FROM {self.table_name}')
        column_names = [description[0] for description in c.description]
        print(column_names)

        info = c.fetchall()
        # for i in info:
        #     print(i)
        # print(info)
        return info

    def build_graph(self):
        data = self.get_data()

        # set up the second layer



if __name__ == '__main__':
    graph = PlayerTree()
    graph.get_data()





