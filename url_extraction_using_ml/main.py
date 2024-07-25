import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse, parse_qs

def extract_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        link_data = []
        for link in links:
            name = link.get_text(strip=True)
            url = link['href']
            if 'youtube.com' in url:
                query = parse_qs(urlparse(url).query)
                if 'v' in query:
                    video_id = query['v'][0]
                    name = f"YouTube Video {video_id}"
            link_data.append({"Name": name, "URL": url})
        return link_data
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

def save_links_to_csv(link_data, filename='links.csv'):
    df = pd.DataFrame(link_data)
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
    print(f"Links saved to {filename}")

if __name__ == "__main__":
    urls = []
    for i in range(13):
        url = input(f"Enter URL {i+1}: ")
        urls.append(url)
    
    all_links = []
    for url in urls:
        links = extract_links(url)
        all_links.extend(links)
    
    if all_links:
        save_links_to_csv(all_links)
