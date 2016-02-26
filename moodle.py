import requests
import re
from bs4 import BeautifulSoup


def main(text):

    mylist = text.split(',')
    username = mylist[0]
    password = mylist[1]
    batch=mylist[2].upper()
    '''
    username = 'ankit.sagwekar'
    password = 'SPITseit_15'
    batch = 'D'
	'''
    URL = 'http://moodle.spit.ac.in/login/index.php'

    login_data = {
        'username': username,
        'password': password,
        'submit': 'login',
    }

    s = requests.session()
    s.post(URL, login_data)

    r = s.get('http://moodle.spit.ac.in/calendar/view.php', timeout=5)
    #print(str(r.text))

    soup = BeautifulSoup((r.text).encode('utf-8'))

    soup = soup.findAll('table', {"class": "event"})
    # print(str(soup))
    i = 0
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

    flag = 1
    pr = 0
    final = ''
    rbatch = ''
    for line in sr.splitlines():

        if len(str(line)) < 3:
            final = final + str(line) + str(line)
            flag = 1
            pr = 0
        # print('flag='+str(flag))
        else:

            if flag == 1:
                #print line
                if 'Batch' in line or 'batch' in line:
                    rbatch = line.replace('-', ' ')
                    rbatch = rbatch.replace('.', ' ')
                    '''
                    rbatch = rbatch.replace('Batch', '')
                    rbatch = rbatch.replace('Exp', '')
                    rbatch = rbatch.replace('Expt', '')
                    rbatch = rbatch.replace('Practical', '')
                    '''
                    wordList = re.sub("[^\w]", " ",  rbatch).split()
                    #print("-------------------------------")
                    for a in wordList:
                        #print(str(a))
                        if len(a)==1:
                            if batch in a:
                                pr = 1
                                #print("This is shit" +str(batch)+"  "+str(rbatch))
                                final = final + '\n -------------------------------------------------------\n'
                            # print "made pr=1"
                            else:
                                pr = 0

                else:
                    final = final + '\n -------------------------------------------------------\n'
                    pr = 1
                flag = 0
            if pr == 1:
                final = final + '\n' + str(line)
    return str(final)
    #print str(final)



