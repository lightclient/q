import datetime as date
import os

import block
import mine
# import transaction


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# blockchain = [create_genesis_block()]
# previous_block = blockchain[0]
#
# num_of_blocks_to_add = 20
#
# for i in range(0, num_of_blocks_to_add):
#     block_to_add = next_block(previous_block)
#     blockchain.append(block_to_add)
#     previous_block = block_to_add
#
#     print("Block %s has been adde to the blockchain" % block_to_add.index)
#     print("Hash: %s\n" % block_to_add.hash)

os.system("clear")
print("Welcome to Q, Matt's first cryptocurrency.")

user_input = ""
while user_input != "q" and user_input != "quit":
    user_input = input("[Q]: ")

    if user_input == "mine":
        print("begin mining")
    elif user_input == "sync":
        print("syncing blockchain")

    elif user_input == "q":
        print("quit")
