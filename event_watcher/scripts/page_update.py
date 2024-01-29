
def event_watcher_no():
    from scripts.utils import send_to_telegram
    import time, requests, xxhash
    
    SITES = [
        'https://ruia-ruia.github.io/posts/',
        'https://www.synacktiv.com/publications/',
    ]

    last_page = {s: '' for s in SITES}

    while True:
        for site in SITES:
            try:
                r = requests.get(site)
                the_hash = xxhash.xxh64(r.text).hexdigest()
                print(site,the_hash)
                if the_hash != last_page[site]:
                    send_to_telegram(f'[page_update] {site}'.encode())
                    last_page[site] = the_hash
            except Exception as e:
                send_to_telegram(f'[page_update] Error in GET {site}: {e}'.encode())

        time.sleep(30 * 60) # Every 30 min


if __name__ == "__main__":
    event_watcher()