import pandas as pd 
import numpy as np 

data = pd.read_csv('Iris.csv')
described = data.describe()

print("--------MEAN--------")
print("The mean of Sepal Length is ",described['SepalLengthCm']['mean'])
print("The mean of Sepal Width is ",described['SepalWidthCm']['mean'])
print("The mean of Petal Length is ",described['PetalLengthCm']['mean'])
print("The mean of Petal Width is ",described['PetalWidthCm']['mean'])


print("-------MEDIAN-----")
print("The median of Sepal Length is ",data['SepalLengthCm'].median())
print("The median of Sepal Width is ",data['SepalWidthCm'].median())
print("The median of Petal Length is ",data['PetalLengthCm'].median())
print("The median of Petal Width is ",data['PetalWidthCm'].median())


print("-------MODE-----")
print("The mode of Sepal Length is ",data['SepalLengthCm'].mode()[0])
print("The mode of Sepal Width is ",data['SepalWidthCm'].mode()[0])
print("The mode of Petal Length is ",data['PetalLengthCm'].mode()[0])
print("The mode of Petal Width is ",data['PetalWidthCm'].mode()[0])



print("--------MAX--------")
print("The max of Sepal Length is ",described['SepalLengthCm']['max'])
print("The max of Sepal Width is ",described['SepalWidthCm']['max'])
print("The max of Petal Length is ",described['PetalLengthCm']['max'])
print("The max of Petal Width is ",described['PetalWidthCm']['max'])



print("--------MIN--------")
print("The min of Sepal Length is ",described['SepalLengthCm']['min'])
print("The min of Sepal Width is ",described['SepalWidthCm']['min'])
print("The min of Petal Length is ",described['PetalLengthCm']['min'])
print("The min of Petal Width is ",described['PetalWidthCm']['min'])


print("---STD DEVIATION---")
print("The standard deviation of Sepal Length is ",data['SepalLengthCm'].std())
print("The standard deviation of Sepal Width is ",data['SepalWidthCm'].std())
print("The standard deviation of Petal Length is ",data['PetalLengthCm'].std())
print("The standard deviation of Petal Width is ",data['PetalWidthCm'].std())