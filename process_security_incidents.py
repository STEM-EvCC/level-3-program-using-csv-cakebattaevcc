import csv

input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

#print(data)

new_column_name = 'Status'
default_value = 'Pending'

header = data[0] + [new_column_name]
#print(data[1])

rows = [row + [default_value] for row in data[1:]]

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)