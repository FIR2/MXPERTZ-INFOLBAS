import threading
 
def printCube(n):
    # function to print cube of given num
    print("Cube: {}" .format(n*n*n))
 
 
def printSquare(n):
    # function to print square of given num
    print("Square: {}" .format(n * n))
 
 
    # creating thread
t1 = threading.Thread(target=printSquare, args=(10,))
t2 = threading.Thread(target=printCube, args=(10,))
 
    # starting thread 1
t1.start()
  # starting thread 2
t2.start()
 
    # wait until thread 1 is completely executed
t1.join()
    # wait until thread 2 is completely executed
t2.join()
 
