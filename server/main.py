import socket

from config import HOST, PORT

if __name__ == '__main__':
	sck = None 
	try:
		sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print('[!] Failed to create socket')

	sck.bind((HOST, PORT))
	sck.listen()

	print(f'Listening on {HOST}:{PORT}')

	conn, addr = sck.accept()
	print(f'{addr} connected')

	conn.send('test'.encode('ascii'))
