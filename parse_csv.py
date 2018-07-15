import csv

with open('/Users/michaelgregoire/postPrimeProjects/python_csv/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # next(csv_reader)
    with open('/Users/michaelgregoire/postPrimeProjects/python_csv/new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter='\t')
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
