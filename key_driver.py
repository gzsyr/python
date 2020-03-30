from selenium import webdriver
import time
import os.path
import sys
import csv

driver = None

def open_browser(browser_name):
	global driver
	if "chrome" in browser_name.lower():
		driver = webdriver.Chrome(executable_path = 'e:\\testPython\\chromedriver')
	elif "ie" in browser_name.lower():
		driver = webdriver.Ie(executable_path = '')
	else:
		driver = webdriver.Firefox(executable_path = '')

def visit(url):
	global driver
	driver.get(url)
	
def input(xpath_exp, value):
	global driver
	driver.find_element_by_xpath(xpath_exp).send_keys(value)
	
def clear(xpath_exp):
	global driver
	driver.find_element_by_xpath(xpath_exp).clear()

def click(xpath_exp):
	global driver
	driver.find_element_by_xpath(xpath_exp).click()
	
def sleep(seconds):
	time.sleep(int(seconds))
	
def assert_word(expect_word):
	global driver
	assert expect_word in driver.page_source
	
def quit():
	global driver
	driver.quit()
	
'''从csv文档中获取数据，执行用例'''
def get_case_steps_from_csv_file(file_path):
	if not os.path.exists(file_path):
		print("文件不存在，错误！")
		sys.exit(0)
	datas = []
	with open(file_path, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
		for row in spamreader:
			data = '||'.join(row)
			#print(data)
			datas.append(data)
	return datas

datas = get_case_steps_from_csv_file("case_data.csv")
print("csv文档整理的数据: %s"  %datas)

if len(datas) == 0:
	print("csv文件没有数据，请重新录入！")
	sys.exit(0)

flag = True
for data in datas:
	tmpData = list(filter(None, data.split(',')))
	#print(tmpData)
	if "step_name" in tmpData:
		print("此为首行展示的列名称：%s，不需要执行" %tmpData)
		continue
	elif len(tmpData) == 3:
		name, xpath, value = tmpData
		command = "%s(\"%s\",\"%s\")" %(name, xpath, value)
	elif len(tmpData) == 2:
		name, value = tmpData
		command = "%s(\"%s\")" %(name, value)
	elif len(tmpData) == 1:
		command = tmpData[0] + '()'
	else:
		print("此步骤数据不符合条件：%s！" %tmpData)
		
	print(command)
	try:
		eval(command)
	except:
		print("执行用例失败：%s" %command)
		flag = False

if flag == True:
	print("所有用例执行成功！")
else:
	print("有用例执行失败！")
	
	
'''
#从txt文档中获取数据
def get_key_data_from_file(file_path):
	if not os.path.exists(file_path):
		print("文件不存在，错误！")
		sys.exit(0)
	with open(file_path, encoding = 'utf-8') as fp:
		data = []
		for line in fp:
			data.append(line.strip())
	return data

datas = get_key_data_from_file('key_data.txt')
if len(datas) == 0:
	print("没有读取到任何测试数据步骤！")
	sys.exit(0)
	
flag = True
for data in datas:
	if data.count("||") == 0:
		command = data + "()"
	elif (data.count("||") == 1):
		func_name, value = data.split("||")
		xpath = None
		command = "%s(\"%s\")" %(func_name, value)
		#command = func_name + "(" + value + ")"
	elif (data.count("||") == 2):
		func_name, xpath, value = data.split("||")
		command = "%s(\"%s\", \"%s\")" %(func_name, xpath, value)
		#command = data[0] + "(" + data[1] + "," + data[2] + ")"
	print(command)
	try:
		eval(command)
	except:
		flag = False
		print("测试用例执行失败！%s" %command)
	else:
		print("测试用例执行成功！")

if flag == True:
	print("所有测试执行成功！")
else:
	print("有测试步骤错误！")
'''	


'''
#方法调用实现用例
open("chrome")
visit("http://www.sogou.com")
input("//input[@id='query']", "365淘房")
click("//input[@id='stb']")
sleep(3)
assert_word("house365.com")
quit()

open("chrome")
visit("http://www.baidu.com")
input("//input[@id='kw']", "自动化测试")
sleep(3)
assert_word("ke.qq.com")
quit()
'''
'''
#在代码中写入参数执行用例
driver = webdriver.Chrome(executable_path = 'e:\\testPython\\chromedriver.exe')

driver.get("http://www.sogou.com")

search_box = driver.find_element_by_xpath("//input[@id='query']")

search_box.send_keys("365淘房")

submit_button = driver.find_element_by_xpath("//input[@id='stb']")

submit_button.click()

time.sleep(3)

assert "house365.com" in driver.page_source

driver.quit()
'''