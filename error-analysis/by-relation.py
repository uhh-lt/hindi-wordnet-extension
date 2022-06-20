import numpy as np

relations = {}
hits = {}


with open('rank_right.csv', 'r') as f:
    for row in f.readlines():
        row = row.split(",")
        relations[row[2]] = []
        hits[row[2]] = []


with open('rank_right.csv', 'r') as f:

    for row in f.readlines():
        row = row.split(",")
        rank = int(row[0])
        relation = row[2]
        relations[relation].append(rank)

        if rank <= 10:
            hits[relation].append(1.0)
        else:
            hits[relation].append(0.0)


with open('rank_left.csv', 'r') as f:

    for row in f.readlines():
        row = row.split(",")
        rank = int(row[3])
        relation = row[1]
        relations[relation].append(rank)

        if rank <= 10:
            hits[relation].append(1.0)
        else:
            hits[relation].append(0.0)


print("Relation","\t MRR","\t\t\t Hit@10")
for relation in relations.keys():
    print("{}\t{}\t{}".format(relation, np.mean(1./np.array(relations[relation])), np.mean(hits[relation])))
