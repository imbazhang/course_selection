# work for freshman - study
from requests_html import HTMLSession
import random
import _thread
import webbrowser

def getUrl():
    session = HTMLSession()
    url = "http://applicationnewjw.ecnu.edu.cn/eams/publicSearch.action"
    return session.get(url)

r = getUrl()
Content = r.content
Texts = r.html.text

'''
login_text = input("input your text:")
login_password = input("input your password")

'''

print(Texts)
'''
for i in r.html.text:
    list_links.append(i)
for i in list_links:
    print(i)
'''