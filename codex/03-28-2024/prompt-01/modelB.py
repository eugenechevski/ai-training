import requests
from bs4 import BeautifulSoup

def scrape_elon_musks_x_posts(url="https://twitter.com/elonmusk", num_posts=5):
    """Scrapes the last num_posts from Elon Musk's X profile."""
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}  # Adding headers to mimic browser request.

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', class_='css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
        
        for post in posts[:num_posts]:
            # Extracting text content from the post, you might need to adjust the class names based on X's HTML structure.
            text_content = post.find('div', class_='css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0').find('span').text
            print(text_content)
            print('-' * 20)
    else:
        print("Failed to retrieve the page.")

if __name__ == "__main__":
    scrape_elon_musks_x_posts()