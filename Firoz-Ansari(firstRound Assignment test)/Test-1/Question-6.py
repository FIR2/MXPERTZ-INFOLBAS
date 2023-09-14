# INPUT MATRIX----------------
X = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
      
    ]

Y = [
     [9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]
    ]

# Initialize a sum matrix with zero
sum = [ 
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
      ]

# Iterate through rows and columns to perform element-wise addition
for i in range(len(X)):
    for j in range(len(X[0])):
        sum[i][j] = X[i][j] + Y[i][j]

# Display the result matrix
for row in sum:
    print(row)
