
hit = input("Enter k for hit@k: ")

print("Hit@{} examples right \n".format(hit))

with open('rank_right.csv', 'r') as f:
    for row in f.readlines():
        row = row.split(",")
        rank = int(row[0])
        if rank > int(hit):
            print(row[1:])


print("\n Hit@{} examples left \n".format(hit))

with open('rank_left.csv', 'r') as f:
    for row in f.readlines():
        row = row.split(",")
        rank = int(row[3])
        if rank > int(hit):
            print(row[:3])
