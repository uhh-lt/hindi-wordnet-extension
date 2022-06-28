# Enriching Hindi WordNet using Knowledge Graph Completion Approaches

Sushil Awale, and Abhik Jana, Enriching Hindi WordNet Using Knowledge Graph Completion Approach,  In Proceedings of the Workshop on Resources and Technologies for Indigenous, Endangered and Lesser-resourced Languages in Eurasia (EURALI), 2022. [pdf](http://www.lrec-conf.org/proceedings/lrec2022/workshops/EURALI/pdf/2022.eurali-1.13.pdf)

[Hindi WordNet data](https://www.cfilt.iitb.ac.in/wordnet/webhwn/wn.php)

## Files

* `parse.py` - Converts the Hindi WordNet data to create a JSON-wrapped data
* `statistics.py` - Displays the WordNet statistics such as synsets per relation
* `convert_to_triples.py` - Convert the JSON-wrapped data to RDF-style triples (Graph format)
* `clean_triples.py` - Remove test leakage
