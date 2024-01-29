
"""
def event_watcher():
    from scripts.utils import send_to_telegram
    import time

    while True:
        print('Sending to telegram')
        send_to_telegram(b'Test event watcher')
        time.sleep(10*60)
"""

if __name__ == "__main__":
    event_watcher()