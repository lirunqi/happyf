import re

league_urls = '/competition.do?lid=5&sid=2022&pid=23&lang=tr'   # /resultschedule.do?lid=5&sid=2022&lang=tr

lid = re.search(r'lid=(\d+)', league_urls).group(1)
sid = re.search(r'sid=(\d+)', league_urls).group(1)
pid = re.search(r'pid=(\d+)', league_urls).group(1)

print("/resultschedule.do?lid="+lid+"&sid="+sid+"&lang=hanz")


for i in range(4,7):
    print(i)