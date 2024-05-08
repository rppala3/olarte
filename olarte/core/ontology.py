from rdflib import OWL, RDF, RDFS, Graph, Namespace, URIRef

ISO = Namespace('http://olarte.org/ISO:1234/')

onto = Graph()
onto.bind('iso:123', ISO)

onto.add((ISO.Concept, RDF.type, OWL.Class))
onto.add((ISO.hasParent, RDF.type, OWL.ObjectProperty))
onto.add((ISO.hasParent, RDFS.domain, ISO.Concept))
onto.add((ISO.hasParent, RDFS.range, ISO.Concept))
