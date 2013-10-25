import socket

def parsing(txt):
    txt=txt.replace('\377', '')
    if txt.find('m') == 0:
        serv_name=txt.split('\0') [1]
        serv_map=txt.split('\0') [2]
        serv_engine=txt.split('\0') [3]
        serv_game=txt.split('\0') [4]
    print 'Server name:', serv_name
    print 'Game:', serv_game, '('+serv_engine+')'
    print 'Map:', serv_map

ip='' #write server ip

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((ip, 27015))

sock.send('\377\377\377\377TSource Engine Query\0')

while 1:
    text=sock.recv(1024)
    text=parsing(text)
    if not text:
        break
    print '[GET]', text

sock.close()
