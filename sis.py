import requests
from bs4 import BeautifulSoup
import time
from playsound import playsound
from datetime import datetime


URL = 'https://sis-hatyai14.psu.ac.th/SubjectInfo.aspx?subject=2565100220050306'

def req():
 r = requests.get(URL)
 soup = BeautifulSoup(r.content, 'html5lib')
 remain = soup.find('span', {'id': 'ctl00_ctl00_mainContent_PageContent_UcDatalistSubjectClassTable_Public1_DataList1_ctl03_NO_REGISTLabel'})
 return remain.text

while True:
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    remain = int(req())
    if remain < 50 :
        print(now+" GO GO GO GO GO")
        playsound('run.mp3')
    else:
        print(now+' noop')
    time.sleep(120)
#print(remain.text)