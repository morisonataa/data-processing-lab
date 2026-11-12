Lab Overview - This lab is about data processing of dataset from cities.csv file, which contain the information of city, country, latitude, longtitude, temperature.


Project Structure
data-processing-lab/
│
├── README.md                 # This file
├── Cities.csv                # The dataset
|---- data_processing.py	  # The analysis code


Design Overview
The program consists of two main classes:
1.DataLoader: Loads CSV files and converts their contents into a list of dictionaries. It uses base_path to locate the dataset.

2.Table: Stores the dataset and provides two main methods:
- filter_items(): Filters records based on specified conditions.
- aggregate(): Performs calculations on a selected column using an aggregation function.


How to test and run your code
1.Ensure Cities.csv and data_processing.py are in the same directory.
2.Run the program
3.Check the output to verify with CSV files.