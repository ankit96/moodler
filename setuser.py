import os
import psycopg2
import urlparse
def set(string):

    conn = psycopg2.connect(
        database='dbsq99cd6govf2',
        user='aoqfgpcbnlwuat',
        password='FSm2OLpubzgXYM_bSNv3PzYHaD',
        host='ec2-107-20-153-141.compute-1.amazonaws.com',
        port='5432'

    )

    mylist = string.split('%')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id,user_name,text,channel_id,channel_name,team_id,team_domain) VALUES ('"+str(mylist[4])+"','"+str(mylist[5])+"','"+str(mylist[6])+"','"+str(mylist[2])+"','"+str(mylist[3])+"','"+str(mylist[1])+"','"+str(mylist[0])+"');")
    conn.commit()
    conn.close()
    return "Successfully registered"
