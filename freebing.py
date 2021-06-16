
import random
import time
import json
import webbrowser
import os

f = open(r"C:\Users\Richd\PycharmProjects\practiceprojects\bingrewards\words_dictionary.json")
searchwords = json.load(f)

searchwords = list(searchwords.keys())

def givemefreestuff():
    global start
    while start < 51:
        picknumber = random.randint(0,370100)
        newword = searchwords[picknumber]
        edgepath = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgepath))
        webbrowser.get("edge").open(f"https://www.bing.com/search?q={newword}&qs=n&form=QBRE&sp=-1&pq=kare&sc=8-4&sk=&cvid=D47CB7FACFD8448394B94458D90E05EC")
        start += 1
        secs = random.randint(60,80)
        time.sleep(secs)
        os.system("taskkill /im msedge.exe /f")
    print(f"COMPLETE")

start = 0
givemefreestuff()

