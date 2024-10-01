```python
import numpy
import scipy

S = lambda vec: get_screw_matrix(vec)
I = lambda n: numpy.identity(n)
N = lambda G: numpy.atleast_2d(nullspace(G))[:,0]
# Questa definizionde della funzione N, è quasi sicuramente
# sbagliata

def main():
	d_1 = numpy.array([-2,  0,  0])
	d_2 = numpy.array([ 2, -1,  0])
	d_3 = numpy.array([ 2,  1,  0])

	W_ext = transpose(numpy.array([0,-10,0,0,0,0]))
	G = construct_grasp_matrix(d_1, d_2, d_3)

	# Definizione di zeta, la pongo a 0, perchè non ho idea di
	# cosa stia a significare e come definirla
	zeta_coefficent = 0
	zeta_form = numpy.diag(numpy.ones((G.shape[1])))
	zeta = zeta_coefficent*zeta_form

	print('is_full_rank(G):', is_full_rank(G), '\n')
	print('grasp matrix: G =\n', G, '\n')
	print('nullspace(G):\n', nullspace(G), '\n')
	print('N(G):\n', N(G), '\n')
	print('Check nullspace: G@N(G) == 0?\n', G@N(G), '\n')
	print('pseudoinverse(G)@(-W_ext):\n', pseudoinverse(G)@(-W_ext), '\n')
	print('N(G)@zeta:\n', N(G)@zeta, '\n')

	F_C = pseudoinverse(G)@(-W_ext) + transpose(N(G)@zeta)

	F_c1, F_c2, F_c3 = F_C[0:3], F_C[3:6], F_C[6:9]
	print('F_c1:\n', F_c1, '\n')
	print('F_c2:\n', F_c2, '\n')
	print('F_c3:\n', F_c3, '\n')



def construct_grasp_matrix(*args) -> numpy.array:
	S = get_screw_matrix
	I = numpy.identity
	cols = list()
	G = None
	for vec in args:
		col = numpy.vstack((I(3), S(vec)))
		cols.append(col)
	G = numpy.hstack(cols)
	return G



def transpose(matrix: numpy.array) -> numpy.array:
	return numpy.atleast_2d(matrix).T



def get_screw_matrix(vector: numpy.array) -> numpy.array:
	shp = vector.shape
	assert shp == (3,) or shp == [1, 3] or shp == [3, 1]

	v_x, v_y, v_z = vector[0], vector[1], vector[2]
	screw_matrix = numpy.array([
		[0   , -v_z, v_y  ],
		[v_z , 0   , -v_x ],
		[-v_y, v_x , 0    ],
	])
	return screw_matrix



def is_full_rank(matrix: numpy.array) -> numpy.array:
	rank = numpy.linalg.matrix_rank(matrix)
	return rank == min(matrix.shape)



def nullspace(matrix: numpy.array,rcond=1e-14, decimals=7) -> numpy.array:
    ns = scipy.linalg.null_space(matrix, rcond)
    if ns.size == 0:
        return numpy.atleast_2d(numpy.zeros((matrix.shape[1],1)))
    ns = ns * numpy.copysign(1, ns[0,0])   # Remove the sign ambiguity of the vector
    return numpy.round(ns, decimals)


def pseudoinverse(matrix: numpy.array, decimals=7) -> numpy.array:
	pinv_matrix = numpy.linalg.pinv(matrix)
	return numpy.round(pinv_matrix, decimals)



if __name__ == '__main__': main()

```