import netmiko

session = netmiko.ConnectHandler(device_type='cisco_ios', host='10.10.20.48', username='developer', password='C1sco12345')

session.enable()
output = session.send_command('show running-config')

with open('/Users/yuinagak/git-running-config/router_Cisco', mode='w') as f:
    f.write(output)