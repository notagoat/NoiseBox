import time,socket,ssl,threading,random

def socketCreate(url,port,runtime,delay):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((url,port))
    except:
        print("Error: Could not open %s : %i" %(url,port))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    message = b"GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n"
    print("Opening socket to %s for %i in %i" %(url,runtime,delay))
    time.sleep(delay)
    s.sendall(message)
    while True:
        new = s.recv(4096)
        time.sleep(runtime)
        s.close()
        print("Socket closed")
        break

def threadController(threadcount):
    websitelist = open("websites.txt","r")
    websites = websitelist.read().split('\n')
    websites = list(filter(None, websites))
    print(websites)
    try:
        for i in range(threadcount):
            threading.Thread(target=socketCreate,args=(random.choice(websites),443,random.randrange(5,120),random.randrange(0,20))).start()
    except:
        print("Unable to start threads")

def options():
    try:
        choice = int(input("How many threads?: "))
    except:
        print("Please enter an int between 1 and 999")
        options()
    if choice >= 1 and choice <= 999:
        threadController(choice)
    else:
        options()

def main():
    print("""
    __   _  _____  _____ _______ _______ ______   _____  _     _
    | \  | |     |   |   |______ |______ |_____] |     |  \___/
    |  \_| |_____| __|__ ______| |______ |_____] |_____| _/   \_
    """)
    print('\n')
    print("Cover your tracks, Make some noise...\n")
    options()


if __name__ == "__main__":
    main()
