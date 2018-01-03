#!/usr/bin/python3.6
import asyncio
import paramiko
import yaml


@asyncio.coroutine
def svn_update(project):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 作用是允许连接不在know_hosts文件中的主机
	try:
		ssh.connect(project[2], config['port'], config['username'], project[1])
	except Exception:
		print("connection %s is time out" % project[0])
		return False
	stdin, stdout, stderr = ssh.exec_command(config['cmd'])
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
	loop = asyncio.get_event_loop()
	tasks = []
	for project in config['projects']:
		tasks.append(asyncio.ensure_future(svn_update(project)))
	loop.run_until_complete(asyncio.wait(tasks))
	print('All cmd finished.')
	loop.close()
