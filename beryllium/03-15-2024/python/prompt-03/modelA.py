import os
import requests
from bs4 import BeautifulSoup


def download_latest_xkcd_comic():
    # Check if the directory exists
    comic_dir = './xkcd_comics/'
    if not os.path.exists(comic_dir):
        os.makedirs(comic_dir)

    try:
        # Fetch the XKCD home page's HTML
        response = requests.get('https://xkcd.com/')
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the URL of the latest comic image
        comic_img_link = soup.find('img', class_='comic')['src']

        # Download the comic image
        print(f"Downloading {comic_img_link}")
        comic_img = requests.get(comic_img_link)
        comic_img.raise_for_status()

        # Save the image to the specified directory
        with open(os.path.join(comic_dir, f'comic_{str(int(comic_img_link.split("/")[-1]))}.png'), 'wb') as image_file:
            image_file.write(comic_img.content)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading comic: {e}")


if __name__ == "__main__":
    download_latest_xkcd_comic()
