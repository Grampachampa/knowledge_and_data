import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef

input_csv_file = 'temp.csv'

with open(input_csv_file, mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

g = Graph()

tr = Namespace("http://example.org/")
rdf_type = RDF.type
for row in data[1:]:
    print(row)
    #Train stations
    subject_uri = tr[row[4]].replace(" ", "_")  # Assuming the first column is the subject identifier
    predicate_uri = tr['hasName']  # Replace with your desired predicate
    object_literal = Literal(row[4])  # Assuming the second column is the object
    g.add((URIRef(subject_uri), rdf_type, tr['trainStation']))
    g.add((URIRef(subject_uri), predicate_uri, object_literal))
    #Companies
    subject_uri = tr[row[1]].replace(" ", "_") # Assuming the first column is the subject identifier
    predicate_uri = tr['hasName']  # Replace with your desired predicate
    object_literal = Literal(row[1])  # Assuming the second column is the object
    g.add((URIRef(subject_uri), rdf_type, tr['Company']))
    g.add((URIRef(subject_uri), predicate_uri, object_literal))

    

output_turtle_file = 'temp2.ttl'
g.serialize(destination=output_turtle_file, format='turtle')
