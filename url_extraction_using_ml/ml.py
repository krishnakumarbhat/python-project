import pandas as pd

# Expanded list of keywords related to ML and AI
keywords = [
    'ml', 'ai', 'deep learning', 'artificial intelligence', 'machine learning',
   
]

def contains_keywords(url, keywords):
    """
    Check if the URL contains any of the specified keywords.
    """
    return any(keyword in url.lower() for keyword in keywords)

def filter_urls_by_keywords(input_csv, output_csv, keywords):
    try:
        # Attempt to read the CSV file with UTF-8 encoding
        data = pd.read_csv(input_csv, encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to a different encoding if UTF-8 fails
        print("UTF-8 decoding failed. Trying 'latin1' encoding.")
        data = pd.read_csv(input_csv, encoding='latin1')
    
    # Ensure the URL column exists
    if 'URL' not in data.columns:
        raise ValueError("Input CSV must contain a 'url' column")

    # Filter rows where the URL contains any of the keywords
    data['contains_keywords'] = data['URL'].apply(lambda x: contains_keywords(x, keywords))
    
    # Filter for URLs containing keywords
    filtered_urls = data[data['contains_keywords']]

    # Save the result to the output CSV file
    filtered_urls.to_csv(output_csv, index=False)

    print(f"Filtered data saved to {output_csv}")

# Run the filtering function
filter_urls_by_keywords('new_link.csv', 'yt.csv', keywords)
