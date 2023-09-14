# --------------------Method Overloading---------------------------------

class Calculator:
    def add(self, a, b=0):
        return a + b

# Creating object of the Calculator class
calc = Calculator()

# Call the add method with different arguments
result1 = calc.add(5)
result2 = calc.add(5, 3)

print("Result 1:", result1)
print("Result 2:", result2)








# -------------------  Method Overriding --------------------------------
# Parent Class
# class A:
#     def first(self):
#         print("First function of class A")

#     def second(self):
#         print('Second function of class A')

# # Derived Class
# class B(A):
#     # Overriden Function
#     def first(self):
#         print("Redefined function of class A in class B")

#     def display(self):
#         print('Display Function of Child class')

# # Driver Code
# # if(__name__ == "__main__"):
#     # Creating child class object
# child_obj = B()
    
#     # Calling the overridden method
# print("Method Overriding\n")
# child_obj.first()
    
#     # Calling the original Parent class method
#     # Using parent class object.
# A().first()
