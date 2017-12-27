#!/usr/bin/python3.6
import paramiko
import yaml
import time
import threading

def svn_update(project):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 作用是允许连接不在know_hosts文件中的主机
	try:
		ssh.connect(project[2], config['port'], config['username'], project[1])
	except Exception:
		print("connection %s is time out" % project[0])
		return False
	stdin, stdout, stderr = ssh.exec_command('svn up /www/web/indonesia2/')
	endtime = time.time() + timeout
	result = stdout.read()
	error = stderr.read().decode('utf-8')
	result = result.decode('utf-8')
	if not error:
		print("<<< " + str(project[0]) + ":\n" + result)
	else:
		print("<<< " + str(project[0]) + ":\n" + error)
	ssh.close()
	return True

if __name__ == '__main__':
	timeout = 1000
	f = open('./config.yaml')
	config = yaml.load(f)
	for project in config['projects']:
		my_thread = threading.Thread(target=svn_update,args=(project,))
		my_thread.start()
		my_thread.join()
	print('all finished update')
