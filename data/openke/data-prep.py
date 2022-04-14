import csv


def read_file(filename):
    with open(filename,"r", encoding='utf-8') as f:
        return f.read().split("\n")


train = read_file("train.csv")
valid = read_file("valid.csv")
test = read_file("test.csv")

clean = lambda x: x.replace("\n","")

def extract_entity(data):
    entity = []
    for d in data:
        d = d.split(",")
        entity.append(d[0])
        entity.append(d[2])
    return entity

def extract_relation(data):
    relation = []
    for d in data:
        d = d.split(",")
        relation.append(d[1])
    return relation


entity = set(extract_entity(train) + extract_entity(valid) + extract_entity(test))
relation = set(extract_relation(train) + extract_relation(valid) + extract_relation(test))


entity2id = {x:i for i, x in enumerate(entity)}

with open("entity2id.txt","w+") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow([len(entity2id)])
    for x, i in entity2id.items():
        writer.writerow([x, i])


relation2id = {x:i for i, x in enumerate(relation)}

with open("relation2id.txt","w+") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow([len(relation2id)])
    for x, i in relation2id.items():
        writer.writerow([x, i])


with open("train2id.txt","w+", encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow([len(train)])
    for x in train:
        e1, r, e2 = x.split(",")
        writer.writerow([entity2id[e1], entity2id[e2], relation2id[r]])


with open("valid2id.txt","w+", encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow([len(valid)])
    for x in valid:
        e1, r, e2 = x.split(",")
        writer.writerow([entity2id[e1], entity2id[e2], relation2id[r]])


with open("test2id.txt","w+", encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow([len(test)])
    for x in test:
        e1, r, e2 = x.split(",")
        writer.writerow([entity2id[e1], entity2id[e2], relation2id[r]])
