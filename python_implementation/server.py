import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.16.129.28', 5353))
server_socket.listen(1)

print("Waiting for client connection...")
client_socket, address = server_socket.accept()

print(f"Connection established with {address}")

# Open the file in binary mode and read its content
with open("message.aes", "rb") as f:
    file_data = f.read()

# Send the file data to the client
client_socket.send(file_data)

# Close the sockets
client_socket.close()
server_socket.close()
