# -*- coding: UTF-8 -*-
import sqlite3


class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children


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

    def get_data(self):
        con = sqlite3.connect(self.db_name)
        c = con.cursor()
        c.execute(f'SELECT * FROM {self.table_name}')
        # column_names = [description[0] for description in c.description]
        # print(column_names)

        info = c.fetchall()
        return info

    def build_tree(self):
        # data = self.get_data()
        # print(data)

        nba_star = ["KDTrey5", "JHarden13", "russwest44", "CP3", "Giannis_An34",
                    "Dame_Lillard", "TheTraeYoung", "DevinBook", "ZachLaVine",
                    "StephenCurry30", "KlayThompson", "DeMar_DeRozan"]

        player_id = ['35936474', '50811932', '35982046', '53853197', '2279776304', '267425142', '2842841126', '237073728', '405205681', '42562446', '1703636814', '43658360']

        # 1. build the second layer of the tree
        children_nodes = []

        con = sqlite3.connect(self.db_name)
        c = con.cursor()
        for player_name, p_id in zip(nba_star, player_id):
            sql = f"""select * from user_with_follwing
                      where player_id = {p_id}"""
            c.execute(sql)
            following_data = c.fetchall()
            player_node = Node(player, following_data)
            children_nodes.append(player_node)

        root = Node("root", children_nodes)
        return root


if __name__ == '__main__':
    tree = PlayerTree()
    # tree.get_data()

    tree.build_tree()


