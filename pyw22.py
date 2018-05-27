import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('x.x.x.x', username='user', password='********')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

sftp = ssh.open_sftp()
sftp.get('/home/user/backup_testdb.sql', 'backup_testdb.sql')
sftp.put("pinggraph.png", "/var/www/html/images/pinggraph.png")
sftp.close()

ssh.close()


