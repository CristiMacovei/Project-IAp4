import socket

from config import SERVER_HOST, SERVER_PORT

if __name__ == '__main__':
	sck = None 
	try:
		sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print('[!] Failed to create socket')
	
	print(f'Attempting to connect to {SERVER_HOST}:{SERVER_PORT}')
	sck.connect((SERVER_HOST, SERVER_PORT))

	print('Connected')

	msg = sck.recv(1024)
	print(f'Got {msg}')