import random
import pandas as pd

from generating_csv import address

address_class = address()


address = []
is_address = []
non_address = []
is_non_address = []


for i in range(1000):
    address.append(address_class.creating_random_address())
    is_address.append(1)
    non_address.append(address_class.creating_non_adddress())
    is_non_address.append(0)



actuall_add = list(zip(address,is_address))
actuall_nonadd = list(zip(non_address,is_non_address))

mixed_data = actuall_add + actuall_nonadd

random.shuffle(mixed_data)


shuffled_data = mixed_data

df = pd.DataFrame(shuffled_data)
df.to_csv("shuffled_data.csv",index=False)
print("done")



















