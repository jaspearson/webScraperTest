from classes.walmartScraper import Walmart
import json

# Get Presidents day deals
extracted_records = Walmart().get_deals('kitten')

# Save results to a json file
with open('products.json', 'w') as outfile:
    json.dump(extracted_records, outfile, indent=4)
