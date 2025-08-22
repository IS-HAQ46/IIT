print('Welcome to the Python Coffee Shop!')
customer_name = input('What is your name? ')

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50
total_cost=0
while True:
    print('Hello, ' + customer_name + '! Let\'s order some coffee.') 
    print('Coffee: $' + str(price_coffee))
    print('Latte: $' + str(price_latte))
    print('Mocha: $' + str(price_mocha))
 
    choice = input('What would you like to order? (coffee/latte/mocha): ').lower()
 
    if choice == 'coffee':
         cost = price_coffee
    elif choice == 'latte':
         cost = price_latte
    elif choice == 'mocha':
         cost = price_mocha
    else:
         print('Sorry, we do not have that.')
         cost = 0
    
    quantity = int(input('How many cups would you like? '))
    total_cost = total_cost+(cost * quantity )
    if quantity > 1:
         print('You get a discount of $1.00!')
         total_cost -= 1.00


    customer_type= input('are you a student? (yes/no)').lower()
    if customer_type == "yes":
        print('you get 10% students discount')
        std_discount= (total_cost/100)*10
        total_cost = total_cost-std_discount

 
    print('Your total is: $' + str(total_cost))

    order= input("do you want another order?(yes/no)")
    if order == "no":
        print('Thank you, ' + customer_name + '! Please come again.')
        break
