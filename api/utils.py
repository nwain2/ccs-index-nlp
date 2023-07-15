import csv
import pickle

def compare_column_counts(file_path, column1, column2):
    """Compares the count of two columns in an excel or csv file"""
    count1 = 0
    count2 = 0
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            count1 += 1 if row[column1] else 0
            count2 += 1 if row[column2] else 0
        return count1 == count2
    
def compare_column_values(file_path, column1, column2):
    """Compares the values of two columns in an excel or csv file"""
    values1 = set()
    values2 = set()
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            values1.add(row[column1])
            values2.add(row[column2])
        return values1 == values2

def load_model(model_path):
    """Loads the given model form the given path"""
    model = None
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def main():
    file_path = "data.csv"
    column1 = "column1"
    column2 = "column2"

    if compare_column_counts(file_path, column1, column2):
        print("The two columns have the same count")
    elif compare_column_values(file_path, column1, column2):
        print("The two columns have the same values")
    else:
        print("The two columns are different")

if __name__ == "__main__":
    main()