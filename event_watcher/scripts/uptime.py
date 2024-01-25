
def event_watcher():
    from scripts.utils import send_to_telegram
    import time, requests

    SITES = [
        'https://apple.com/',
        'http://example.com/'
    ]

    while True:
        for site in SITES:
            try:
                r = requests.get(site)
                if r.status_code != 200:
                    send_to_telegram(f'[uptime] {site} -> status {r.status_code}'.encode())
            except Exception as e:
                send_to_telegram(f'[uptime] Error in GET {site}'.encode())

        time.sleep(30 * 60) # Every 30 min


if __name__ == "__main__":
    event_watcher()