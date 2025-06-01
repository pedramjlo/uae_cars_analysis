import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class ClusteringAnalysis:
    def __init__(self, data, scale_data=True):
        """
        Initialize the clustering analysis.

        Parameters:
        - data (ndarray or DataFrame): Input features for clustering.
        - scale_data (bool): Whether to scale data using StandardScaler.
        """
        self.original_data = data
        self.data = self._scale_data(data) if scale_data else data

    def _scale_data(self, data):
        scaler = StandardScaler()
        return scaler.fit_transform(data)

    def elbow_method(self, k_range=(1, 11), plot=True):
        """
        Applies the Elbow method to determine the optimal number of clusters.

        Parameters:
        - k_range (tuple): Range of K values to try (inclusive of start, exclusive of end).
        - plot (bool): Whether to show the elbow plot.

        Returns:
        - inertias (list): Inertia values for each k.
        """
        inertias = []
        for k in range(*k_range):
            model = KMeans(n_clusters=k, random_state=42)
            model.fit(self.data)
            inertias.append(model.inertia_)

        if plot:
            plt.figure(figsize=(8, 4))
            plt.plot(range(*k_range), inertias, marker='o')
            plt.xlabel('Number of clusters (k)')
            plt.ylabel('Inertia')
            plt.title('Elbow Method for Optimal k')
            plt.grid(True)
            plt.show()

        return inertias


    def fit_kmeans(self, k):
        """
        Fits KMeans with the specified number of clusters.

        Parameters:
        - k (int): Number of clusters.

        Returns:
        - model (KMeans): Trained KMeans model.
        - labels (ndarray): Predicted cluster labels.
        """
        model = KMeans(n_clusters=k, random_state=42)
        labels = model.fit_predict(self.data)
        return model, labels



    def plot_clusters(self, labels, model=None, show_centers=True):
        """
        Plots clustering results for 2D data.

        Parameters:
        - labels (ndarray): Cluster labels from fit_kmeans.
        - model (KMeans, optional): Trained KMeans model, used for centers.
        - show_centers (bool): Whether to plot cluster centers.
        """
        if self.data.shape[1] != 2:
            raise ValueError("plot_clusters only supports 2D data.")

        plt.figure(figsize=(8, 6))
        plt.scatter(self.data[:, 0], self.data[:, 1], c=labels, cmap='viridis', s=50)
        if show_centers and model is not None:
            centers = model.cluster_centers_
            plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroids')
            plt.legend()
        plt.title("KMeans Clustering Result")
        plt.grid(True)
        plt.show()
