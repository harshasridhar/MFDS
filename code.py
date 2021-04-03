# A space optimized python3 program to
# print optimal parenthesization in
# matrix chain multiplication.

print_message=""
def printParenthesis(m, j, i ):
	global print_message

	# Displaying the parenthesis.
	if j == i:

		# The first matrix is printed as
		# 'A', next as 'B', and so on
		print_message += str(chr(65+j))
		#print(chr(65 + j), end = "")
		return;
	else:
		#print("(", end = "")
		print_message += "("

		# Passing (m, k, i) instead of (s, i, k)
		printParenthesis(m, m[j][i] - 1, i)

		# (m, j, k+1) instead of (s, k+1, j)
		printParenthesis(m, j, m[j][i])
		print_message += ")"
		#print (")", end = "" )

def matrixChainOrder(p, n):
	global print_message

	# Creating a matrix of order
	# n*n in the memory.
	m = [[0 for i in range(n)]
			for i in range (n)]

	for l in range (2, n + 1):
		for i in range (n - l + 1):
			j = i + l - 1

			# Initializing infinity value.
			m[i][j] = float('Inf')
			#print('i={}, j={}'.format(i+1,j+1))
			print_message +='i={}, j={}\n'.format(i+1,j+1)
			min_index=-1
			for k in range (i, j):
				q = (m[i][k] + m[k + 1][j] +
					(p[i] * p[k + 1] * p[j + 1]));
				#print('\tk={}, m[{}][{}]+m[{}][{}]+(p{}*p{}*p{})={}+{}+{}={}'.format(k+1,i+1,k+1,k+2,j+1,i,k+1,j+1,m[i][k],m[k+1][j],p[i]*p[k+1]*p[j+1],q))
				print_message +='\tk={}, m[{}][{}]+m[{}][{}]+(p{}*p{}*p{})={}+{}+{}={}\n'.format(k+1,i+1,k+1,k+2,j+1,i,k+1,j+1,m[i][k],m[k+1][j],p[i]*p[k+1]*p[j+1],q)
				if (q < m[i][j]):
					m[i][j] = q

					# Storing k value in opposite index.
					m[j][i] = k + 1
					min_index=k+1
			#print('Min is {}, for k={}'.format(m[i][j],min_index))
			print_message += '   Min is {}, for k={}\n'.format(m[i][j],min_index)
	return m;
def main(arr):
	global print_message
	print_message = ""
	# Driver Code
	#arr = [4, 10, 3, 12, 20,7]
	n = len(arr) - 1

	m = matrixChainOrder(arr, n) # Forming the matrix m

	#print("Optimal Parenthesization is: ", end = "")
	print_message += "Optimal Parenthesization is: "

	# Passing the index of the bottom left
	# corner of the 'm' matrix instead of
	# passing the index of the top right
	# corner of the 's' matrix as we used
	# to do earlier. Everything is just opposite
	# as we are using the bottom half of the
	# matrix so assume everything opposite even
	# the index, take m[j][i].
	printParenthesis(m, n - 1, 0)
	print_message += "\n"
	#print()
	print_message += str(m)
	#print(m)
	#print("\nOptimal Cost is :", m[0][n - 1])
	print_message += "\nOptimal Cost is: {}".format(m[0][n-1])
	# This code is contributed by Akash Gupta.
	return print_message

#print(main([4,10,3,12,20,7]))

