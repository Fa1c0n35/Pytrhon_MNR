import re

pingResult = '\nPinging 1.1.1.1 with 32 bytes of data:\nReply from 1.1.1.1: bytes=32 time=32ms TTL=54\nReply from 1.1.1.1: bytes=32 time=31ms TTL=54\nReply from 1.1.1.1: bytes=32 time=32ms TTL=54\nReply from 1.1.1.1: bytes=32 time=32ms TTL=54\n\nPing statistics for 1.1.1.1:\n    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\nApproximate round trip times in milli-seconds:\n    Minimum = 34ms, Maximum = 63ms, Average = 41ms\n'

lineInterest = pingResult[pingResult.find('Minimum'):]
pattern = re.compile(r'\d+')
result = pattern.findall(lineInterest)
print(result)
print("Min:",result[0])
print("Max:",result[1])
print("Average:",result[2])


