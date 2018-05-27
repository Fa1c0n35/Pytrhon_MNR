import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('x.x.x.x', username='user', password='********')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

stdin, stdout, stderr = ssh.exec_command("pwd")

for line in stdout.readlines():
    print(line.strip())
ssh.close()

