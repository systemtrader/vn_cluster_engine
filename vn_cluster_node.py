# -*- coding: utf-8 -*-

from tcp_io_gateway import tcp_gateway
from utilities.environment_and_platform import get_current_environment_pack
from utilities.ip_and_socket import scan_available_ports_then_return
from tornado_timer import tornado_timer
from datetime import timedelta,datetime
from utilities.csv_and_json_serialisation import temperarily_load_a_local_json


class vn_event_agent_node(object):
	'''
	事件代理节点，每个工作类产生的事件都往节点里面塞，它应该和工作类在同一个线程/进程中构造
	每一类事件作为集群中的一个订阅topic
	'''
	#----------------------------------------------------------------------
	def __init__(self,config_file=None):
		"""初始化事件引擎"""
		self._environment_pack=get_current_environment_pack()
		
		if not config_file:
			self._listening_port=scan_available_ports_then_return(
				self._environment_pack['current_platform_info']['current_system_category'])#搜索一个还没有被占用的端口，接下来开始监听
		else:
			config=temperarily_load_a_local_json(config_file)
			self._listening_port=config['listening_port'] if config else scan_available_ports_then_return(
				self._environment_pack['current_platform_info']['current_system_category'])
			pass
		
		self._tcp_gateway=tcp_gateway(self._listening_port, self.__process)
		self.__handlers={}
		self.__timer=tornado_timer(emit_interval=timedelta(seconds=3),emit_function=self.__test_emit)
		
		pass
	
	def __test_emit(self):
		target_port=31416 if self._listening_port==31418 else 31418
		target_string="%s,my port is %d"%(datetime.now().__repr__(),self._listening_port)
		self._tcp_gateway.send_string("0.0.0.0",target_port,target_string)
		pass
	
	#----------------------------------------------------------------------
	def __run(self):
		"""引擎运行"""
		pass
	
	#----------------------------------------------------------------------
	def __process(self, event):
		'''
		事件入口
		'''
		print event
		pass
		#for handler in self.__handlers[event.type_]:
		#handler(event)
	
	#----------------------------------------------------------------------
	def start(self):
		"""引擎启动"""
		# 将引擎设为启动
		pass
	
	#----------------------------------------------------------------------
	def stop(self):
		"""停止引擎"""
		# 将引擎设为停止
		pass
	
	#----------------------------------------------------------------------
	def register(self, type_, handler):
		"""注册事件处理函数监听"""
		# 尝试获取该事件类型对应的处理函数列表，若无则创建
		try:
			handlerList=self.__handlers[type_]
		except KeyError:
			handlerList=[]
			self.__handlers[type_]=handlerList
		
		# 若要注册的处理器不在该事件的处理器列表中，则注册该事件
		if handler not in handlerList:
			handlerList.append(handler)
	
	#----------------------------------------------------------------------
	def unregister(self, type_, handler):
		"""注销事件处理函数监听"""
		# 尝试获取该事件类型对应的处理函数列表，若无则忽略该次注销请求
		try:
			handlerList=self.__handlers[type_]
			
			# 如果该函数存在于列表中，则移除
			if handler in handlerList:
				handlerList.remove(handler)
			
			# 如果函数列表为空，则从引擎中移除该事件类型
			if not handlerList:
				del self.__handlers[type_]
		except KeyError:
			pass
	
	#----------------------------------------------------------------------
	def put(self, event):
		pass
	pass