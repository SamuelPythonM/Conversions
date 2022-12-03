import time
import json


def mphtokmh(x):
    return float(x)*1.609344
def kmhtomph(x):
    return float(x)/1.609344
def celtofair(x):
    return float(x)*1.8+32
def fairtocel(x):
    return (float(x)-32)/1.8
def metertofoot(x):
    return float(x)*3
def foottometer(x):
    return float(x)/3
def miletokilometer(x):
    return float(x)*1.621
def kilometertomile(x):
    return float(x)/1.621
def inchestocentimeters(x):
    return float(x)*2.54
def centimeterstoinches(x):
    return float(x)/2.54
print("Welcome To Conversions!")
print("Version = Beta 1.0")
rows = int(6)
columns = 2*rows -1
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( (columns//2)-i <= j <= (columns//2)  +i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1
    
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( i <= j <= columns-1 -i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1



print("Conversions: ")
print("1. MPH to KMH")
print("2. KMH to MPH")
print("3. Celcius to Fahrenheit")
print("4. Fahrenheit to Celcius")
print("5. Meters to Feet")
print("6. Feet to Meters")
print("7. Miles to KiloMeters")
print("8. KiloMeters to Miles")
print("9. Inches to CentiMeters")
print("10. CentiMeters to Inches")

while True:
    choice = input("Please Choose a Conversion: 1-10: ")
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        if choice == str(1):
            num1 = input("Please Enter MPH To Be Converted To KMH: ")
            print(mphtokmh(num1))
        elif choice == str(2):
            num1 = input("Please Enter KMH To Be Converted To MPH: ")
            print(kmhtomph(num1))
        elif choice == str(3):
            num1 = input("Please Enter A Celsius Temperture To Be Converted To Fahrenheit: ")
            print(celtofair(num1))
        elif choice == str(4):
            num1 = input("Please Enter A Fahrenheit Temperture To Be Converted To Celcius: ")
            print(celtofair(num1))
        elif choice == str(5):
            num1 = input("Please Enter An Amount Of Meters To Be Converted To Feet: ")
            print(metertofoot(num1))
        elif choice == str(6):
            num1 = input("Please Enter An Amount Of Feet To Be Converted To Meters: ")
            print(foottometer(num1))
        elif choice == str(7):
            num1 = input("Please Enter An Amount Of Miles To Be Converted To KiloMeters: ")
            print(miletokilometer(num1))
        elif choice == str(8):
            num1 = input("Please Enter An Amount Of KiloMeters To Be Converted To Miles: ")
            print(kilometertomile(num1))
        elif choice == str(9):
            num1 = input("Please Enter An Amount Of Inches To Be Converted To CentiMeters: ")
            print(inchestocentimeters(num1))
        elif choice == str(10):
            num1 = input("Please Enter An Amount Of CentiMeters To Be Converted To Inches: ")
            print(centimeterstoinches(num1))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Please Wait a Second")
            print("Closing....")
            time.sleep(3)
            break
rows = int(6)
columns = 2*rows -1
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( (columns//2)-i <= j <= (columns//2)  +i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1
    
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( i <= j <= columns-1 -i):
            print("*",end = "")
        else:
            print(" ",end = "")
        
        j+=1
    print(" ")
    i+=1





