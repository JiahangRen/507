# -*- coding: UTF-8 -*-
import streamlit as st   # pip install streamlit
import pandas as pd
import sqlite3
import numpy as np

#---------------------------------------------------------------------------
# 1. Show data
#---------------------------------------------------------------------------
st.title("NBA player on Twitter")
con = sqlite3.connect("./twitter_nba.db")
cur = con.cursor()
sql = "select * from user_info"
player_df = pd.read_sql(sql, con)

if st.checkbox('Show NBA player data'):
    st.write(player_df)



#---------------------------------------------------------------------------
# 2. Ask user to select data
#---------------------------------------------------------------------------
selected_player = st.selectbox(
    'Which player do you like see?',
    player_df['username'])

st.write('You selected: ', selected_player)

# find player id by username
user_id_sql = f"""select * from user_info 
              where username='{selected_player}'"""

cur.execute(user_id_sql)
selected_user_id = cur.fetchall()[0][0]
print(selected_user_id)
st.write(selected_user_id)


#---------------------------------------------------------------------------
# 3. Player following data
#---------------------------------------------------------------------------
# following_sql = "select * from user_with_follwing"
following_sql = f"""select * from user_with_follwing 
              where player_id='{selected_user_id}'"""
st.write(f"Showing the people followed by: {selected_player} ")
player_following_df = pd.read_sql(following_sql, con)
st.write(player_following_df)
st.write("Total: ", player_following_df.shape[0])


#---------------------------------------------------------------------------
# 3. Check if there is friendship in these 12 players
#---------------------------------------------------------------------------

nba_star = ["KDTrey5", "JHarden13", "russwest44", "CP3", "Giannis_An34",
            "Dame_Lillard", "TheTraeYoung", "DevinBook", "ZachLaVine",
            "StephenCurry30", "KlayThompson", "DeMar_DeRozan"]

player_id = ['35936474', '50811932', '35982046', '53853197', '2279776304', '267425142', '2842841126', '237073728',
             '405205681', '42562446', '1703636814', '43658360']

player_dic = {x: y for x, y in zip(player_id, nba_star)}

friends = []
for i in player_following_df["following_user_id"]:
    if i in player_id:
        friends.append(player_dic[i])

if len(friends) > 0:
    st.write(f"{selected_player}'s league friends on Twitter are: ")
    st.write(", ".join(friends))
else:
    st.write(f"Oops!  {selected_player} doesn't have any league friend on Twitter.")


#---------------------------------------------------------------------------
# 4. Compare the number of friends and plot
#---------------------------------------------------------------------------
total_following_df = pd.read_sql("select * from user_with_follwing", con)
# st.write(total_following_df)


friends_count_dic = {}
total_friends_dic = {}
for p_id in player_id:
    filt = total_following_df["player_id"] == p_id
    p_df = total_following_df[filt]

    cnt = 0
    friends_list =[]
    for i in p_df["following_user_id"]:
        if i in player_id:
            friends_list.append(player_dic[i])
            cnt += 1

    friends_count_dic[player_dic[p_id]] = cnt
    total_friends_dic[player_dic[p_id]] = friends_list


st.write("Friends Count for all players: ")
s = pd.Series(friends_count_dic).to_frame()
st.bar_chart(s)


# total_friends_df = pd.DataFrame(total_friends_dic)
# st.write("total_friends_dic ", total_friends_df)