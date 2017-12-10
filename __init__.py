'''
Created on Dec 9, 2017

@author: prosaiccode
'''
import socket, time

def internet(host="8.8.8.8", port=53, timeout=5):
    socket.setdefaulttimeout(timeout)
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True, 
    except Exception:
        return False

def test():
    pre, now = None, None
    while True:
        now = internet()
        if now != pre:
            ct = time.localtime()
            pre = now
            if now:
                log(True, ct)
            else:
                log(False, ct)
        time.sleep(10)
        
def log(b, t):
    a = None
    if b:
        a = "Connected"
    else:
        a = "Disconnected"
    with open("connection.log", "a+") as f:
        f.write("{:4}-{:02}-{:02} {:02}:{:02}\t{}\n".format(t[0], t[1], t[2], t[3], t[4], a))

if __name__ == "__main__":
    test()
