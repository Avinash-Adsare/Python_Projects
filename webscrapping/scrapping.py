import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title and paragraphs
        title = soup.title.string if soup.title else "No title found"
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        return title, paragraphs
    except Exception as e:
        return None, [f"Error: {str(e)}"]

def main():
    st.title("Web Scraping App")
    st.markdown("""
    Enter a URL to scrape its content. This app will fetch the webpage's title and extract text from all paragraphs.
    """)

    # Input for the URL
    url = st.text_input("Enter the URL:")

    if st.button("Scrape") and url:
        st.markdown("### Results:")

        # Scrape the website
        title, paragraphs = scrape_website(url)

        if title:
            st.markdown(f"**Title:** {title}")
        else:
            st.markdown("**Title:** No title found")

        st.markdown("**Content:**")
        for para in paragraphs:
            st.write(para)

if __name__ == "__main__":
    main()
