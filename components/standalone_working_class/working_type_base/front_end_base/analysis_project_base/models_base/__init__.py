# encoding: UTF-8

from components import analysis_project_base

class models_base(analysis_project_base):
	'''
	研究模型基类
	'''

	def __init__(self):
		super(models_base, self).__init__()
		self._is_data_ready=False

	def __get_needed_data_from_each_file(self,data_filename):
		pass
	pass