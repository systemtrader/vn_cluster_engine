# -*- coding: utf-8 -*-
from os import path, environ

if __name__=='__main__':
	
	current_env=environ
	from utilities.process_and_main_function.main_function import main
	
	current_start_script=path.realpath(__file__)#取得当前main.py脚本的绝对路径
	main(current_start_script)#传入单个工作实例的类定义，在主线程中构造之
	pass