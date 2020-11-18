#!/usr/bin/python3 -u

if __name__ == '__main__' :
	from subprocess import run, PIPE
	import sys
	import requests, json

	print("AZK start.")

	r = run(['ip', 'address'], check=True, stdout=PIPE)

	print("AZK ips:")
	print(str(r.stdout, 'utf8'))

	r = run(['ip', 'address', 'add', '169.254.101.101/16', 'scope', 'link', 'dev', 'eth0'], check=True)
	r = run(['ip', 'link', 'set', 'eth0', 'up'], check=True)

	r = run(['ip', 'address'], check=True, stdout=PIPE)
	print("AZK ips2:")
	print(str(r.stdout, 'utf8'))

	r = requests.get('http://169.254.169.254/metadata/instance?api-version=2020-09-01',
					headers={'Metadata':'true'}, proxies = {"http": None, "https": None, })
	print("AZK json:")
	print(json.dumps(r.json(), sort_keys=True, indent=2))

	r = run(['ip', 'link', 'set', 'eth0', 'down'], check=True)
	r = run(['ip', 'address', 'del', '169.254.101.101/16', 'scope', 'link', 'dev', 'eth0'], check=True)

	r = run(['ip', 'address'], check=True, stdout=PIPE)
	print("AZK ips3:")
	print(str(r.stdout, 'utf8'))

	sys.exit(0);