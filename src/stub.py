import cloudpickle

def start(func):
    print("Preparing to run\n")
    cloudpickle.dumps(func)
    print("Sending data through pickling")
    func()
    

    
