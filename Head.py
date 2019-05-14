import listen as ls
import threading


def worker():
    ls.rec.recd()


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
