#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:14:47 2019

@author: adrian
K-Nearest-Neighbors Algorithm
"""

# Generate sample data
import numpy as np
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import fbeta_score, make_scorer
import warnings 
warnings.simplefilter(action='ignore', category=FutureWarning)

X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=1)
scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
scalarX.fit(X)
scalarY.fit(y.reshape(100,1))
X = scalarX.transform(X)
y = scalarY.transform(y.reshape(100,1))

# Implementierung des k-Nächste-Nachbarn-Algorithmus. Dieser bestimmt auch selber bei einer Liste von Anzahlen an Nachbarn die betrachtet werden 
# sollen welches die beste Wahl ist.
#
# X: Inputvektor für das Kalibirieren des Modells 
# Y: Inputvektor für das Kalibirieren des Modells (Zielvektor an den die Gewichte angepasst werden) 
# T: Inputvektor für den eine Vorhersage bestimmte werden soll

def k_nearest_neighbor (X,Y):
    
    split = int(0.8*np.size(X,0))
    
    X_train = X[:split,:]
    Y_train = Y[:split]
    X_test = X[split:,:]
    
    
    params = {'n_neighbors':[2,3,4,5,6,7,8,9], 'weights': ['uniform', 'distance']}

    knn = neighbors.KNeighborsRegressor()
    
    knn_gridsearch_model = GridSearchCV(knn, params, cv=5)
    knn_gridsearch_model.fit(X_train,Y_train)
    
    return knn_gridsearch_model.predict(X_test)

prediction_neighbor = k_nearest_neighbor(X,y)
    
    

