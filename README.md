# GramSchmidth
A program to find the orthogonal bases of a given matrix with n columns.
The program has two functions: proj and gramSchmidt.
The proj functions takes in 2 parameters as vectors and returns the projection of the second vector onto the first vector
The gramSchmidth functions takes in the matrix with n columns with n>=2 and returns the orthogonal bases of that matrix.

# Modules
numpy: The program uses numpy.dot function in the proj function to return the dot product of parameters in the proj function
sympy: uses the matrix function to make the result of the orthogonal matrix more larger and visuable.
Fraction: this python built in module converts all entries in the matrix to fraction.
