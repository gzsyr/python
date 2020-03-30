from selenium import webdriver
import time
import unittest

def get_data_from_file(file_path):
	with open(file_path, encoding = 'utf-8') as fp:
		test_data = fp.readlines()
	return test_data

def report(test_case_count, test_case_success, test_case_fail):
	print("一共执行%s测试用例" %test_case_count)
	print("		执行成功了%s测试用例" %test_case_success)
	print("		执行失败了%s测试用例" %test_case_fail)


test_datas = get_data_from_file('test_data.txt')

if (test_datas) == 0:
	print('文件数据为空，请补充数据')
	sys.exit(0)
	
test_case_count = len(test_datas)
test_case_success = 0
test_case_fail = 0


for test_data in test_datas:
	try:
		search_word, expected_word = test_data.strip().split('||')
		driver = webdriver.Chrome(executable_path = 'e:\\testPython\\chromedriver.exe')

		driver.get('http://www.sogou.com')

		input_box = driver.find_element_by_id('query')
		input_box.send_keys(search_word)
		button = driver.find_element_by_id('stb')
		button.click()
		time.sleep(3)
		assert expected_word in driver.page_source
	
		driver.quit()
		test_case_success += 1
	except AssertionError:
		print("*"*50)
		test_case_fail += 1
		print("断言错误，原因：%s没有在源码中找到" %expected_word)
		print("*"*50)
	except Expection as e:
		print("*"*50)
		test_case_fail += 1
		print("执行过程中出现未知异常，具体异常信息：%s" %e)
	
	print("测试执行的测试数据：%s" %test_data.strip())
	print("*"*50)
	
report(test_case_count, test_case_success, test_case_fail)
