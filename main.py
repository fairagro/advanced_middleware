from arctrl.arctrl import ArcInvestigation, Comment, XlsxController, JsonController
from fsspreadsheet.xlsx import Xlsx
from rdflib import Graph, URIRef
from pyld import jsonld
import json


with open('dataset.json', 'r') as f:
    dataset = json.loads(f.read())

with open('context.json', 'r') as f:
    context = json.loads(f.read())

expanded = jsonld.expand(dataset)
compacted = jsonld.compact(expanded, context)

print(json.dumps(expanded, indent=2))
print(json.dumps(compacted, indent=2))

# mapping = {
#     "Identifier": "identifier",
#     "Title": "name",
#     "Description": "description",
#     "SubmissionDate": "dateCreated",
#     "PublicReleaseDate": "datePublished"
# }

# def extractValues(graph, key):
#     triples = graph.triples((None, URIRef("https://schema.org/" + mapping[key]), None))
#     values = [t[2].toPython() for t in triples]
#     return values

# # Load the JSON-LD file into the graph
# with open('dataset.json', 'r') as f:
#     data = f.read()
#     # Create an RDF graph
#     g = Graph().parse(data=data, format='json-ld')

#     investigation = ArcInvestigation.init("schema.org example")
#     investigation.Identifier = extractValues(g, "Identifier")
#     investigation.Title = extractValues(g, "Title")

#     # arc = JsonController.Investigation().from_json_string(data)
#     # json_str = JsonController.Investigation().to_json_string(arc)

#     json_str = JsonController.Investigation().to_json_string(investigation)

#     print(json_str)
