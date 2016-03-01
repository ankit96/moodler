import requests
import re
from bs4 import BeautifulSoup


def main(text):

    mylist = text.split(',')
    username = mylist[0].strip()
    password = mylist[1].strip()
    batch=mylist[2].upper().strip()

    URL = 'http://moodle.spit.ac.in/login/index.php'

    login_data = {
        'username': username,
        'password': password,
        'submit': 'login',
    }

    s = requests.session()
    s.post(URL, login_data)

    r = s.get('http://moodle.spit.ac.in/calendar/view.php', timeout=5)


    soup = BeautifulSoup((r.text).encode('utf-8'))

    soup = soup.findAll('table', {"class": "event"})


    sr = ''
    soup = str(soup).replace("\\n", "")
    soup = str(soup).replace("\\xa0", "")
    soup = BeautifulSoup(str(soup))
    for a in soup.findAll(text=True):
        if 'AM' in str(a) or 'PM' in str(a):
            sr = sr + str(a)
        else:
            sr = sr + '\n' + str(a)
    sr = sr.replace(',', ' ')
    sr = sr.replace('[', ' ')
    sr = sr.replace(']', ' ')
    if len(sr) < 5:
        return "Invalid username,password :( or moodle is down :)"
    flag = 1
    pr = 0
    final = ''
    rbatch = ''
    divider=0
    for line in sr.splitlines():

        if len(str(line)) < 3:
            final = final + str(line) + str(line)
            flag = 1
            pr = 0

        else:

            if flag == 1:

                if 'Batch' in line or 'batch' in line:
                    rbatch = line.replace('-', ' ')
                    rbatch = rbatch.replace('.', ' ')

                    wordList = re.sub("[^\w]", " ",  rbatch).split()

                    for a in wordList:

                        if len(a)==1:
                            if batch in a or a in batch:
                                pr = 1

                                if divider == 0 :
                                    divider =1
                                else:
                                    final = final + '\n -------------------------------------------------------\n'

                            else:
                                pr = 0

                else:
                    if divider ==0 :
                        divider =1
                    else:
                        final = final + '\n -------------------------------------------------------\n'
                    pr = 1
                flag = 0
            if pr == 1:
                final = final + '\n' + str(line)
    return str(final)




