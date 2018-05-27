import crassh

router = "10.0.1.11"
username = "admin"
password = "admin1234"
cmd01 = "show running-config"

try:
    hostname = crassh.connect(router, username, password)
    print("Connected device %s [%s]" %(hostname,router))
    output = crassh.send_command(cmd01, hostname)
    print(output)
    crassh.disconnect()

except:
    print("Can not connect to [%s]" %router)

