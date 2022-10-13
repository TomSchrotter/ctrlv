import os
import string
import random
import bs4
import requests


def ctrlv_url(size: int):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


def html():
    strings = ctrlv_url(4)
    url = f"https://www.ctrlv.link/{strings}"
    r = requests.get(url)
    return r.content


def img_search():
    src = '/images/notexists.png'
    while src == '/images/notexists.png':
        soup = bs4.BeautifulSoup(html(), 'html.parser')
        src = soup.find('img', {'class': 'outline'}).attrs['src']
    return src


def download(desktop_folder):
    img = img_search()

    file_name = img.split('/')[5]
    file_path = os.path.join(desktop_folder, file_name)
    img_data = requests.get("https://www.ctrlv.link" + img).content

    with open(file_path, 'wb') as handler:
        handler.write(img_data)


def main():
    # create "mydir" folder in the same directory as main.py if it doesn't exist
    if not os.path.exists("mydir"):
        os.makedirs("mydir")

    while True:
        download(desktop_folder="mydir")


if __name__ == '__main__':
    main()
