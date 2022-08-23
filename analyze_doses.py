import csv


def minimum(tuple_list):
    """Takes the list of dates and vaccinations and returns the date with the fewest
    vaccinations and the total number of vaccinations administered on that date."""
    dose_list = []
    date = ''
    min_value = 0
    for element in tuple_list:
        dose_list.append(int(element[1])) # append all doses into one list
        min_value = min(dose_list)
        if min_value in element or str(min_value) in element: # find the date which matches the min_value
            date = element[0]
    return date, min_value


def maximum(tuple_list):
    """Takes the list of dates and vaccinations and returns the date with the most
    vaccinations and the total number of vaccinations administered on that date."""
    dose_list = []
    date = ''
    max_value = 0
    for element in tuple_list:
        dose_list.append(int(element[1])) # append all doses into one list
        max_value = max(dose_list)
        if max_value in element or str(max_value) in element: # find which date matches max_value
            date = element[0]
    return date, max_value


def total_vaccinations(tuple_list):
    """Sums the number of vaccine doses delivered by different
locations on the same date to get a total number of vaccinations from given list."""
    dose_list = []
    total_vaccines = 0
    for element in tuple_list:
        dose_list.append(int(element[1])) # append all doses into one list
        total_vaccines = sum(dose_list)
    return total_vaccines


def main():
    with open('doses.csv', 'r') as infile, open('vaccine_stats.txt', 'w') as outfile:
        reader = csv.reader('doses.csv')
        list_of_tuples = []
        for row in infile:
            stripped_row = row.strip('\n').split(',')
            list_of_tuples.append(tuple(stripped_row))

        print('Total doses: {}\nMinimum date: {}, Doses: {}\nMaximum date: {}, Doses: {}'.format(
            total_vaccinations(list_of_tuples), minimum(list_of_tuples)[0], minimum(list_of_tuples)[1],
            maximum(list_of_tuples)[0], maximum(list_of_tuples)[1]))

        # write to outfile
        outfile.write('Total doses: {}\nMinimum date: {}, Doses: {}\nMaximum date: {}, Doses: {}\n'.format(
            total_vaccinations(list_of_tuples), minimum(list_of_tuples)[0], minimum(list_of_tuples)[1],
            maximum(list_of_tuples)[0], maximum(list_of_tuples)[1]))


main()
