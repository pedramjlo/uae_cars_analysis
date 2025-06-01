from analysis.clustering_analysis.utils.clusteringUtils import ClusteringAnalysis

class BrandClustering:
    def __init__(self, df):
        self.df = df

    def cluster_by_sales(self, k=3):
        try:
            # Aggregate total price per brand
            data = self.df.groupby('Make')['Price'].sum().reset_index()
            features = data[['Price']].values

            clustering = ClusteringAnalysis(features)
            model, labels = clustering.fit_kmeans(k=k)

            # Optional: attach labels to data
            data['cluster'] = labels
            return data, model

        except Exception as e:
            print(f"Clustering failed: {e}")
            return None, None
