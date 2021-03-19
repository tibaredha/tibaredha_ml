import warnings
warnings.filterwarnings('ignore')

import numpy as np 
import scipy 
import pandas as pd
import matplotlib as plt0
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",10)
pd.set_option("display.max_rows",10)
pd.set_option("display.width",60)

import datetime
from datetime import datetime,date
import os
for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
