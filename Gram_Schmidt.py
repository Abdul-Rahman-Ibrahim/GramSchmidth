def proj(v1, v2):
    """Returns the projection of v2 onto v1"""
    coef = np.dot(v2,v1)/np.dot(v1,v1)
    return np.dot(coef, v1)

def gramSchmidt(A):
    """Takes Transpose of a matrix and Returns orthogonal bases of that matrix"""
    orthVectors = []
    j = 1
    for row in A:
        orthVectors.append(row)
        if len(orthVectors) == 1:
            continue
        pro = 0
        for i in range(len(orthVectors)-1):
            pro = np.add(pro, proj(orthVectors[i], row))
            orthVectors[j] = row - pro
            j += 1
    #Converting entries with decimals to fraction
    orthVectors = sp.Matrix(np.array(orthVectors).T)
    for i, val in enumerate(orthVectors):
        frac = Fraction(str(val)).limit_denominator()
        orthVectors[i] = frac
        
    return orthVectors
