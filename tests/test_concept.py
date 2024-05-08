import csv
import unittest
from datetime import datetime
from os import path

from olarte.core.graph import load_graph

CURRENT_DIR = path.dirname(__file__)
FILES_DIR = path.join(CURRENT_DIR, 'files')
OUTPUT_DIR = path.join(CURRENT_DIR, 'out')

class TestConcept(unittest.TestCase):

  def test_shortlist01(self):
    CSV_FILE = path.join(FILES_DIR, 'cutting_tools_short01.csv')
    with open(CSV_FILE, 'r' ) as csvfp:
      csvdict = csv.DictReader(csvfp)
      g = load_graph(csvdict)

      current_datetime = datetime.now().isoformat()
      g.serialize(
        destination=path.join(OUTPUT_DIR, current_datetime + '.nt'),
        format='ntriples'
      )
      g.serialize(
        destination=path.join(OUTPUT_DIR, current_datetime + '.ttl'),
        format='turtle'
      )

  def test_shortlist02(self):
    CSV_FILE = path.join(FILES_DIR, 'cutting_tools_short02.csv')
    with open(CSV_FILE, 'r' ) as csvfp:
      csvdict = csv.DictReader(csvfp)
      g = load_graph(csvdict)

      current_datetime = datetime.now().isoformat()
      g.serialize(
        destination=path.join(OUTPUT_DIR, current_datetime + '.nt'),
        format='ntriples'
      )
      g.serialize(
        destination=path.join(OUTPUT_DIR, current_datetime + '.ttl'),
        format='turtle'
      )
