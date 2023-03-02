# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:16:35 2023

@author: aswin
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def line_plot(file_path):
    """
    Plots a line chart for international student migration using data from the specified CSV file

    Args:
        file_path (str): The path of the CSV file

    Returns:
        None
    """
    # Read data from CSV file
    migration_data = pd.read_csv(file_path)

    # Drop rows with NaN values in the 'Country' column
    migration_data = migration_data.dropna(subset=['Country'])

    # Convert 'Country' column to string
    migration_data['Country'] = migration_data['Country'].astype(str)

    # Convert number columns to float
    for year in range(2014, 2022):
        col_name = str(year)
        migration_data[col_name] = migration_data[col_name].str.replace(',', '').astype(float)

    # Plot line chart for each year
    plt.figure()
    for year in range(2014, 2022):
        col_name = str(year)
        plt.plot(migration_data['Country'], migration_data[col_name], label=col_name, marker=".")
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    plt.xlabel("Country")
    plt.ylabel("Number of international student migration")
    plt.title("Trend of Enrollment over time")
    plt.show()


def bar_plot(file_path):
    """
    Plots a bar chart for student enrolments by level and mode of study using data from the specified CSV file

    Args:
        file_path (str): The path of the CSV file

    Returns:
        None
    """
    # Read data from CSV file
    enrollment_data = pd.read_csv(file_path)

    # Extract data for plotting
    levels_and_modes = np.array(enrollment_data['Level and Mode of Study'])
    no_of_students = np.array(enrollment_data['number of students'])

    # Plot bar chart
    plt.figure()
    plt.bar(levels_and_modes, no_of_students, color='green', label='Enrollment by Level and Mode')
    plt.xlabel('Level and Mode of Study')
    plt.ylabel('Number of Students')
    plt.title('Academic years 2021/22')
    plt.legend()
    plt.show()


def pie_plot1(file_path):
    """
    Plots a pie chart for relative sizes of universities using data from the specified CSV file

    Args:
        file_path (str): The path of the CSV file

    Returns:
        None
    """
    # Read data from CSV file
    data = pd.read_csv(file_path)

    # Convert 'International student population' column to numeric
    data['International student population'] = pd.to_numeric(data['International student population'], errors='coerce').fillna(0)

    # Extract data for plotting
    labels = data['Destination country']
    sizes = data['International student population']

    # Plot pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('International Student Population by Destination Country (2014)')
    plt.axis('equal')
    plt.show()


def pie_plot2(file_path):
    """
    Plots a pie chart for relative sizes of universities using data from the specified CSV file

    Args:
        file_path (str): The path of the CSV file

    Returns:
        None
    """
    # Read data from CSV file
    data = pd.read_csv(file_path)

    # Convert 'International student population' column to numeric
    data['International student population'] = pd.to_numeric(data['International student population'], errors='coerce').fillna(0)

    # Extract data for plotting
    labels = data['Destination country']
    sizes = data['International student population']

    # Plot pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('International Student Population by Destination Country (2020)')
    plt.axis('equal')
    plt.show()


# Line plot
line_plot("C:\\Users\\aswin\\Downloads\\oc051-chart-6 (2).csv")

# Bar plot
bar_plot("C:\\Users\\aswin\\Downloads\\sb265-figure-8 (3).csv")

# Pie plot1
pie_plot1("C:\\Users\\aswin\\Desktop\\pie chart 2014\\Book1.csv")

# Pie plot2
pie_plot2("C:\\Users\\aswin\\Desktop\\pie chart 2020\\Book2.csv")