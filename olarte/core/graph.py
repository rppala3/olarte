from rdflib import RDF, RDFS, Graph, Literal, Namespace, URIRef

ISO = Namespace('http://olarte.org/ISO:1234/')

#
#
#
def get_concept_uri(id):
  return URIRef(id, ISO.Concept)

#
#
#
def append_concept_node(g, id, label='', parent_uri=None):
  concept_uri = get_concept_uri(id)
  g.add((concept_uri, RDF.type, ISO.Concept))
  #
  if label != '':
    g.add((concept_uri, RDFS.label, Literal(label, lang="en")))
  #
  if parent_uri is not None:
    g.add((concept_uri, ISO.hasParent, parent_uri))
  #
  return concept_uri

#
#
#
def load_graph(csvfile):
  g = Graph()
  g.bind('iso_1234', ISO)
  for line in csvfile:
    #
    parent_id = line['parentID']
    if parent_id != '':
      parent_uri = get_concept_uri(parent_id)
      if (parent_uri, None, None) not in g:
        parent_uri = append_concept_node(g, parent_id)
    else:
      parent_uri = None
    #
    concept_id = line['conceptID']
    concept_label = line['conceptLable']
    append_concept_node(g, concept_id, concept_label, parent_uri)
  return g
