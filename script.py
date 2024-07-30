import json

# Opening JSON file
f = open('payload.json')

# returns JSON object as 
data = json.load(f)

dataPoints = data["ScopeMetrics"][0]["Metrics"][0]['Data']['DataPoints'][0]

scale = dataPoints["Scale"]
offset = dataPoints['PositiveBucket']['Offset']
bucketCounts = dataPoints['PositiveBucket']['Counts']

base = 2**(2**(-scale))

print(f'{"Lower":>9}   {"Upper":>10}  Count')
for index, val in enumerate(bucketCounts):
  i = index + offset
  print(f"{base**i:9.2f} - {base**(i + 1):9.2f}: {val}")

# Closing file
f.close()
