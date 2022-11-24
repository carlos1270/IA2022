import sklearn.cluster as c
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyt

def score(gabarito, previsoes):
    acertos = 0
    for i in range(len(gabarito)):
        if gabarito[i] == previsoes[i]:
            acertos += 1
    return (acertos / len(gabarito))

# Plota a base com a classificação original
rs = pd.read_csv('BaseRS.csv', sep=",", header=0)
sns.pairplot(rs, hue="target", palette=['red', 'green', 'blue'])
pyt.show()

# Dropa a coluna target com os resultados 'corretos'
rs = rs.drop(columns='target')
# Instância o algoritmo de kmeans com 3 clusters
kmeans = c.KMeans(n_clusters=3)
# Treina o algoritmo com a base RS
kmeans.fit(rs)
# Gera o score do algoritmo
rs_gabarito = pd.read_csv('BaseRS.csv', sep=",", header=0)
gabarito = []
for esporte in rs_gabarito['target']:
    if esporte == 'F':
        gabarito.append(0)
    elif esporte == 'B': 
        gabarito.append(1)
    elif esporte == 'V':
        gabarito.append(2)
print(score(gabarito, kmeans.labels_))

# Faz a insersão da coluna 'target-kmeans' com as previsões do kmeans
rs.insert(1, "target-kmeans", kmeans.labels_)

# Plota a base com as classes classificadas pelo k-means
sns.pairplot(rs, hue="target-kmeans", palette=['red', 'green', 'blue'])
pyt.show()

# Separa e une os centroides a base
centroides = []
for i in range(len(kmeans.cluster_centers_)):
    centroides.append([kmeans.cluster_centers_[i][0], int(i)+int(len(kmeans.cluster_centers_)), kmeans.cluster_centers_[i][1]])
df_centroides = pd.DataFrame(centroides, columns=['Altura', 'target-kmeans', 'Peso'])
kmenas_centroides = pd.concat([rs, df_centroides])

# Plota a base com as classes classificadas pelo k-means com os centroides
""" 
    Orange é centroide de red
    Yellow é centroide de green
    Purple é centroide de blue 

    Logo, um score de 0.76
"""
sns.pairplot(kmenas_centroides, hue="target-kmeans", palette=['red', 'green', 'blue', 'orange', 'yellow', 'purple'])
pyt.show()