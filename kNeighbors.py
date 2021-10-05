import numpy as np
import pandas as pd

books = pd.read_csv("/Users/benjamingoldblatt/webscraper/goodreads.csv")
ranked_books = books.sort_values(by=["rating"], ascending=False)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 

y = books['genre'].values
X = books.drop(['genre','title','author', 'rating', 'reviews'], axis=1).values
print(y)
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=3, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=10)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))