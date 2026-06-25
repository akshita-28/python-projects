print("="* 40)
print(" TEMPERATURE CONVERTER")
print("=" * 40 )
celsius = float(input("Enter Temperature in celsius :"))
fahrenheit =(celsius * 9/5)+32
print("/n")
print("Temperature in fahrenheit = ",round(fahrenheit , 2))
if celsius <0:
    print("Weather :Freezing")
elif celsius >= 0 and celsius<30:
    print("weather : cold")    
elif celsius >=0 and celsius <30:
    print("weather : pleasant")
elif celsius >= 30 and celsius<40:
    print("weather :hot")
else:
    print("weather:very hot")       

