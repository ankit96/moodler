import os
import psycopg2
import urlparse



def set(string):

    conn = psycopg2.connect(
        database='a',
        user='b',
        password='a',
        host='q',
        port='t'

    )

    mylist = string.split('%')
    cur = conn.cursor()


    text=mylist[6]
    mytext=text.split(',')
    password=mytext[1]

    encrypt = #some encoded password
    cur.execute("select * from users where \"user_id\"=%s", (mylist[4],))
    rows = cur.fetchall()
    ct=0
    for row in rows:
        ct=ct+1
    if ct==1:
        return "Already your data is with us ,if you want to delete your previous data ,apply /deletemoodle command"
    data=mytext[0]+','+encrypt+','+mytext[2]

    cur.execute("INSERT INTO users (user_id,user_name,text,channel_id,channel_name,team_id,team_domain) VALUES ('"+str(mylist[4])+"','"+str(mylist[5])+"','"+str(data)+"','"+str(mylist[2])+"','"+str(mylist[3])+"','"+str(mylist[1])+"','"+str(mylist[0])+"');")

    conn.commit()
    conn.close()
    return "Successfully registered"

def delete(userid):
     conn = psycopg2.connect(
        database='a',
        user='b',
        password='a',
        host='p',
        port='w'

    )


     cur = conn.cursor()
     cur.execute("select * from users where \"user_id\"=%s", (userid,))
     rows = cur.fetchall()
     ct=0
     for row in rows:
        ct=ct+1
     if ct==0:
        return "No data present in database to delete which matches your data"

     cur.execute("Delete from users where \"user_id\"=%s", (userid,))

     conn.commit()
     conn.close()

     return "Your data is deleted succesfully"

