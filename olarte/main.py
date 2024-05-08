import csv
from datetime import datetime
from os import path

from olarte.core.graph import load_graph

CSV_FILE = path.join('data', 'cutting_tools.csv')
OUTPUT_DIR = path.join('output')

def main():
  with open(CSV_FILE, 'r') as csvfp:
    csvdict = csv.DictReader(csvfp)
    g = load_graph(csvdict)

    current_datetime = datetime.now().isoformat()
    g.serialize(
      destination=path.join(OUTPUT_DIR, current_datetime + '.nt'),
      format='ntriples'
    )
    # g.serialize(
    #   destination=path.join(OUTPUT_DIR, current_datetime + '.ttl'),
    #   format='turtle'
    # )
    # g.serialize(
    #   destination=path.join(OUTPUT_DIR, current_datetime + '.xml'),
    #   format='xml'
    # )

if __name__ == "__main__":
  main()
