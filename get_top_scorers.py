# 1st Step: Read and Parse CSV Data
def read_csv(csv_file):
    """
    This function will read a CSV file and parses it into a list of dictionaries.
    """
    csv_data = []
    with open(csv_file, 'r') as file:
        lines = file.readlines()  # Reads all the lines from the file
        headers = lines[0].strip().split(',')  # Retrieve  headers (First Name, Second Name, and Score)

        for line in lines[1:]:
            values = line.strip().split(',')  # Split up each line by a comma
            person = {
                headers[0]: values[0],  # First Name
                headers[1]: values[1],  # Second Name
                headers[2]: int(values[2])  # Score (which has been converted into an integer)
            }
            csv_data.append(person)  # This will add each person to the data list
    return csv_data

# 2nd Step: Find Top Scorers
def get_top_students(csv_data):
    """
    Finds the top scorer(s) from the parsed data.
    Returns a list of names and the top score.
    """
    highest_score = max(person['Score'] for person in csv_data)  # This will find the highest score
    top_scorers = [person for person in csv_data if person['Score'] == highest_score]  # Filters the top scorers

    # Sorts the top scorers alphabetically (by their full name)
    top_scorers.sort(key=lambda x: f"{x['First Name']} {x['Second Name']}")

    # This will retrieve names and corresponding score
    names = [f"{person['First Name']} {person['Second Name']}" for person in top_scorers]
    return names, highest_score

# 3rd Step: Output Results
def show_top_scorers(names, score):
    """
    Prints the top scorers and their score in the required format
    """
    print("\nTop Scorers:")
    for name in names:
        print(name)
    print(f"\nScore: {score}")

# Execution of functions
csv_file = 'TestData.csv'
csv_data = read_csv(csv_file)
names, top_score = get_top_students(csv_data)
show_top_scorers(names, top_score)
