blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    # not need for an else statement here,if the statement is True the first return will run and exit the fxn, the second will not run.
    return blockchain[-1]

#Used default arguments in setting the first last_transaction amount
def add_transaction(transaction_amount,last_transaction):

    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction,transaction_amount])

def get_transaction_value():
    return (input('Transaction Amount please ?:'))


def get_user_choice():
    user_input = input('Your choice? ')
    return user_input 
    
def print_blockchain_elements():
    #output blockchain to the console
    for block in blockchain:
        print(block)



while True:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(transaction_amount=tx_amount,last_transaction=get_last_blockchain_value())

    elif user_choice == '2':
        print_blockchain_elements()

    elif user_choice == 'q':
         break
    else:
        print('Invalid input')

print('done')   



#seraphine if you notice the order of parameter is switched when calling the function. This is because I used a keyword arguments. It does not matter the order as long as you the paraments of the functions to the arguments when calling it.




