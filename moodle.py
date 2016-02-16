
#Used to make requests
import requests
import re
from bs4 import BeautifulSoup

def main():
		username = 'ankit.sagwekar'
		password = 'SPITseit_15'
		batch='D'
		URL = 'http://moodle.spit.ac.in/login/index.php'

		login_data = {
		        'username': username,
		        'password': password,
		        'submit': 'login',
		    }

		s = requests.session()
		s.post(URL, login_data)

		r= s.get('http://moodle.spit.ac.in/calendar/view.php',timeout=5)
		paragraphs = re.findall(r'<div class="referer">(.*?)</div><div class="course">(.*?)</div>(.*?)<span class="date">(.*?)</span>',str(r.text))

		#for eachP in paragraphs:
		soup = BeautifulSoup(str(paragraphs))


		for m in soup.find_all('a'):
			m.replaceWithChildren()
		soup = ''.join(soup.findAll(text=True))
		#print(soup)

		x=[]
		arr = []
		arr.append([])
		i=0
		soup = soup.split("'") 
		for m in soup:
			if len(str(m))>3 and m[0] != ')':
				 x.append(str(m))
				
		#print(str(x))

		for p in x:
			arr[i].append(str(p))
			if str(p).find('AM')!=-1 or str(p).find('PM')!=-1 :
				i=i+1
				arr.append([])
		j=i
		return arr
		'''for a in arr:
			for b in a:
				print(str(b))
			print("")
			print("")
			print("")

		flag=0

		y=[]
		i=0
		for a in arr:
			flag=0
			for b in a:
				if str(b).find('Batch')!=-1:
					flag=1
			if flag==0 and i+1<=j:
				y.append(int(i+1))
			i=i+1
		print(y)
		'''
