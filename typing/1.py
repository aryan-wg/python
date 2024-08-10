from typing import List,Dict,Union

Item = Dict(str,Union(str,int))

def do_something()->List[Dict]:
    print("i did something")
    return [{"name":"aryan"},{"name":"kamboj"}]

def returns_an_item(arg1:str, arg2:int)->Item:
    print("this function returns item")
    return {"name":"aryan","surname":3}

