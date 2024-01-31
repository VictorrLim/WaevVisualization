import csv
import matplotlib.pyplot as plt
from collections import Counter

def get_column_strings(csv_file, column_index):
    """
    Reads a CSV file and extracts values from a specified column.

    Args:
        csv_file (str): Path to the CSV file.
        column_index (int): Index of the column to extract values from (0-based).

    Returns:
        list: A list of strings containing the values from the specified column.
    """

    column_values = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            column_values.append(row[column_index])

    return column_values

def string_counter(string_list):
 """
 This function takes a list of strings and returns a dictionary where the keys are the unique strings in the list and the values are the number of times each string appears in the list.

 Args:
   string_list: A list of strings.

 Returns:
   A dictionary where the keys are the unique strings in the list and the values are the number of times each string appears in the list.
 """


 string_counts = Counter(string_list)


 string_dict = dict(string_counts)

 return string_dict

def top_10(data):
  """
  Returns a new dictionary with the top 10 values from the input dictionary.

  Args:
    data: A dictionary of key-value pairs.

  Returns:
    A new dictionary with the top 10 values from the input dictionary, sorted in descending order.
  """


  sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)


  return dict(sorted_data[:10])
def plot_ev_car_brands_washington(data):
  """
  Plots a bar graph of electric vehicle car brands in Washington

  Args:
    data: A dictionary containing brand names as keys and their corresponding number of cars in Washington as values.

  Returns:
    None

  """


  brands = list(data.keys())
  car_counts = list(data.values())


  plt.figure(figsize=(8, 6))
  plt.bar(brands, car_counts, color=['skyblue', 'lightgreen', 'gold'])
  plt.xlabel("Brand")
  plt.ylabel("Number of Cars")
  plt.title("Frequency of EV Car Brands in Washington")


  for i, count in enumerate(car_counts):
    plt.text(i, count + 0.1, f"{count}", ha='center', va='bottom')

  if len(brands) > 5:
    plt.xticks(rotation=45)

  
  plt.tight_layout()
  plt.show()

x = get_column_strings("Electric_Vehicle_Population_Data.csv", 6)
y = string_counter(x)
z = top_10(y)
plot_ev_car_brands_washington(z)