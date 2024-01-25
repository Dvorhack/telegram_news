

def send_to_telegram(msg):
    try:
        import socket
        io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        io.connect(('telegram_api',7878))
        io.send(msg)
        io.close()
    except Exception as e:
        print('ERROR', e)