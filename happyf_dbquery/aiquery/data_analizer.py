from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

tmp_data = [
    [2.3, 2.1, 1.9, 2.5, 2.1, 0.6],  # 初+终+结果
    [2.3, 2.1, 1.9, 2.5, 2.1, 0.6],
    [2.3, 2.1, 1.9, 2.5, 2.1, 0.6],
    [2.3, 2.1, 1.9, 2.5, 2.1, 0.6],
    [2.3, 2.1, 1.9, 2.5, 2.1, 0.6],
]
tmp_label = [1, 0, 1, 1, 1]
tmp_data = pd.DataFrame(tmp_data)
tmp_label = pd.DataFrame(tmp_label)

class DataAna:
    def __init__(self, k=5):
        self.k = k
        self.model = KNeighborsClassifier(n_neighbors=k)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    # 根据四个参数找数据集
    def dataf(self, a, b, c, d,request):

        # 以下三行是造出来的测试数据，后面需要根据a, b, c, d从数据库拉出来
        X_train = tmp_data
        y_train = tmp_label
        request = [[2.5, 2.1, 0.6, 2.5, 2.1, 0.6]]

        self.fit(X_train,y_train)
        return self.predict(request)


if __name__ == '__main__':
    model = DataAna(k=3)
    print(model.dataf(1,2,3,4,5))