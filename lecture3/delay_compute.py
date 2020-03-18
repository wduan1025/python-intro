def delayed_compute(l):
    def some_complicated_computation():
        return sum([2**i for i in l])
    return some_complicated_computation

l = range(3)
f = delayed_compute(l)
print(f)
print(f())