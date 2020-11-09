import ase.io

NACL = ase.io.read("nacl.cif", None)

x = NACL.get_atomic_numbers()
print (x)
print (len(x))

y = NACL.get_positions()
print (y[3])
print (y)
print (len(y))
print (y[3,2])