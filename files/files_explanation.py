# Module to load/elaborate/tranform csv/tsv
import csv  # read/write csv / tsv and more

# r = read
# w = write
# a = append
# b = binary
# Eg. rw, wb and so on.

# This method is open a file and read all the file.
def open_file_read_all():
    path = 'eggs.csv'  # or /path/files/eggs.csv directory+file.ext
    # 'r' is the default behaviour.
    eggs_file = open(path, 'r')
    eggs_read = eggs_file.read()
    print(eggs_read)
    eggs_file.close()

# This method is open a file and read it line by line
# using while and readline(next)
def open_file_read_line_while():
    path = 'eggs.csv'  # or /path/files/eggs.csv directory+file.ext
    with open(path, 'r') as reader:
        # Read and print the entire file line by line
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            print(line, end='')
            # read next line!
            line = reader.readline()

    reader.close()

# This method is open a file and read it line by line
# For is simpler to use
def open_file(filename):
    with open(filename, 'r') as reader:
        for line in reader.readlines():
            print(line, end='')

    reader.close()

# This method is open a file and read it line by line
# For is simpler to use and split the line using "," as separator
def open_file_csv_no_module(filename):
    with open(filename, 'r') as reader:
        for line in reader.readlines():
            elem_of_line = line.split(",")
            print(elem_of_line[0])

    reader.close()


# This method uses the module CSV and read the file line by line
def open_csv(filename):
    with open(filename, newline='') as csvfile:
        # by default delimiter is comma. Tab -> delimiter = '\t'
        spam = csv.reader(csvfile)
        for row in spam:
            # To check the lenght of the number of rows
            array_len = len(row)
            if array_len >=4 : # strange csv were there is a 4th column once...
                print(row[3])

            print(row[0])

    csvfile.close()

# This method uses the module TSV and read the file line by line
def open_tsv(filename):
    with open(filename, newline='') as csvfile:
        # by default delimiter is comma. Tab -> delimiter = '\t'
        spam = csv.reader(csvfile, delimiter='\t')
        for row in spam:
            print(row[1], row[2])

    csvfile.close()

# This method uses the module CSV and read the file as dict!
def open_csv_as_dict(filename):
    with open(filename, newline='') as csvfile:
        # reader is a dict!!!!!
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Hi ",row['first_name'], row['last_name'])

    csvfile.close()


def main():
    open_file_read_all()
    open_file_read_line_while()
    open_file('eggs.csv')
    open_file_csv_no_module('eggs.csv')
    open_csv('eggs.csv')
    open_tsv('countries.tsv')
    open_csv_as_dict('names.csv')


if __name__ == "__main__":
    main()
