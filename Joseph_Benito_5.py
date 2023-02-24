#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#This program inputs and records information of each person in a class in excel worksheet

from pandas import DataFrame

try:    
    students = int(raw_input("How many students are in the class: "))
except ValueError:
    print "Invalid entry! Enter only whole numbers"
    students = int(raw_input("How many students are in the class: "))
    
person=[]
name=[]
gender=[]
major=[]
diet=[]
height=[]
degree=[]
breakfast=[]
lunch=[]
dinner=[]
lens=[]
car=[]
car_color=[]
distance=[]

for i in range(1,students+1):
    try:    
        person.append(int(raw_input("\nEnter the number of the %d person: " %(i))))
    except ValueError:
        print "Invalid entry! Enter only whole numbers"
        person.append(int(raw_input("Enter the number of the %d person: " %(i))))
    name.append(str(raw_input("Enter the name of the %d person: " %(i))))
    gender.append(str(raw_input("Enter the gender of the %d person: " %(i))))
    major.append(str(raw_input("Enter the major of the %d person: " %(i))))
    diet.append(str(raw_input("Enter the diet of the %d person: " %(i))))
    try:
        height.append(float(raw_input("Enter the height of the %d person in feet.inches: " %(i))))
    except ValueError:
        print "Invalid entry! Enter either whole number or decimal"
        height.append(float(raw_input("Enter the height of the %d person in feet.inches: " %(i))))
    degree.append(str(raw_input("Enter the degree of the %d person: " %(i))))
    breakfast.append(str(raw_input("Does the %d person eat breakfast daily: " %(i))))
    lunch.append(str(raw_input("Does the %d person eat lunch daily: " %(i))))
    dinner.append(str(raw_input("Does the %d person eat dinner daily: " %(i))))
    lens.append(str(raw_input("Does the %d person wear corrected lenses: " %(i))))
    car.append(str(raw_input("Enter the make of the %d person's car: " %(i))))
    car_color.append(str(raw_input("Enter the color of the %d person's car: " %(i))))
    try:
        distance.append(float(raw_input("Enter the commute distance of the %d person from home to UAH in miles: " %(i))))
    except ValueError:
        print "Invalid entry! Enter either whole number or decimal"
        distance.append(float(raw_input("Enter the commute distance of the %d person from home to UAH in miles: " %(i))))

c1 = person
c2 = name
c3 = gender
c4 = major
c5 = diet
c6 = height
c7 = degree
c8 = breakfast
c9 = lunch
c10 = dinner
c11 = lens
c12 = car
c13 = car_color
c14 = distance

df = DataFrame({'Student':c1,'Name':c2,'Gender':c3,'Major':c4,'Diet':c5,'Height':c6,'Degree':c7,'Breakfast':c8,'Lunch':c9,'Dinner':c10,'Lens':c11,'Car':c12,'Car_color':c13,'Commute_distance':c14},columns=['Student','Name','Gender','Major','Diet','Height','Degree','Breakfast','Lunch','Dinner','Lens','Car','Car_color','Commute_distance'])

df.to_excel('students_info.xlsx', sheet_name='info',index=False)

    
