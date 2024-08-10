# the generators work by using "yield" and "next" keywords 

# when we run the generator using the next keyword the generator
# function runs form the "yield" that was last executed and runs 
# through the logic of the code until it encounters another yield

# each yield (logically each yield) only runs once 
# here is a little exmaple that prove point not 2
# 
def each_logical_yield_only_runs_once(n):

    yield("this is 1st yield"+n)

    n+="2"
    yield("this is 2nd yield"+n)

    n+="3"
    yield("this is 3rd yield"+n)

    n+="4"
    yield("this is 4th yield"+n)

chained = each_logical_yield_only_runs_once("1")

print(chained)

print(next(chained))

print(next(chained))

print(next(chained))

print(next(chained))