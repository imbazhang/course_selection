# work for freshman - study
# 通过request和服务器交流的尝试
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

'''
electableLessonList = browser.find_elements_by_css_selector("electGridTr electGridTr-even")
lessonList = []
for lesson in electableLessonList:
    L = browser.find_elements_by_tag_name("td")
    print(L)
    os.system("pause")
    '''

'''
class_first = []
for i in browser.find_elements_by_css_selector("[class='electableCell defaultElected']"):   # 定位每天的第一节课的尝试
    class_first.append([])
print(class_first)
cLass = []
for i in class_first:
    unit = i.find_elements_by_tag_name("unit")
    weekday = i.find_elements_by_tag_name("weekday")
    cLass.append([unit,weekday,i.text])
os.system("pause")
'''

'''
trlist = browser.find_elements_by_tag_name("tr")   #定位tr 标签的尝试
tr_text_list = []
for tr in trlist:
    if tr.text != "":
        tr_text_list.append(tr.text.split())
    print(tr_text_list)
    tdlist = tr.find_elements_by_tag_name("td")
    if len(tdlist) > 0:
        text = tr.find_elements_by_tag_name("td")[0].text
        print(text)
        '''


'''
table = []
table.append(browser.find_element_by_id("electGroupResultsTable"))    # 定位选课结果id的尝试
print(table)
'''

'''
def get_table_content(tableid, queryCpntent):
    arr = []
    arr1 = []
    table_loc = (By.ID,tableid)
    table_tr_list = webdriver.find_element(*table_loc).find_elements(By.TAG_NAME, "tr")
    for tr in table_tr_list:
        arr1 = (tr.text).split(" ")
        print(tr.text)
        print(arr1)
        arr.append(arr1)

    print(arr1)
'''
# get_table_content("")