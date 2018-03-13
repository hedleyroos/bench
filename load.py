import threading
import time

import requests


HOST = "http://127.0.0.1"
#HOST = "http://aerie"
PORTS = [9011, 9012, 9014]
NUM = 100

def worker(num):
    for i in range(5):
        for port in PORTS:
            response = requests.get("%s:%s" % (HOST, port))


start = time.time()

threads = []
for i in range(NUM / 5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

print "Requests per second = %s" % (NUM * len(PORTS) / (end - start))
