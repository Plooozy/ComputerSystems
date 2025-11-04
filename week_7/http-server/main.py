import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print("Listening on port %s" % SERVER_PORT)

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    print(request)
    headers = request.split('\n')
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if path == '/':
        with open("beautiful_and_useless.html", "r", encoding="utf-8") as fin:
            content = fin.read()

        response_header = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html; charset=utf-8\n"
            "Connection: close\n\n"
        )
        client_socket.sendall(response_header.encode("utf-8") + content.encode("utf-8"))
        client_socket.close()


