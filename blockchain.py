
#genesis_block is the first block in the blockchain as the next ones will need a previous hash key. 

genesis_block = {
    "previous_hash": "",
    "index" : 0,
    "transactions" : []
}

# Then add the genesis_block to the blockchain, so it will not throw an error when last_block variable is trying to access the last block.

blockchain = [genesis_block]
#Open_transactions hows a list of new trascations that have not been processed yet
open_transactions = []
owner = "seraphine"

def hash_block(block):
    return "-".join([str(block[key]) for key in block])



def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    # not need for an else statement here,if the statement is True the first return will run and exit the fxn, the second will not run.
    return blockchain[-1]

#Used default arguments in setting the first last_transaction amount
def add_transaction(recipient,sender=owner,amount=1.0):
    """
:sender : The sender of the coins
:recipient: The rcipient of the coins
:amount : The amount of coins sent with the transaction(default = 1.0)
"""
    transaction = {
    "sender" : sender,
    "recipient": recipient,
    "amount": amount
    }
    open_transactions.append(transaction)

#when the mine_block function is called, this should take all the open transactions and add them to a block, which will be eventually added to the blockchain.
def mine_block():

    last_block = blockchain[-1]
    # using list comprehension
    hashed_block = hash_block(last_block)

#to access the previous hash, loop through last_block that holds the previous block, and access the key "previous_hash"
    # for key in last_block:
    #     value = last_block[key]
 #hashed_block variable is used to store all the values   
        # hashed_block = hashed_block + str(value)
    
    print(hashed_block, 'this is hashed_block')

    block = {
    "previous_hash": hashed_block,
    "index" : len(blockchain),
    "transactions" : open_transactions
    }

    blockchain.append(block)



def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float((input('Transaction Amount please ?:')))
    return tx_recipient, tx_amount



def get_user_choice():
    user_input = input('Your choice? ')
    return user_input 
    
def print_blockchain_elements():
    #output blockchain to the console
    for block in blockchain:
        print(block)

def verify_chain():
#    if you wrap an element in enumerate it will return a tuple with the index of that element and the element itself 
    for (index,block) in enumerate(blockchain):
        print(index,block , 'this is the index and block')
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            print(hash_block(blockchain[index - 1]))
            return False        
    return True
   

waiting_for_input = True
while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        #Adding transaction to opentransaction
        add_transaction(recipient,amount=amount)
        print(open_transactions)

    elif user_choice == '2':
        mine_block()

    elif user_choice == '3':
        print_blockchain_elements()

    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    elif user_choice == 'q':
        #setting the waiting variable to false to exit the loop
         waiting_for_input = False
    else:
        print('Invalid input')

    if not verify_chain():
        print_blockchain_elements()
        print('invalid blockchain')
        break

print('done')   



#seraphine if you notice the order of parameter is switched when calling the function. This is because I used a keyword arguments. It does not matter the order as long as you the paraments of the functions to the arguments when calling it.




