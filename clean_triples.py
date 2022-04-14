'''
    Remove redundant relations
'''

import csv


def write_to_file(data, filename):
    path = "data/openke/"
    with open(path+filename,"w+", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_file(filename):
    path = "data/openke/"
    with open(path+filename,"r", encoding='utf-8') as f:
        return f.read().split("\n")


train = read_file("train.csv")
valid = read_file("valid.csv")
test = read_file("test.csv")

print("Train:", len(train))
print("Valid:", len(valid))
print("Test:", len(test))


# Removing entries whose entity pairs are directly linked to train
train_e_pairs = set()

for each in train:
    e1, r, e2 = each.split(",")
    train_e_pairs.add((e1,e2))


_valid = []
for each in valid:
    e1, r, e2 = each.split(",")
    if (e1, e2) and (e2, e1) not in train_e_pairs:
        _valid.append((e1,r,e2))

print("Valid:", len(_valid))
write_to_file(_valid, "valid.csv")

_test = []
for each in test:
    e1, r, e2 = each.split(",")
    if (e1, e2) and (e2, e1) not in train_e_pairs:
        _test.append((e1,r,e2))

print("Test:", len(_test))
write_to_file(_test, "test.csv")
