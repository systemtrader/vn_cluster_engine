# -*- coding: utf-8 -*-
from zmq.eventloop import IOLoop

from utilities.process_and_main_function.my_engine import my_engine
from vn_cluster_node import vn_event_agent_node

def main(start_script_file,running_class_def=None):
	'''主函数，传入开始执行的主函数，然后以指定的类作为起始工作实例，为单实例机器的程序入口'''
	a=my_engine(vn_event_agent_node,config_file='config_a.json')
	b=my_engine(vn_event_agent_node,config_file='config_b.json')
	IOLoop.instance().start()
	pass