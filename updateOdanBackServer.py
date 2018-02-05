#!/usr/bin/python3.6
import paramiko
import yaml
import time
import multiprocessing

def svn_update(project,config):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 作用是允许连接不在know_hosts文件中的主机
	try:
		ssh.connect(project[2], config['port'], config['username'], project[1])
	except Exception:
		print("connection %s is time out" % project[0])
		return False
	stdin, stdout, stderr = ssh.exec_command('''
		echo 'server{
        listen 80;
        server_name %s-m.iposecure.com;
        #告诉浏览器有效期内只准用 https 访问
        add_header Strict-Transport-Security max-age=15768000;
        return 301 https://$server_name$request_uri;
}
server{
        listen 80;
        server_name %s-agent.iposecure.com;
        #告诉浏览器有效期内只准用 https 访问
        add_header Strict-Transport-Security max-age=15768000;
        return 301 https://$server_name$request_uri;

}
server{
        listen 80;
        server_name %s-op.iposecure.com;
        #告诉浏览器有效期内只准用 https 访问
        add_header Strict-Transport-Security max-age=15768000;
        return 301 https://$server_name$request_uri;

}
'  > /www/wdlinux/nginx/conf/vhost/https.conf;
service nginxd restart
	
	''' % (project[0],project[0],project[0]))
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
		my_thread = multiprocessing.Process(target=svn_update,args=(project,config))
		my_thread.start()
		my_thread.join()
	print('all finished update')
