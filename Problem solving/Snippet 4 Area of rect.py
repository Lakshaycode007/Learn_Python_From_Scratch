
# Excercise 1 calculate the area of rectangle

length =  float(input("Enter the length "))
width = float(input("Enter the width "))

area = length * width

print(f"Area of rectangle is {length} and {width} = {area} cm²")


# Shopping cart program

item = input("What would you like to buy ")
price = float(input("What is the price of your product "))
quantity = int(input("Howm many quantity you bought "))

total_bill = int(price * quantity)
print(f"Your item is {item} quantity is {quantity} price of your item {price} \nyour total_bill is {total_bill}")