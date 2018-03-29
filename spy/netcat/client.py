import sys
import socket
import getopt
import threading
import subprocess


ip              = ""
port            = 0

def usage():
    print "client.py"
    print
    print "Usage: python client.py -p port -i ip"
    print "-i --ip          ip of the server"
    print "-p --port        port of the server"
    print
    print
    print "Example:"
    print "         python client.py -p localhost -i 8080"
    print
    sys.exit(0)

# def client_domain(command, client):
#     if len(command) > 0:
#         command += '\n'
#         client.send(command)
#
#     recv_buffer = ""
#
#     while True:
#         recv = client.recv(1024)
#         print recv
#
#         if not recv:
#             print recv_buffer
#             break
#         else:
#             recv_buffer += recv
#
#     client.close()

def client_establish(ip, port):
    if not len(ip):
        ip = "localhost"
    server_address = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    print 'Connecting to server %s port %s' % server_address

    while True:
        command = raw_input("command:")

        if len(command) > 0:
            command += '\n'
            client.send(command)

        recv = client.recv(1024)
        print recv

        # client_thread = threading.Thread(target=client_domain, args=(command,client))
        # client_thread.start()

def main():
    global ip
    global port

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:p:", ["help", "ip", "port"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-i", "--ip"):
            ip = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False,"Unhandled Option"

    client_establish(ip, port)

if __name__ == "__main__":
    main()

