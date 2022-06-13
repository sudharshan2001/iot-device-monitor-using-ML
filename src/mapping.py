import elasticsearch
import datetime
import time

def crate_index(indexname):
    body = {
        'mapping' : { "properties": {
      "Barn [kW]": {"type": "double"},
      "Dishwasher [kW]": {"type": "double"},
      "Fridge [kW]": {"type": "double"},
      "Furnace 1 [kW]": {"type": "double"},
      "Furnace 2 [kW]": {"type": "double"},
      "Garage door [kW]": {"type": "double"},
      "Home office [kW]": {"type": "double"},
      "House overall [kW]": {"type": "double"},
      "Kitchen 12 [kW]": {"type": "double"},
      "Kitchen 14 [kW]": {"type": "double"},
      "Kitchen 38 [kW]": {"type": "double"},
      "Living room [kW]": {"type": "double"},
      "Microwave [kW]": {"type": "double"},
      "Solar [kW]": {"type": "double"},
      "Well [kW]": {"type": "double"},
      "Wine cellar [kW]": {"type": "double"},
      "gen [kW]": {"type": "double"},
      "humidity": {"type": "double"},
      "pressure": {"type": "double"},
      "temperature": {"type": "double"},
      "time": {"type": "date","format": "epoch_second"},
      "use [kW]": {"type": "double"},
            }}}

    elastic = elasticsearch.Elasticsearch("http://localhost:9200")
    elastic.indices.create(index=indexname, body=body)

