"""Extract named entities from a doc at a url.

   Diffbot endpoint: http://www.diffbot.com/api/article?token=...&url=...
   Jeff Reynar, 2013
"""
from urllib2 import urlopen
import nltk

DIFFBOT_URL = "http://www.diffbot.com/api/article?token="
DIFFBOT_TOKEN = "1a1781471e3fbc194d64461eb17c8821"
TAGGER = nltk.data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
TOKENIZER = nltk.data.load('tokenizers/punkt/english.pickle')
CHUNKER = nltk.data.load(
    'chunkers/maxent_ne_chunker/english_ace_binary.pickle')


def chunk(text):
    """Chunk text and return NLTK data stucture."""
    sentences = TOKENIZER.tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence
                           in sentences]
    tagged_sentences = [TAGGER.tag(sentence) for sentence
                        in tokenized_sentences]
    return CHUNKER.batch_parse(tagged_sentences)


# https://gist.github.com/322906/90dea659c04570757cccf0ce1e6d26c9d06f9283
def extract_entity_names(tree):
    """Returns all the nodes tagged as named entities from the tree"""
    entity_names = []

    if hasattr(tree, 'node') and tree.node:
        if tree.node == 'NE':
            entity_names.append(' '.join([child[0] for child in tree]))
        else:
            for child in tree:
                entity_names.extend(extract_entity_names(child))

    return entity_names


def extract_named_entities_from_text(text):
    """Chunk text, extract named entities and return a FreqDist containing
    them."""
    chunked = chunk(text)
    named_entities = nltk.FreqDist()
    for sentence in chunked:
        named_entities.update(extract_entity_names(sentence))
    return named_entities


def fetch_text_from_url(url):
    diffbot_url = DIFFBOT_URL + DIFFBOT_TOKEN
    diffbot_url += '&url=' + url
    response = urlopen(url)
    text = response.read()
    return text

    
def main():
    # Todo(jeff): silly nyt has a redirect loop
    url = "http://www.guardian.co.uk/world/2013/jun/23/edward-snowden-gchq"
    text = fetch_text_from_url(url)
    #text = ("Rich Burdon and Jeff Reynar are meeting in Brooklyn at 9 a.m. "
    #        "They used to work at Google.")
    entities = extract_named_entities_from_text(text)
    print text
    print entities


if __name__ == "__main__":
    main()
