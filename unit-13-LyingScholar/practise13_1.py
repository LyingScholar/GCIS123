import csv

def find_streets(filename, street_name):
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            found_streets = []
            for row in csv_reader:
                if row[0].lower() == street_name.lower():
                    street = row[0]
                    street_type = row[1]
                    post_direction = row[2]
                    full_street_name = street + ' ' + street_type + ' ' + post_direction
                    found_streets.append(full_street_name)

            for street in found_streets:
                print(street)
            else:
                print("No streets found.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")


def find_most_popular_street(filename):
    street_count = {}

    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row

            for row in csv_reader:
                street_name = row[0]
                if street_name in street_count:
                    street_count[street_name] += 1
                else:
                    street_count[street_name] = 1

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return
            
    most_common_street = []
    max_count = 0
    
    for street, count in street_count.items():
        if count > max_count:
            most_common_street = [street]
            max_count = count
        elif count == max_count:
            most_common_street.append(street)

    return most_common_street