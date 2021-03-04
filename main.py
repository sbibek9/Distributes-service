from hashlib import sha256
import time
import src.stub


@src.stub.start
def sendMe():
    transactions = '''
    AgentX->AgentY->250
    Heinz Doofenshmirtz->Agent P->400
     '''
    difficulty = 8
    old_hash ='0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'
    prefix_str = '0'*difficulty
    m = sha256()
    for val in range(10000000):
        text = (str(5) + transactions + old_hash + str(val))
        m.update(bytes(text,"utf-8")) 
        new_hash = m.hexdigest()
        print(f"Hash = {new_hash}\n")
        if new_hash.startswith(prefix_str):
            print(f"Successfull after {val}")
            return new_hash
    else:
        print("Couldn't find the correct hash\n")

