from data_analizer import DataAna

# 只输出label对应的odd和日期。
tmp = [
    ['2021-12-31', 1.8],
    ['2021-12-31', 1.8],
    ['2021-12-31', 1.8],
    ['2021-12-31', 1.8],
    ['2022-12-31', 1.8],
    ['2022-12-31', 1.8],
    ['2022-12-31', 2.1],
]

cost = 1


# 找出tmp中的所有日期并去重，计算每个日期对应的odd*cost的总和
class CostAna:
    def __init__(self, cost):
        self.cost = cost

    def calculate_total_cost(self, tmp):
        unique_dates = set([row[0] for row in tmp])
        total_cost_dict = {}
        for date in unique_dates:
            total_cost_dict[date] = sum([row[1] * self.cost for row in tmp if row[0] == date])
        return total_cost_dict


# 测试
if __name__ == '__main__':
    cost_ana = CostAna(cost)
    total_cost_dict = cost_ana.calculate_total_cost(tmp)
    print(total_cost_dict)
