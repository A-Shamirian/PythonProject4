#Assignment 3: Annie Shamirian (251103387)

import csv

def count_doses_by_date(list):
    """This function takes the vaccine dictionary and its date and returns the total number of vaccine doses
    administered on that day."""
    int_list = []
    for element in list:
        if element.isdigit():
            int_list.append(int(element)) # append numbers in list to int_list
        elif ',' in element:
            number = str(element)
            number = number.replace(',', '')
            int_list.append(int(number)) # append numbers without comma separators (e.g. 1,000 -> 1000)
    total_doses = sum(int_list)
    return total_doses


def main():
    with open('doses_data_mar_20.csv', 'r') as infile, open('doses.csv', 'w') as outfile:
        user_input = input('Which data would you like to consider?\n')  # prompt user to choose csv file
        if user_input == 'doses_data_mar_20.csv':
            reader = csv.reader(infile)  # pass the header
            next(reader, None)
            d_doses = {}
            for line in reader:
                value_list = line
                if value_list[0] in d_doses:
                    d_doses[value_list[0]].extend(value_list[1:-1]) # if duplicate dates exist, list all vaccines under one date
                else:
                    d_doses[value_list[0]] = value_list[1:-1] # otherwise, append without including empty string

            # write to outfile
            for key in d_doses:
                vaccines = d_doses.get(key)
                outfile.write('{},{}\n'.format(key, count_doses_by_date(vaccines)))
                print('Date: {}\nDoses: {}'.format(key, d_doses.get(key)))


main()
