import csv

input_file = 'services-2022.csv'
output_file = 'temp.csv'

columns_to_remove = [0, 4, 2, 5, 6, 7, 11, 13, 14, 15, 16]  # List of column indices to remove

with open(input_file, mode='r') as in_file, open(output_file, mode='w', newline='') as out_file:
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)
    
    for row in reader:
        # Create a new row with the specified columns removed
        new_row = [value for i, value in enumerate(row) if i not in columns_to_remove]
        writer.writerow(new_row)
        

print("Done")