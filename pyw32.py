import crassh

routers = ["10.0.1.11"]
youraddress = "5.5.5.5"
username = "cisco"
password = "ciscopass"
enablepass = "enpass"
cmd01 = "configure terminal"
cmd02 = "access-list 1 permit host " + youraddress

for device in routers:
   try:
       hostname = crassh.connect(device, username, password, enable=True , enable_password = enablepass)
       print("Connected device %s [%s]" %(hostname,device))
       crassh.send_command(cmd01, hostname)
       crassh.send_command(cmd02, hostname)
       crassh.disconnect()
   except:
       print("Can not connect to [%s]" %device)
       pass



	
