import csv

filename = 'mastercsv.csv'

# Create dictionaries to store the count of formal and informal tags for each topic type
formal_counts = {'Conversational / Everyday Phrases': 0, 'Politics': 0, 'Sports': 0, 'Business': 0, 'Health & Wellness': 0, 'Food / Cuisine': 0, 'Travel': 0}
informal_counts = {'Conversational / Everyday Phrases': 0, 'Politics': 0, 'Sports': 0, 'Business': 0, 'Health & Wellness': 0, 'Food / Cuisine': 0, 'Travel': 0}

# Open the CSV file and read the data
with open(filename, 'r', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip the header row
    for row in reader:
        # Get the topic type from the 14th column
        topic_type = row[13]
        # Get the tag from the 11th column
        tag = row[10]
        # Count the tag for the corresponding topic type
        if tag == 'Formal':
            formal_counts[topic_type] += 1
        elif tag == 'Informal':
            informal_counts[topic_type] += 1

# Print the results
print("Formal Counts:")
for topic_type, count in formal_counts.items():
    print(f"{topic_type}: {count}")
print("Informal Counts:")
for topic_type, count in informal_counts.items():
    print(f"{topic_type}: {count}")