'''
    Statistics from the data
'''


import json


relation_map = json.load(open("indices/relations.json","r"))
category_map = json.load(open("indices/category.json","r"))
vocab = json.load(open("indices/idx2word.json","r"))
wordnet = json.load(open("wordnet.json","r"))


print("Total synsets: ", len(wordnet))
print("Total relations: ", len(relation_map))
print("Total unique words: ", len(vocab))


words = [w for _,x in wordnet.items() for w in x['synset']]
print("Total words: ", len(words))


relation_count = {id:0 for id,_ in relation_map.items()}
for _, synset in wordnet.items():
    for relation_id in synset["relation_with"].values():
        relation_count[relation_id[-2:]] += 1


print("Total synset relations for each relation")
for id, c in relation_count.items():
    print(relation_map[id], c)

