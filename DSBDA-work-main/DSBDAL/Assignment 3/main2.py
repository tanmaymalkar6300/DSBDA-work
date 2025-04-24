import pandas as pd 


data = pd.read_csv('Iris.csv')
grouped_data = data.groupby('Species')

IrisVirginica = grouped_data.get_group('Iris-virginica')
print('Iris Virginica\n')
print(IrisVirginica.describe())

print('\nIris Setosa\n')
IrisSetosa = grouped_data.get_group('Iris-setosa')
print(IrisSetosa.describe())

print('\nIris versicolor\n')
Irisversicolor = grouped_data.get_group('Iris-versicolor')
print(Irisversicolor.describe())