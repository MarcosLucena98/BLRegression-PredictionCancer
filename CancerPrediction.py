# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 22:14:47 2025

@author: Marcos
"""

# In[0.1]: Package installation

!pip install pandas
!pip install numpy
!pip install -U seaborn
!pip install matplotlib
!pip install plotly
!pip install scipy
!pip install statsmodels
!pip install scikit-learn
!pip install statstests

# In[0.2]: Package Import

import pandas as pd # data manipulation in dataframe format
import numpy as np # mathematical operations
import seaborn as sns # graphical visualization
import matplotlib.pyplot as plt # graphical visualization
from scipy.interpolate import UnivariateSpline # smoothed sigmoid curve
import statsmodels.api as sm # model estimation
import statsmodels.formula.api as smf # binary logistic model estimation
from statstests.process import stepwise # Stepwise procedure
from scipy import stats # chi2 statistics
import plotly.graph_objects as go # 3D graphics
from statsmodels.iolib.summary2 import summary_col # model comparison
from statsmodels.discrete.discrete_model import MNLogit # multinomial logistic model estimation
import warnings
from sklearn.preprocessing import MinMaxScaler
warnings.filterwarnings('ignore')

# In[0.3] Loading the Data

