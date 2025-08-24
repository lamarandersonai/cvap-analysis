import csv

### What program does Analyze 4 racial groups:
# Black or African American Alone
# Asian Alone
# White Alone, Not Hispanic or Latino
# Hispanic or Latino
# Compare their percentage of total CVAP for each state
# Print a simple text graph for each group in a few states

# Load data from file
file_path = "/Users/manofactionandmystery/Documents/Data Science/Datasets/American Community Survey/2019-2023 Citizen Voting Age by Race and Ethnicity/CVAP_2019-2023_ACS_csv_files/State.csv"

# Read csv
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

# Create lists for racial groups
    total_cvap = []
    group_data = {
        "Black or African American Alone": [],
        "Asian Alone": [],
        "White Alone, Not Hispanic or Latino": [],
        "Hispanic or Latino": []
    }

# Loop through the file rows
    for row in reader:
        state = row[0]
        group = row[1]
        cvap_est = int(row[10])

        if group == "Total":
            total_cvap.append([state, cvap_est])
        else:
            if group in group_data:
                group_data[group].append([state, cvap_est])

# Function to match totals with group and compute %
def calculate_percentages(group_list, total_list):
    result = []
    for t in total_list:
        state = t[0]
        total = t[1]
        for g in group_list:
            if g[0] == state:
                percent = (g[1] / total) * 100
                result.append([state, round(percent, 2)])
    return result

# Calculate percentage lists for all groups
black_pct = calculate_percentages(group_data["Black or African American Alone"], total_cvap)
asian_pct = calculate_percentages(group_data["Asian Alone"], total_cvap)
white_pct = calculate_percentages(group_data["White Alone, Not Hispanic or Latino"], total_cvap)
hispanic_pct = calculate_percentages(group_data["Hispanic or Latino"], total_cvap)

# Function to draw a simple bar graph line
def draw_bar(state, percent):
    bar = "#" * int(percent / 2)  # 1 # = 2%
    return state + ": " + bar + " " + str(percent) + "%"

# Show bar chart for 5 selected states
states_to_show = ["California", "Texas", "Florida", "New York", "Georgia"]

print("\n\nCitizen Voting Age Population % by Race (Text Graph)\n")

print("Black or African American:")
for row in black_pct:
    if row[0] in states_to_show:
        print(draw_bar(row[0], row[1]))

print("\nAsian:")
for row in asian_pct:
    if row[0] in states_to_show:
        print(draw_bar(row[0], row[1]))

print("\nWhite (Non-Hispanic):")
for row in white_pct:
    if row[0] in states_to_show:
        print(draw_bar(row[0], row[1]))

print("\nHispanic or Latino:")
for row in hispanic_pct:
    if row[0] in states_to_show:
        print(draw_bar(row[0], row[1]))
