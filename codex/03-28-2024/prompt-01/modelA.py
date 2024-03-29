import requests
from bs4 import BeautifulSoup

def get_last_five_tweets(url):
  """Scrapes the last 5 tweets from the given Twitter URL using Beautifulsoup

  Args:
      url: The URL of the Twitter account to scrape

  Returns:
      A list of dictionaries, where each dictionary contains the text of the tweet
      and the URL of the tweet.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  tweets = []
  # Find all tweet containers
  tweet_containers = soup.find_all('div', attrs={'class': 'css-1dbjc4n R-lefamR'})

  # Extract tweet text and URL for the last 5 tweets
  for container in tweet_containers[:5]:
    tweet_text = container.find('div', attrs={'class': 'css-901oao css-16my40l R-poilbo R-bcqeeo'}).text.strip()
    tweet_url = f"https://twitter.com{container.find('a', attrs={'href': True})['href']}"
    tweets.append({"text": tweet_text, "url": tweet_url})
  
  return tweets

# Example usage: Replace with Elon Musk's Twitter URL
url = "https://twitter.com/elonmusk"

last_five_tweets = get_last_five_tweets(url)

# Print the last 5 tweets
for tweet in last_five_tweets:
  print(f"Tweet Text: {tweet['text']}")
  print(f"Tweet URL: {tweet['url']}")
  print("---")
