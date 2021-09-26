from urllib.parse import urlparse

urls = set()  # using a set because they don't allow duplicates

with open('urls.txt') as f:
    for line in f:
        if line != "\n":  # ignore empty lines
            # clean up the urls removing new line characters and www. as hosts don't include www.
            urls.add(line.replace('\n', '').replace('www.', ''))

hosts = set()

with open('hosts.txt') as f:
    for line in f:
        hosts.add(line.replace('\n', ''))

match = 0
unmatched = 0
host_tracker = {}  # count of how many links appear for each hostname

for url in urls:  # go through all the unique urls
    if urlparse(url).netloc in hosts:
        # if hostname part of the url matches one of hostnames, sum 1 to matches counter
        match += 1
        # check if hostname part of url is in host_trackers, if it is, sum 1, if not, then add it and set to 1
        if urlparse(url).netloc in host_tracker:
            host_tracker[urlparse(url).netloc] += 1
        else:
            host_tracker[urlparse(url).netloc] = 1

    else:
        # else if the hostname part of the url doesn't match one of the hostnames, sum 1 to unmatched counter
        unmatched += 1
        if urlparse(url).netloc in host_tracker:
            host_tracker[urlparse(url).netloc] += 1
        else:
            host_tracker[urlparse(url).netloc] = 1


print(match, "URLs match to hostnames")
print(unmatched, "URLs don't match to hostnames")

print("\n---- List of unique hostnames and count of URLs ----")
for host, amount in sorted(host_tracker.items()):
    print("{} | {} URLs".format(host, amount))
