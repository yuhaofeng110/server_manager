#!/usr/bin/python3.6

import pymysql
import yaml
import multiprocessing


class execMysql:
	def __init__(self):
		f = open('./mysql.yaml',encoding = 'utf-8')
		self.config = yaml.load(f)
	
	def executeOne(self, config, project):
		db = pymysql.connect(project[1], project[2], project[3], project[2], charset='utf8')
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """ALTER TABLE `t_loan` ADD COLUMN `close_time` datetime(0) DEFAULT NULL COMMENT 'loan close time'  """
		res = cursor.execute(sql)
		result = cursor.fetchall()
		db.commit()
		cursor.close()
		db.close()
		print("<<< %s 影响行数: %s " %(project[0], res) )
		print(result)
		print("\n")
	
	def execute(self):
		for project in self.config['projects']:
			my_process = multiprocessing.Process(target=self.executeOne, args=(self.config, project,))
			my_process.start()
			my_process.join()
		print("\n*************  all cmd finished ***************")


if __name__ == '__main__':
	exec = execMysql()
	exec.execute()
