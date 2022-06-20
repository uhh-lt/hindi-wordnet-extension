import numpy as np

def read_file(filename):
    with open(filename,"r", encoding='utf-8') as f:
        return f.read().split("\n")


def extract_relation(data):
    relation = []
    for d in data:
        d = d.split("\t")
        relation.append(d[1])
    return relation


one_one = read_file("../data/conve/relation-type/1-1-text.tsv")
n_one = read_file("../data/conve/relation-type/n-1-text.tsv")
n_n = read_file("../data/conve/relation-type/n-n-text.tsv")

relation_one_one = set(extract_relation(one_one))
relation_n_one = set(extract_relation(n_one))
relation_n_n = set(extract_relation(n_n))

relations = {
    'one_one': [],
    'n_one': [],
    'n_n': [],
}

hits = {
    'one_one': [],
    'n_one': [],
    'n_n': [],
}

def store_hits(relation_type):
    if rank <= 10:
        hits[relation_type].append(1.0)
    else:
        hits[relation_type].append(0.0)

with open('rank_right.csv', 'r') as f:

    for row in f.readlines():
        row = row.split(",")
        rank = int(row[0])
        relation = row[2]

        if relation in relation_one_one:
            relations['one_one'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['one_one'].append(hit)
        elif relation in relation_n_one:
            relations['n_one'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['n_one'].append(hit)
        elif relation in relation_n_n:
            relations['n_n'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['n_n'].append(hit)
        else:
            pass



with open('rank_left.csv', 'r') as f:

    for row in f.readlines():
        row = row.split(",")
        rank = int(row[3])
        relation = row[1]

        if relation in relation_one_one:
            relations['one_one'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['one_one'].append(hit)
        elif relation in relation_n_one:
            relations['n_one'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['n_one'].append(hit)
        elif relation in relation_n_n:
            relations['n_n'].append(rank)
            hit = 1.0 if rank <= 10 else 0.0
            hits['n_n'].append(hit)
        else:
            pass


print("Relation","\t MRR","\t\t Hit@10")
for relation in relations.keys():
    print("{}\t{}\t{}".format(relation, np.mean(1./np.array(relations[relation])), np.mean(hits[relation])))
