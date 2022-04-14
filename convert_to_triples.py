'''
    Convert WordNet to RDF triples in the form (subject, predicate, object) 
        subject & object - entities
        predicate - relation between entities
    Remove near-duplicate and inverse relations
'''

import json
import csv


from sklearn.model_selection import train_test_split


wordnet = json.load(open("wordnet.json","r"))
word2idx = json.load(open("indices/word2idx.json","r"))
relation_map = relation_map = json.load(open("indices/relations.json","r"))


# Inverse relations
relations_to_remove = [
    '_holonym','_hyponym'
]


def relation_mapper(id):

    relation = relation_map[id[-2:]].lower()

    if relation.endswith("verb"):
        return "verb"
    elif relation.startswith("anto"):
        return "antonym"
    elif relation.startswith("grad"):
        return "gradation"
    elif relation.startswith("mero"):
        return "meronym"
    elif relation.startswith("holo"):
        return "holonym"
    else:
        return relation


def convert_to_triples(wordnet):
    
    triples = []
    
    for synset_id, synset in wordnet.items():
        for other_synset_id, relation_id in synset['relation_with'].items():
            try:
                x = wordnet[other_synset_id]
                triples.append((synset_id, '_' + relation_mapper(relation_id), other_synset_id))
            except KeyError:
                print("Synset " + other_synset_id + " not found. Skipping...")
    return triples


def write_to_file(data, filename):
    path = "data/openke/"
    with open(path+filename,"w+", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


triples = convert_to_triples(wordnet)
_triples = [(e1, r, e2) for (e1, r, e2) in triples if r not in relations_to_remove]

train, valid = train_test_split(_triples, test_size=0.1, random_state=22, shuffle=True)
valid, test = train_test_split(valid, test_size=0.5, random_state=22, shuffle=True)

write_to_file(train, "train.csv")
write_to_file(valid, "valid.csv")
write_to_file(test, "test.csv")



