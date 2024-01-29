def fun(*arg,**kwargs):
    print(type(arg))
    print(arg)
    print(type(kwargs))
    print(kwargs)
dict = {"1":"hi","2":"hello"}
fun(*"yogee",**dict)