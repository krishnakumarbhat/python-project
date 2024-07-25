import pandas as pd
import re

def extract_uri(link):
    if isinstance(link, str):
        # Use regex to find the part after 'uri='
        match = re.search(r'uri=(.*)', link)
        if match:
            # Return the part after 'uri='
            return match.group(1)
    return link

def process_links(input_filename, output_filename):
    # Read the CSV file with specified encoding
    df = pd.read_csv(input_filename, encoding='ISO-8859-1')
    
    # Check if 'URL' column exists
    if 'URL' in df.columns:
        # Process each link
        df['URL'] = df['URL'].apply(extract_uri)
        
        # Save the cleaned URLs to a new CSV file
        df.to_csv(output_filename, index=False)
        print(f"Processed links saved to {output_filename}")
    else:
        print("The input CSV file does not contain a 'URL' column.")

if __name__ == "__main__":
    input_filename = 'links.csv'
    output_filename = 'new_link.csv'
    process_links(input_filename, output_filename)
