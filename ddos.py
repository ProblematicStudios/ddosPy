from faker import Faker
ip = Faker()
ipv4 = ip.ipv4()
ipv6 = ip.ipv6()
ipType = input("IPv4 or IPv6? ")
if ipType == 'IPv4':
  print("IP found, ipv4 is ",ipv4)

else:
  print("IP found, ipv6 is ",ipv6)
