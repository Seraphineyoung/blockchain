blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

#Used default arguments in setting the first last_transaction amount
def add_value(transaction_amount,last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])

def get_transaction_value():
    return float(input('Transaction Amount please ?:'))

def get_user_choice():
    user_input = input('Your choice ')
    return user_input

def print_blockchain_elements():
    #output blockchain to the console
    for block in blockchain:
        print(block)

   
tx_amount = get_transaction_value()
#saving the value of input function in a variable calle tx_amount
add_value(tx_amount)

while True:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(transaction_amount=tx_amount,last_transaction=get_last_blockchain_value())

    else:
        print_blockchain_elements()

print(done)   

# add_value(last_transaction=get_last_blockchain_value(),transaction_amount=tx_amount)

#seraphine if you notice the order of parameter is switched when calling the function. This is because I used a keyword arguments. It does not matter the order as long as you the paraments of the functions to the arguments when calling it.

# tx_amount = get_user_input()
# add_value(transaction_amount=tx_amount,last_transaction=get_last_blockchain_value())

# tx_amount = get_user_input()
# add_value(last_transaction =get_last_blockchain_value(),transaction_amount=tx_amount)

# print(blockchain)



