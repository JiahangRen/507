# -*- coding: UTF-8 -*-
import json


class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children


def build_tree_from_json():
    with open("player_tree.json", "r") as json_file:
        data = json.load(json_file)
        # print(data)

    children_nodes = []
    for k, v in data.items():
        if k == "root":
            nba_star = v
        else:
            player_node = Node(k, v)
            children_nodes.append(player_node)

    root_node = Node("root", children_nodes)
    return  root_node



build_tree_from_json()
