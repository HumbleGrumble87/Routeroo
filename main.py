#! /usr/bin/env python3 

# initialize routing table
# array of arrays, first array is index, next is destination then mask in binary. last is interface
#apparently python has lists, not arrays

index = []

# BEFORE WE GO ANY FURTHER, FINISH FUTURE CODER. WILL TAKE A FEW HOURS. 


# program takes config as argument and modifies routing table
# once finished, a banner appears with following info
    # "Available commands are ADD, DELETE, SEND, PRINT"
    # "ADD 10.0.0.0/29 via INT0"
    # "DELETE 10.0.0.0/29 via INT0"
    # "SENDTO 10.0.0.13"
    # "PRINT"
# go to router prompt


# prompt logic implementation
    # print a prompt and wait for user input
    # router prompt 'routeroo> ' will await "ADD" "DELETE" "SEND" or "PRINT" commands 
    # identify user input with case statement? catch errors and re-prompt
    # execute methods accordingly, the methods should not print, only return data
    # seperate add, delete, modify, and print methods created in routing_functions.py

