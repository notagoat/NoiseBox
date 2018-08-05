import time,socket, ssl, threading

def socketCreate(url,port,delay):
    print("Opening socket to %s" %url)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url,port))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    message = b"GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n"
    s.sendall(message)
    print("Socket Open!")
    while True:
        new = s.recv(4096)
        time.sleep(delay)
        s.close()
        print("Socket closed")
        break

def threadController(threadcount):
    try:
        for i in range(threadcount):
            threading.Thread(target=socketCreate,args= ("github.com",443,10)).start()
    except:
        print("Unable to start threads")

def main():
    threadController(10)


if __name__ == "__main__":
    main()
