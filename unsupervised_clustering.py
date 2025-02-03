# 4. Unsupervised Clustering
X = tfidf_matrix
kmeans = KMeans(n_clusters=10, random_state=42)
labels = kmeans.fit_predict(X)
silhouette_avg = silhouette_score(X, labels)
print(f'Silhouette score: {silhouette_avg}')
