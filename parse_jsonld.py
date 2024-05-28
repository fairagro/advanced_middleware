from rdflib import Graph, Namespace

# Load the JSON-LD file into the graph
with open('dataset.json', 'r') as f:
    data = f.read()
    # Create an RDF graph
    g = Graph().parse(data=data, format='json-ld')


schema_org = Namespace("https://schema.org/")

triples = g.triples((None, schema_org.datePublished, None))
dates = [t[2] for t in triples]

print(dates)