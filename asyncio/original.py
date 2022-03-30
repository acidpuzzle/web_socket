import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 5000))
server_socket.listen()


while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept()
    print('Connectiom from "addr": {}'.format(addr))

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)
        print('request contain: {}'.format(request))
        if not request:
            break
        else:
            response = b'\nHELLO WORLD \n'
            client_socket.send(response)
    print('Outside inner While loop.')
    client_socket.close()
