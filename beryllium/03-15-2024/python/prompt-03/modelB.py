import requests
from bs4 import BeautifulSoup
import os
import shutil


def download_latest_xkcd_comic():
    # Specify the directory to save the comic image
    save_directory = 'xkcd_comics'

    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Fetch the XKCD home page
    response = requests.get('https://xkcd.com/')
    if response.status_code != 200:
        print(f"Error fetching XKCD home page: {response.status_code}")
        return

    # Parse the HTML to find the URL of the latest comic image
    soup = BeautifulSoup(response.text, 'html.parser')
    img_src = soup.find('img', {'class': 'comic'})['src']
    if not img_src:
        print("Error finding comic image URL in HTML.")
        return

    # Download the comic image
    comic_image_url = f'https://imgs.xkcd.com/comics/{img_src}'
    response = requests.get(comic_image_url)
    if response.status_code != 200:
        print(f"Error downloading comic image: {response.status_code}")
        return

    # Extract the filename and extension from the comic image URL
    filename, _ = os.path.splitext(os.path.basename(comic_image_url))

    # Save the image to the specified directory
    save_path = os.path.join(save_directory, filename)
    with open(save_path, 'wb') as f:
        f.write(response.content)

    print(f"Comic image downloaded and saved to: {save_path}")


if __name__ == "__main__":
    download_latest_xkcd_comic()
