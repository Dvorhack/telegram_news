from scripts.utils import send_to_telegram
import time, requests, xxhash, string
from bs4 import BeautifulSoup

def synacktiv_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('article').find('h2').find('span').text
    name = ''.join(filter(lambda x: x in printable, first_article))
    
    return name

def ruia_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('article').find('a')
    
    name = first_article.find('h2').text + ': ' + first_article.find('h3').text
    name = ''.join(filter(lambda x: x in printable, name))
    
    return name

def quarkslab_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('div', {'class':'article'}).find('h1').find('a').text
    name = ''.join(filter(lambda x: x in printable, first_article))
    return name

def organizers_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('td').find('a').text
    name = 'Writeup: ' + ''.join(filter(lambda x: x in printable, first_article))

    return name

def c99_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('article').find('a').text
    name = 'Writeup: ' + ''.join(filter(lambda x: x in printable, first_article))
    return name


def kalmarunionen_parser(req_content):
    soup = BeautifulSoup(req_content, 'html5lib')
    printable = set(string.printable)

    first_article = soup.find('li').find('h3').find('a').text
    name =  ''.join(filter(lambda x: x in printable, first_article))
    return name

def default_parser(req_content):
    return xxhash.xxh64(req_content).hexdigest()

def event_watcher():
    
    SITES = {
        'https://www.synacktiv.com/publications': synacktiv_parser,
        'https://ruia-ruia.github.io/posts/': ruia_parser,
        'https://blog.quarkslab.com/': quarkslab_parser,
        'https://org.anize.rs/writeups/': organizers_parser,
        'https://chovid99.github.io/posts/': c99_parser,
        'https://www.kalmarunionen.dk/categories/writeups/': kalmarunionen_parser,
    }

    last_page = {s: [p, ''] for s,p in SITES.items()}

    while True:
        for site, (parser, last_content) in last_page.items():
            try:
                r = requests.get(site)
                content = parser(r.text)
                print(content,last_content)
                if content != last_content:
                    send_to_telegram(f'[new_post] {site}: {content}'.encode())
                    last_page[site][1] = content
            except Exception as e:
                send_to_telegram(f'[page_update] Error in GET {site}: {e}'.encode())

        time.sleep(30 * 60) # Every 30 min


if __name__ == "__main__":
    event_watcher()