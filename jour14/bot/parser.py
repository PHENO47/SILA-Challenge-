from bs4 import BeautifulSoup
import pandas as pd
import re

def parse_data(html):

    soup = BeautifulSoup(html, "html.parser")

    items = []

    # Recherche de produits potentiels
    for element in soup.find_all(["article", "div", "li"]):

        text = element.get_text(" ", strip=True)

        if len(text) < 20:
            continue

        # Recherche prix
        price_match = re.search(r'(\$|€|£)?\s?\d+[.,]?\d*', text)

        title = element.find(["h1","h2","h3","h4"])

        link = element.find("a")

        if title and price_match:

            items.append({

                "title": title.get_text(strip=True),
                "price": price_match.group(),
                "link": link["href"] if link and link.has_attr("href") else None

            })

    df = pd.DataFrame(items)

    return df