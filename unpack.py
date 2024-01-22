def f(*args,**kwargs):
    print("Positional:",*kwargs.keys())

f(galleons=100,sickles=50,knuts=25)