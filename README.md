Lab Overview - This lab is about data processing of dataset from Cities.csv file and Countries.cvs file, which contain the information of city, country, latitude, longtitude, temperature. The program loads, filters, aggregates, and joins data from both files.


Project Structure
data-processing-lab/
│
├── README.md                 # This file
├── Cities.csv                # The dataset
|---- data_processing.py	  # The analysis code


Design Overview
The program consists of three main classes:
1.DataLoader: Loads CSV files and converts their contents into a list of dictionaries. It uses base_path to locate the dataset.
2.DB: Stores and manages multiple tables.
- insert(): Adds a table to the database.
- search(): Finds a table by its name.
3.Table: Stores the dataset and provides two main methods:
- filter_items(): Filters records based on specified conditions.
- aggregate(): Performs calculations on a selected column using an aggregation function.
- join(): Combines two tables using a common key.


How to test and run your code
1.Ensure Cities.csv, Countries.cvs and data_processing.py are in the same directory.
2.Run the program
3.Check the output to verify with CSV files.