from scapy.all import traceroute

target = 'google.com'
resutl, _ = traceroute(target)