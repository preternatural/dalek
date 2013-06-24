"""Class to extract named entities from text.

   Jeff Reynar, 2013
"""
import nltk

CHUNKER_DATA_FILE = 'chunkers/maxent_ne_chunker/english_ace_binary.pickle'
TAGGER_DATA_FILE = 'taggers/maxent_treebank_pos_tagger/english.pickle'
TOKENIZER_DATA_FILE = 'tokenizers/punkt/english.pickle'

class EntityExtractor(object):
    def __init__(self,
                 tagger_data=TAGGER_DATA_FILE,
                 tokenizer_data=TOKENIZER_DATA_FILE,
                 chunker_data=CHUNKER_DATA_FILE):
        self.tagger = nltk.data.load(tagger_data)
        self.tokenizer = nltk.data.load(tokenizer_data)
        self.chunker = nltk.data.load(chunker_data)

    # https://gist.github.com/322906/90dea659c04570757cccf0ce1e6d26c9d06f9283
    def extract_entities_from_tree(self, tree):
        """Returns all the nodes tagged as named entities from the tree"""
        entity_names = []
        if hasattr(tree, 'node') and tree.node:
            if tree.node == 'NE':
                entity_names.append(' '.join([child[0] for child in tree]))
            else:
                for child in tree:
                    entity_names.extend(self.extract_entities_from_tree(child))
        return entity_names

    def chunk(self, text):
        """Chunk text and return NLTK data stucture."""
        sentences = self.tokenizer.tokenize(text)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence
                               in sentences]
        tagged_sentences = [self.tagger.tag(sentence) for sentence
                            in tokenized_sentences]
        return self.chunker.batch_parse(tagged_sentences)

    def extract_named_entities(self, text):
        chunked = self.chunk(text)
        named_entities = nltk.FreqDist()
        for sentence in chunked:
            named_entities.update(self.extract_entities_from_tree(sentence))
        return named_entities
