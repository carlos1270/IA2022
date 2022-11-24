import sklearn.cluster as c
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyt

def score(gabarito, previsoes):
    acertos = 0
    for i in range(len(gabarito)):
        if gabarito[i] == previsoes[i]:
            acertos += 1
    return (acertos / 150)

# Plota a base com a classificação original
iris = pd.read_csv('iris.csv', sep=",", header=0)
# sns.pairplot(iris, hue="target", palette=['black', 'red', 'green'])
# pyt.show()

# Dropa a coluna target com os resultados 'corretos'
iris = iris.drop(columns='target')
# Instância o algoritmo de kmeans com 3 clusters
kmeans = c.KMeans(n_clusters=3)
# Treina o algoritmo com a base IRIS
kmeans.fit(iris)
# Gera o score do algoritmo
iris_gabarito = pd.read_csv('iris.csv', sep=",", header=0)
gabarito = []
for especie in iris_gabarito['target']:
    if especie == 'versicolor':
        gabarito.append(0)
    elif especie == 'setosa': 
        gabarito.append(1)
    elif especie == 'virginica':
        gabarito.append(2)
print(score(gabarito, kmeans.labels_))

# Faz a insersão da coluna 'target-kmeans' com as previsões do kmeans
iris.insert(1, "target-kmeans", kmeans.labels_)

# Plota a base com as classes classificadas pelo k-means
# sns.pairplot(iris, hue="target-kmeans", palette=['red', 'black', 'green'])
# pyt.show()

# Separa e une os centroides a base
centroides = []
for i in range(len(kmeans.cluster_centers_)):
    centroides.append([kmeans.cluster_centers_[i][0], int(i)+int(len(kmeans.cluster_centers_)), kmeans.cluster_centers_[i][1], kmeans.cluster_centers_[i][2], kmeans.cluster_centers_[i][3]])
df_centroides = pd.DataFrame(centroides, columns=['sepal length(cm)', 'target-kmeans', 'sepal width(cm)', 'petal length(cm)', 'petal width(cm)'])
kmeans_centroides = pd.concat([iris, df_centroides])

# Plota a base com as classes classificadas pelo k-means com os centroides
""" 
    Orange é centroide de red
    Gray é centroide de black
    Yellow é centroide de green 

    Logo, um score de 0.89
"""
sns.pairplot(kmeans_centroides, hue="target-kmeans", palette=['red', 'black', 'green', 'orange', 'gray', 'yellow'])
pyt.show()