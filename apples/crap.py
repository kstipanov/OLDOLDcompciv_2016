import requests

for x in range(1, 100):
	url = "http://en.wikipedia.org/wiki/" + str(x)
	resp = requests.get(url)
	print("Status code is", resp.status_code, url)