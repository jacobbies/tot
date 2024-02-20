from dotenv import load_dotenv
from apify_client import ApifyClient
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Load .env variables and initialize apifyclient with API token
load_dotenv()
APIFY_API_KEY = os.getenv('APIFY_API_KEY')
client = ApifyClient(APIFY_API_KEY)

# Draw a title and some text to the app:
'''
# Datascout

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df # Draw the dataframe

x = 10
'x', x  # Draw the string 'x' and then the value of x

# Also works with most supported chart types
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # Draw a Matplotlib chart