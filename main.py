from generating_csv import abc

a = abc()
a.creating_random_address()

address = []
is_address = []
for i in range(1000):
    address.append(a.creating_random_address())
    is_address.append(1)

actuall_add = list(zip(address,is_address))






