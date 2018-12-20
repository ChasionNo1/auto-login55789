import socket


host = 'localhost'
data_payload = 128


def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print('Connecting to %s port %s'% server_address)
    sock.connect(server_address)

    try:
        message = 'test messages, this message will be echoed'
        print('Sending: %s' % message)
        message = bytes(message, encoding='utf-8')
        sock.sendall(message)
        data = sock.recv(data_payload)
        data = str(data, encoding='utf-8')
        print('Received: %s' % data)
    except socket.error as e:
        print('socket error: %s' % str(e))
    except Exception as e:
        print('Other error happened: %s' % str(e))
    finally:
        print('Closing connection to the server')
        sock.close()


if __name__ == '__main__':
    echo_client(1234)
