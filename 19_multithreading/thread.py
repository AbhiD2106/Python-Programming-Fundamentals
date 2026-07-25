#run program or functions parallelly
import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["products" , "customers" , "orders" , "cancel" , "reviews"]

def myfun(i):

        wait = random.randint(1,10)
        time.sleep(wait )
        print(f"i'm {i}.i'm took {wait} sec")

# for i in tables:
#     myfun(i)

#loops are slow so insted of loop we use thread

with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    futures = executor.map(myfun,tables)
        

