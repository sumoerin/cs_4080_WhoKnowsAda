import os
import time


start = time.time()

for x in range(32):
    start = time.time()
    os.system("scala DynamicBufferCommands < bigbible.txt")
    print(time.time() - start)
