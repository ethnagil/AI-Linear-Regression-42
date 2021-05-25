# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egillesp <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/12 12:29:55 by egillesp          #+#    #+#              #
#    Updated: 2021/04/12 12:29:57 by egillesp         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python
# -*-coding:Utf-8 -*

import csv
import math
import matplotlib.pyplot as plt

# global variable for number of elements in input file
m = 0 

def opendata(filename):
    global m
    file = open(f'{filename}', 'r')
    test = csv.reader(file)
    km = list()
    price = list()
    for row in test:
        try:
            if row[0] and row[1]:
                km.append(float(row[0]))
                price.append(float(row[1]))
                m=m+1
        except:
            print("Header or alphanumeric input ignored")
    # #### display 1 - scatter chart of input
    print("__Exit chart to continue......")
    plt.title("Scatter Chart: input X and Y values")
    plt.plot(km, price, "ro")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(km, price)
    plt.show()
    return km, price

# normalize the numbers (reduction) between 0 and 1 for size problems and efficiency 
def normalize_list(liste):
    max_list = float(max(liste))
    new_list = []
    for i in range(len(liste)):
        new_list.append(liste[i] / max_list)
    return new_list, max_list

def calc_newthetas(km, price, theta0, theta1, learnRate):
    diff0 = 0.0
    diff1 = 0.0
    i = 0
    for i in range(m):  
        diff0 += (hypothesis(theta0, theta1, km[i]) - price[i])
        diff1 += (hypothesis(theta0, theta1, km[i]) - price[i]) * km[i]
    tmp0 = theta0 - (learnRate / float(m) * diff0)   
    tmp1 = theta1 - (learnRate / float(m) * diff1)
    return tmp0, tmp1

def hypothesis(theta0, theta1, km):
    estimatePrice = theta0 + (theta1 * km)
    return (estimatePrice)

def grad_desc(km, price, theta0, theta1, learnRate):
    J = float()
    tmpJ = -1.0
    w=list()
    mse=list()
    while round(tmpJ, 25) != round(J, 25):
        tmpJ = J
        theta0, theta1 = calc_newthetas(km, price, theta0, theta1, learnRate)
        sumJ = 0.0
        for i in range(m):
            sumJ = sumJ + (hypothesis(theta0, theta1, km[i]) - price[i])**2           
        J = (1 / (2 * float(m))) * sumJ
        w.append((theta0*8290)+(theta1*8290/240000))
        mse.append(J)
    plot_mse(mse,w)
    return(theta0, theta1)

# claculate standard Linear Regression for the dataset using mathamatical formula - Bonus to test accuracy
def Average(lst):
    return sum(lst) / len(lst)

def classic_linier_regression(km, price):
    sum_dev_x = 0
    sum_dev_x2 = 0
    sum_dev_y = 0
    sum_dev_y2 = 0 
    sum_dev_xy = 0
    for i in range(m):
        sum_dev_x += km[i] - Average(km)
        sum_dev_x2 += pow(km[i] - Average(km),2)
        sum_dev_y += price[i] - Average(price)
        sum_dev_y2 += pow(price[i] - Average(price),2)
        sum_dev_xy += (km[i] - Average(km)) * (price[i] - Average(price))
    r = sum_dev_xy/math.sqrt(sum_dev_x2*sum_dev_y2)
    b = r*((math.sqrt(sum_dev_y2/(m-1)))/(math.sqrt(sum_dev_x2/(m-1))))
    a = Average(price)-b*Average(km)

    return(a,b)

# plot the data 
def plot_data(theta0, theta1, km, price, max_km):
    print("__Exit chart to continue......")
    plt.title("Linear Regression using gradient descent algorithm")
    plt.xlabel('x')
    plt.ylabel('y=theta0 +theta1(x)')
    plt.plot([hypothesis(theta0, theta1, x) for x in range(int(max_km))], "b", linewidth=3)
    plt.plot(km, price, "ro")
    plt.savefig('fig2linearRegression.png')
    plt.show()

# plot the cost curve - bonus
def plot_mse(mse,w):
    print("__Exit chart to continue......")
    plt.title("Cost Slope")
    plt.xlabel('multiplication factor')
    plt.ylabel('error')
    plt.plot(w, mse, "ro") 
    plt.savefig('fig1cost.png')
    plt.show()

def save_thetas(theta0, theta1, a, b):
    with open('thetas.csv', 'w', newline='') as file:
    # with open('thetas.csv', 'wb') as file:   
        writer = csv.writer(file)
        writer.writerow(["theta0", theta0])
        writer.writerow(["theta1", theta1])
        writer.writerow(["a", a])
        writer.writerow(["b", b])

def estimate(filename, learnRate):
    km, price = opendata(filename)
    theta0 = 0.0
    theta1 = 0.0
    km_normalize, max_km = normalize_list(km)
    price_normalize, max_price = normalize_list(price)

    #calculate theta0,1 using gradient descent algorithm
    theta0, theta1 = grad_desc(km_normalize, price_normalize, theta0, theta1, learnRate)
    theta0 = theta0 * max_price
    theta1 = (theta1 * max_price) / max_km
 
    #plot the resulting linear representation on a scatterchart
    plot_data(theta0, theta1, km, price, max_km)

    #compare algorithm results with standard linier regression
    a,b = classic_linier_regression(km, price)
    print("\n____Compare the results with a classic Linear regression calculation____")
    print("Classic Linier regression a: {}  b: {}".format(a,b))
    print("Gradiant algorithm L.R   t0: {} t1: {}".format(theta0, theta1))
    save_thetas(theta0, theta1, a , b)


if __name__ == '__main__':
    filename = 'data.csv'
    learnRate = 0.01  # normally between 0 and 1

    estimate(filename, learnRate)
