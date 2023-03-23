from sklearn.cluster import KMeans

tmp = [
    [[2.3, 2.1, 1.9], [2.5, 2.1, 0.6], 1],  # 初+终+结果
    [[2.3, 2.1, 1.9], [2.5, 2.1, 0.6], 2],
]

class DataAna:
    def __init__(self, data):
        """
        Initializes the model and fits it to the given data using K-Means clustering.
        """
        self.model = KMeans(n_clusters=len(set([d[2] for d in data])))
        points = [d[:2] for d in data]  # 仅选择前两个维度
        self.model.fit(points)

    def predict(self, point):
        """
        Predicts the cluster for the given point.
        """
        if len(point) != 3:
            raise ValueError("Point must be a list of three elements")
        cluster = self.model.predict([point[:2]])[0]
        return cluster


if __name__ == '__main__':
    dataAnner = DataAna(tmp)
    point = [[2.5, 2.1, 0.6],[2.5, 2.1, 0.6]]
    cluster = dataAnner.predict(point)
    print(f"Predicted cluster for {point}: {cluster}")
