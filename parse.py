'''
    Extract WordNet data to JSON format

    - Notes on how to interpret the data with first example

    00000001 02 11 अजन्मा:अजात:अनुत्पन्न:अनुद्भूत:अप्रादुर्भूत:अज:अजन:अजन्म:अनन्यभव:अनागत:अयोनि 0005 2224 0000 00000008 2224 0000 00000008 2224 0000 00000008 2111 00000047 0400 00000101 | जिसने जन्म न लिया हो:"देवकी के अजन्मे बालकों के विषय में भविष्यवाणी हुई थी ।"

    synset_id synset_category synset_size synsets relation_size [relation_type other_synset_id] | sense:example

    - Breakdown of relation_type

    first_digit -> category of head word
    second_digit -> category of relation word
    last_two_digits -> relation_type
'''


import re
import json


wordnet = {}

def clean(string):
    string = re.sub("\n","", string) # remove NEWLINE characters
    string = re.sub("\"","", string) # remove quatations
    return string

with open("database/data_txt","r", encoding="utf-8") as f:
    
    for line in f.readlines():
        _meta, _gloss = line.split("|")
        meta = _meta.split(" ")
        gloss = _gloss.split(":")

        sense, example = gloss[0], clean(gloss[1]) if len(gloss) > 1 else "" # if example present

        id, category, size = meta[0], meta[1], int(meta[2])

        if size > 0:
            
            synset = meta[3].split(":")

            # Parse relations
            relation_str = " ".join(meta[5:])
            matches = re.findall("([0-9]{4}) (00000*0*) ([0-9]{8})|([0-9]{4}) ([0-9]{8})", relation_str)
            matches = [(m[0], m[2]) if m[0] else (m[3], m[4]) for m in matches]
            relations = {ssid:rid for rid, ssid in matches}
            
            wordnet[id] =  {
                    "head_word": synset[0],
                    "category": category, 
                    "size": size,
                    "synset": synset,
                    "relation_with": relations,
                    "sense": sense,
                    "example": example 
                }


with open("wordnet.json", "w+", encoding="utf-8") as f:            
    json.dump(wordnet, f, indent=4, ensure_ascii=False)