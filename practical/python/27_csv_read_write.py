import csv

# --- Reading CSV file ---
print("Reading data.csv:")
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# --- Writing to a new CSV file ---
data_to_write = [
    ['Name', 'Age', 'Location'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'San Francisco'],
    ['Bob', 22, 'Chicago']
]

with open('new_data.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_to_write)

print("\nData written to new_data.csv successfully.")
