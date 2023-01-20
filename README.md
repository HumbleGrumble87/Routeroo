FIRST

Need to get router modeled, with ability to take a config
as arguement, and wait for user input 


MODEL

- Need interfaces, addressing, and mask
    - interfaces should be a dict
    - key should be interface number
    - value of dict should be a list
    - list contains interface name, address, mask 
    - address needs to be stored as binary for AND mask operation

- Need routing table (keyword table?)
    - how do you model a table?
    - this *could* be an array of arrays?
    - i think the IP addresses need an "order" because
        bitwise operations + search algo = fast/efficient
    - how does the mask work into that then??
    ex. destination 10.0.0.7
        10.0.0.0   /8
        10.0.0.8   /29
    - how will we know to pick the former?
    - the second nearly matches
    -CHECK THE ALGO FFS | IT'S IN THE F!!!ING BOOK
