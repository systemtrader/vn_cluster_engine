# -*- coding: utf-8 -*-
import socket
from tornado.tcpserver import TCPServer
from tornado.iostream import IOStream

class tcp_listener(TCPServer):
	def __init__(self,callback):
		super(tcp_listener, self).__init__()
		self.callback_entry=callback
		pass
	
	def handle_stream(self, stream, address):
		'''
		客户端连入时触发的回调
		'''
		try:
			stream.read_until_close(self.callback_entry)#流数据(实际上是事件)读取完成触发回调入口函数处理事件
		except:
			print 'TCP监听端口读取失败'
			pass
		pass

class tcp_sender(object):

	
	def __init__(self,target_ip,target_port,message):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		self.__message=message
		self.__stream=IOStream(s)
		self.__stream.connect((target_ip, target_port), self.__sending_action)
		pass
	pass

class tcp_gateway(object):
	'''
	tcpip消息入口服务器，iostream默认缓冲区100mb
	'''
	
	def __init__(self, in_port, callback_entrance):
		super(tcp_gateway, self).__init__()#注意此处tcpserver可以有出入缓冲区大小的设置
		self.__tcp_lisener=tcp_listener(callback_entrance)
		self.__tcp_lisener.bind(in_port)
		self.__tcp_lisener.start()
		pass
	
	def __sending_action(self):
		self.__sending_stream.write(self.__message, self.__clear_up)#发送完成时关闭流
		pass
	
	def __clear_up(self):
		self.__sending_stream.close()
		self.__sending_stream=None
		self.__message=None
		pass
	
	
	
	def send_string(self,target_ip,target_port,string_data):
		self.sending_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		self.__message=string_data
		self.__sending_stream=IOStream(self.sending_socket)
		self.__sending_stream.connect((target_ip, target_port), self.__sending_action)
		pass
	pass