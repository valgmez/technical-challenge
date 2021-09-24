from urllib.parse import urlparse

urls = set()

with open('urls.txt') as f:
	for line in f:
		if line != "\n":
			if line not in urls:
				urls.add(line.replace('\n', ''))

hosts = set()

with open('hosts.txt') as f:
	for line in f:
		hosts.add(line.replace('\n', ''))

match = 0
unmatched = 0
host_tracker = {}

for url in urls:
	# go through all the unique urls
	if '.'.join(urlparse(url).netloc.split('.')[-2:]) in hosts:
		# if hostname part of the url matches one of hostnames, sum 1 to matches counter
		match = match + 1
		
		# check if hostname part of url is in host_trackers, if it's not, add it and 
		if '.'.join(urlparse(url).netloc.split('.')[-2:]) in host_tracker:
			host_tracker['.'.join(urlparse(url).netloc.split('.')[-2:])] += 1
		else:
			host_tracker['.'.join(urlparse(url).netloc.split('.')[-2:])] = 1

	else:
		# else if hostname part of the url doesnt match one of the hostnames, sum 1 to unmatched counter
		unmatched = unmatched + 1
		if '.'.join(urlparse(url).netloc.split('.')[-2:]) in host_tracker:
			host_tracker['.'.join(urlparse(url).netloc.split('.')[-2:])] += 1
		else:
			host_tracker['.'.join(urlparse(url).netloc.split('.')[-2:])] = 1



print(match, "url match to hostnames")
print(unmatched, "urls don't match to hostnames")

print("\n---- List of hostsnames and count of URLs ----")
for host, amount in host_tracker.items():
	print("{} | {} URLs".format(host, amount))

