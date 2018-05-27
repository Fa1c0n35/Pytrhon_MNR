import subprocess
ipaddr = "1.1.1.1"
result = subprocess.run(["ping",ipaddr], stdout=subprocess.PIPE, universal_newlines="\r\n")
print("return code:",result.returncode)
print(result.stdout)


