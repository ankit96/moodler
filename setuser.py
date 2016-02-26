import os
import psycopg2
import urlparse
def set(string):

    conn = psycopg2.connect(
        database='dc',
        user='s a',
        password='sc',
        host='s ',
        port='23'

    )

    mylist = string.split('%')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id,user_name,text,channel_id,channel_name,team_id,team_domain) VALUES ('"+str(mylist[4])+"','"+str(mylist[5])+"','"+str(mylist[6])+"','"+str(mylist[2])+"','"+str(mylist[3])+"','"+str(mylist[1])+"','"+str(mylist[0])+"');")
    conn.commit()
    conn.close()
    return "Successfully registered"
