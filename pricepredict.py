# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pricepredict.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: egillesp <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/12 12:30:09 by egillesp          #+#    #+#              #
#    Updated: 2021/04/12 12:30:12 by egillesp         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python
# -*-coding:Utf-8 -*

import csv

def getVariables():

	try:
		file = open("thetas.csv", "r")
		test = csv.reader(file)
		for row in test:
			if row[0] == 'theta0':
				theta0 = float(row[1])
			if row[0] == 'theta1':
				theta1 = float(row[1])
	except:
		theta0 = 0.0
		theta1 = 0.0
	return theta0, theta1

def estimate():
	theta0, theta1 = getVariables()
	if theta0 == 0 or theta1 == 0:
		print("Variables not set: Please run the linear_regression program")
	else:
		while True:
				inputKM = input("\nPlease enter the milage of your car to estimate the price (E to exit): ")
				if inputKM == 'E':
					break
				try:
					inputKM = int(inputKM)
					if inputKM < 0:
						raise exception()
					
					estimatePrice = theta0 + theta1 * inputKM
					if estimatePrice >= 0:
						print("A car with {} km has an estimated price of {} euros".format(round(inputKM, 2), round(estimatePrice, 2)))
					else:
						print("A car with {} km is worth ZERO. Its good for the scrap yard!".format(int(round(inputKM, 0))))
				except:
					print("Mileage must be a whole positive numeric number, please try again.")

if __name__ == '__main__':
	estimate()
