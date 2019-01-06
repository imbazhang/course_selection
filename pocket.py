from selenium import webdriver
from selenium.webdriver.support.wait import *
import os
import xlwt
from selenium.webdriver.common.by import By # 导入所有的模块

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"     # 启动chrome需要另外一个Chromedriver程序
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:/Users/imbazhang/AppData/Local/Google/Chrome/User Data/Default')       # 导入我本机的chrome设置，没啥用
os.environ["webdriver.chrome.driver()"] = chromedriver   

public_database = "https://portal1.ecnu.edu.cn/cas/login?service=http%3A%2F%2Fportal.ecnu.edu.cn%2Fneusoftcas.jsp"
browser = webdriver.Chrome(chromedriver, chrome_options = option)  # 准备打开网页    启动



browser.get(public_database) # 打开数据库登陆页面

browser.find_element_by_id("un").send_keys("10185102120")     # account
browser.find_element_by_id("pd").send_keys("123456abc")       # password
os.system("pause") # 人工输入验证码：需要修改

browser.find_element_by_id("index_login_btn").click()         # action
os.system("pause")

application_new_jw = "http://applicationnewjw.ecnu.edu.cn/eams"   # 选课
browser.get(application_new_jw)
os.system("pause")


application_action = "http://applicationnewjw.ecnu.edu.cn/eams/stdElectCourse.action"   # 进入选课
browser.get(application_action)   # 跳转到选课页面（这里直接分析第二轮选课页面）
# os.system("pause")


print("进入 跨年级跨专业选课 还是 本专业第二轮选课？跨选输入 1，本专业输入 2")
n  = int(input())
if n is 1:
    application = "http://applicationnewjw.ecnu.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=2631"
else:
    application = "http://applicationnewjw.ecnu.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=2630"
browser.get(application)
os.system("pause")  # 分页面进行

Electable_classes = []

pageNum = 1
while pageNum < 34:
    table_elecatable = browser.find_element_by_id('electableLessonList') #定位可选课程表格
    table_elecatable_rows = table_elecatable.find_elements_by_tag_name('tr')   # 获取总计行数
    table_elecatable_cols = table_elecatable_rows[0].find_elements_by_tag_name("th")
    electable_text = table_elecatable.text.split('\n')
    '''
    for i in range(len(table_elecatable_rows)):
        for j in range(len(table_elecatable_cols)):
            text.append(table_elecatable_rows[i].find_elements_by_tag_name("td")[j].text)
    
    print(table_elecatable, table_elecatable_rows, table_elecatable_cols)
    '''
    for i in range(len(electable_text)):
        electable_text[i] = [electable_text[i]]
    for i in range(len(electable_text)):
        text = electable_text[i][0]
        electable_text[i] = text.split()
    i = 0
    while i < len(electable_text):           # 由于多个老师同时任教一门课程时会对他们各自的上课时间分割，这里进行了合并
        if len(electable_text[i]) <= 5:
            if len(electable_text[i]) is 3:
                electable_text[i - 1][7] = electable_text[i - 1][7] + electable_text[i][0]
                electable_text[i - 1][8] = electable_text[i - 1][8] + electable_text[i][1]
                electable_text[i - 1][9] = electable_text[i - 1][9] + electable_text[i][2]
                del electable_text[i]
            elif len(electable_text[i]) is 4:
                electable_text[i - 1][7] = electable_text[i - 1][7] + electable_text[i][0]
                electable_text[i - 1][8] = electable_text[i - 1][8] + electable_text[i][1]
                electable_text[i - 1][9] = electable_text[i - 1][9] + electable_text[i][2]
                electable_text[i - 1].append(electable_text[i][-1])
                del electable_text[i]
            elif len(electable_text[i]) is 5:
                electable_text[i - 1][7] = electable_text[i - 1][7] + electable_text[i][0] + electable_text[i][1]
                electable_text[i - 1][8] = electable_text[i - 1][8] + electable_text[i][2]
                electable_text[i - 1][9] = electable_text[i - 1][9] + electable_text[i][3]
                electable_text[i - 1].append(electable_text[i][-1])
                del electable_text[i]
        else:
            i += 1
    for i in electable_text:
        Electable_classes.append(i)       # 加入到总表中

    browser.find_element_by_class_name("pgNextBtn").click()    # 自动转到下一页
    pageNum += 1

elecatable_class_workbook = xlwt.Workbook()        # 所有页面爬取完成吼创建表格
elecatable_class_sheet = elecatable_class_workbook.add_sheet('Elecatable classes')

for i in range(len(Electable_classes)):
    for j in range(len(Electable_classes[i])):
        if Electable_classes[i][j] == '分组（已选/上限）':  # 删除一个没有用的元素
            del Electable_classes[i][j]
            break
        break

for i in range(len(Electable_classes)):
    for j in range(len(Electable_classes[i])):
        elecatable_class_sheet.write(i, j, Electable_classes[i][j])      # 写入

elecatable_class_workbook.save("Elecatable_Classes.xls")          # 保存

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
def get_table_content(tableid, queryCpntent):                   # 网上抄的代码
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