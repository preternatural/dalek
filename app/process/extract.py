"""Extract named entities from a doc at a url.

   (C) 2013 Dalek Labs
"""
from app.process.entities import EntityExtractor
from app.process.fetcher import Fetcher


def main():
    extractor = EntityExtractor()
    fetcher = Fetcher()
    url = "http://www.guardian.co.uk/world/2013/jun/23/edward-snowden-gchq"
    text = fetcher.fetch_text_from_url(url)
    entities = extractor.extract_named_entities(text)
    print text
    print entities


if __name__ == "__main__":
    main()
