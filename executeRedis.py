import redis
import yaml
import multiprocessing


# 清除redis
class execRedis:
	def __init__(self):
		f = open('./redis.yaml', encoding='utf-8')
		self.config = yaml.load(f)
	
	def executeOne(self, config, project):
		r = redis.Redis(host=project[1], port=9053, db=project[2], password=project[3])
		res = r.flushdb()
		print('<<< %s 清除redis: %s ' % (project[0], res))
	
	def execute(self):
		for project in self.config['projects']:
			my_process = multiprocessing.Process(target=self.executeOne, args=(self.config, project,))
			my_process.start()
			my_process.join()
		print("\n*************  all cmd finished ***************")


if __name__ == '__main__':
	exec = execRedis()
	exec.execute()
