import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.1', 139))

# Receive the file data from the server
file_data = client_socket.recv(1024)

# Write the file data to a file
with open("received_file.txt", "wb") as f:
    f.write(file_data)

# Close the socket
client_socket.close()
