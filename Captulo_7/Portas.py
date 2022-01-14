import socket

print(f'{socket.getservbyname("domain")}\n'
      f'{socket.getservbyname("http")}\n'
      f'{socket.getservbyname("ftp")}')
