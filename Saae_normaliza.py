# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 16:40:10 2025

@author: julio
"""

import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer # Habilita o IterativeImputer (é uma funcionalidade experimental).
from sklearn.impute import IterativeImputer # Importa a classe IterativeImputer para preenchimento inteligente de dados ausentes.
from sklearn.ensemble import RandomForestRegressor

# Carrega o DataFrame
df = pd.read_excel('datase_saae.xlsx')

