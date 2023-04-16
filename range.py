# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:18:22 2023

@author: sompa
"""



start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))


for num in range(start, end + 1):


	if num >= 0:
		print(num, end=" ")
