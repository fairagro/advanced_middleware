
from pyld import jsonld
from arctrl.arctrl import ArcInvestigation, Comment, XlsxController, JsonController
from arctrl.Json.person import ARCtrl_Person__Person_fromROCrateJsonString_Static_Z721C83C5 as person_from_string
import json


with open('person_test/organization.jsonld', 'r') as f:
    dataset = json.loads(f.read())

with open('person_test/context.jsonld', 'r') as f:
    context = json.loads(f.read())

expanded = jsonld.expand(dataset)
compacted = jsonld.compact(expanded, context)

print(json.dumps(expanded, indent=2))
print(json.dumps(compacted, indent=2))

json_str = person_from_string(json.dumps(compacted))

print(json_str)