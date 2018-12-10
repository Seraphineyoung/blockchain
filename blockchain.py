blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

#Used default arguments in setting the first last_transaction amount
def add_value(transaction_amount,last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])

def get_user_input():
    return float(input('Transaction Amount please ?:'))
    
tx_amount = get_user_input()
#saving the value of input function in a variable calle tx_amount
add_value(tx_amount)

tx_amount = get_user_input()

add_value(last_transaction=get_last_blockchain_value(),transaction_amount=tx_amount)

#seraphine if you notice the order of parameter is switched when calling the function. This is because I used a keyword arguments. It does not matter the order as long as you the paraments of the functions to the arguments when calling it.

tx_amount = get_user_input()
add_value(transaction_amount=tx_amount,last_transaction=get_last_blockchain_value())

tx_amount = get_user_input()
add_value(last_transaction =get_last_blockchain_value(),transaction_amount=tx_amount)

print(blockchain)

