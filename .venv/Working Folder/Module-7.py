"""File Name: Module-7.py
Date of Last Edit: 4/8/2024
Author: Benjamin Thomas Raleigh
Purpose of Code: Remove outliers from a list of words.
"""
from wv import Model
from scipy.stats import zscore

model = Model("models/glove_short.txt")
while True:
    words = input("Please enter a comma separated list of words: ").split(",")
    