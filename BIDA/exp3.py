import pandas,numpy
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
wcss=[]
features=pandas.read_csv