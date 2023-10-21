import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS

input_csv_file = 'train_data.csv'

with open(input_csv_file, mode='r') as file:
    print('opening and reading file...')
    reader = csv.reader(file)
    data = list(reader)

start_row = 1
while start_row < len(data):
    g = Graph()

    tr = Namespace("http://example.org/")
    g.bind('tr', tr)
    rdf_type = RDF.type
    rdfs_label = RDFS.label
    for row in data[start_row:start_row + 500000]:
        print(row)
        # Train stations
        subject_uri = tr[row[4]].replace(" ", "_")  # Assuming the first column is the subject identifier
        predicate_uri = tr['hasName']  # Replace with your desired predicate
        object_literal = Literal(row[4])  # Assuming the second column is the object
        g.add((URIRef(subject_uri), rdf_type, tr['trainStation']))
        g.add((URIRef(subject_uri), predicate_uri, object_literal))
        # Companies
        subject_uri = tr[row[1]].replace(" ", "_")  # Assuming the first column is the subject identifier
        predicate_uri = tr['hasName']  # Replace with your desired predicate
        object_literal = Literal(row[1])  # Assuming the second column is the object
        g.add((URIRef(subject_uri), rdf_type, tr['Company']))
        g.add((URIRef(subject_uri), predicate_uri, object_literal))

        # Station Code
        subject_uri = tr[row[3]].replace(" ", "_")  # Assuming the first column is the subject identifier
        predicate_uri = tr['hasName']  # Replace with your desired predicate
        object_literal = Literal(row[3])  # Assuming the second column is the object
        g.add((URIRef(subject_uri), rdf_type, tr['stationCode']))
        g.add((URIRef(subject_uri), predicate_uri, object_literal))

        # StationStopID
        subject_uri = tr[row[2]].replace(" ", "_")  # stationStopID
        station_code = Literal(row[3].replace(" ", "_"))  # stationCode
        station_name = Literal(row[4].replace(" ", "_"))  # stationname
        delay_minutes = tr[row[5].replace(" ", "_")]  # stationname
        company_name = Literal(row[1].replace(" ", "_"))  # companyname
        date = tr[row[0]]  # date

        g.add((URIRef(subject_uri), rdf_type, tr['stationstopID']))
        g.add((URIRef(subject_uri), rdfs_label, station_name))

        g.add((URIRef(subject_uri), tr['hasStationCode'], station_code))
        g.add((URIRef(subject_uri), tr['hasDelay'], delay_minutes))
        g.add((URIRef(subject_uri), tr['hasCompany'], company_name))
        g.add((URIRef(subject_uri), tr['hasDate'], date))

    output_turtle_file = f'train_RDF{start_row}_{start_row + 500000}.ttl'
    g.serialize(destination=output_turtle_file, format='turtle')
    print(f'adding from {start_row} row to {start_row + 500000}')
    start_row += 500000