#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:45:15 2019

@author: usmankhan
"""

balance = int(raw_input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
monthlyPaymentRate = float(raw_input("Enter the monthly payment rate as a decimal: "))
month = 0

while month<12:
    monthlyPayment = (monthlyPaymentRate)*(balance)
    unpaidBalance = (balance)-(monthlyPayment)
    interest = ((annualInterestRate)/(12.0)) *(unpaidBalance)
    updatedBalance = (unpaidBalance)+(interest)
    month +=1
    balance = updatedBalance
    print ('Month: '+ str(month))
    print ('Minimum monthly payment:' + str(round(monthlyPayment,2)))
    print ('Remaining Balance after one year: ' + str(round(updatedBalance,2)))