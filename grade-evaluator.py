#!/usr/bin/python3
import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for row in data:
        if row['score'] < 0 or row['score'] > 100:
            print(f"Invalid score for {row['assignment']}, it must be 0-100")
            
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = 0
    tot_sum_weight = 0
    tot_form_weight = 0
    for row in data:
        total_weight += row['weight']
        if row['group'] == 'Summative':
            tot_sum_weight += row['weight']
        elif row['group'] == 'Formative':
            tot_form_weight += row['weight']

    if total_weight != 100:
        print(f"Invalid total weight, {total_weight} has to be 100")
    
    if tot_sum_weight != 40:
        print(f"Warning! the summative total weight {tot_sum_weight} should to be 40")

    if tot_form_weight != 60:
        print(f"Warning, the formative total weight: {tot_form_weight} should be 60")
            

    # TODO: c) Calculate the Final Grade and GPA
    final_grade = 0
    for row in data:
        grade = row['score'] * (row['weight'] / 100)
        final_grade += grade
    print("Your final grade is {}".format(final_grade))
    GPA = (final_grade / 100) * 5.0
    print(f"Your final GPA is {GPA}")



    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    #I am going to determine the respective 50% of summative and formative. 
    sum_score = 0
    form_score = 0
    for row in data:
        id_score = row['score'] * (row['weight'] / 100)
        if row['group'] == 'Summative':
            sum_score += id_score
        elif row['group'] == 'Formative':
            form_score += id_score

    sum_percent = (sum_score / tot_sum_weight) * 100
    form_percent = (form_score / tot_form_weight) * 100

    if sum_percent >= 50 and form_percent >=50:
        print("PASSED")
    else:
        print("FAILED")
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    #step 1: collect all the failed formative.
    failed = []
    for row in data:
        if row['group'] == 'Formative' and row['score'] < 50:
            failed.append(row)
    # step 2: filter the result
    if failed:
        #find the highest weight among the failed formatives.
        highest = 0
        for row in failed:
            if row['weight'] > highest:
                highest = row['weight']

        #display the assignment with the highest weight(for ties)
        resubmit = []
        for row in failed:
            if row['weight'] == highest:
                resubmit.append(row)

        print("Eligible for resubmission:")
        for row in resubmit:
            print(f" -{row['assignment']} (weight {row['weight']})")
    else:
        print("No formative assignment failed. No resubmission")



    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options

    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)

