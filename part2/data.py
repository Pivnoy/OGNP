import pandas as pd

# чтение данных из csv формата по ТЗ
data = pd.read_csv("/Users/lubovmakareva/Documents/ognp3/part2/Aids2.csv")

# Блок начальных сведений о данных
dataFrame = pd.DataFrame(data)

# Информация о типах столбцов
print(dataFrame.dtypes)
# Общая размерность объекта
print(dataFrame.size)
# Кортеж, в котором хранится количество строк и столбцов
print(dataFrame.shape)