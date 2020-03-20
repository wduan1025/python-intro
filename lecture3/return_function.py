def lazy_sum(k):
    def get_power_sum(x):
        return sum([i ** k for i in x])
    return get_power_sum

f = lazy_sum(2)
g = lazy_sum(3)
print(f)
print(f([1,2,3]))
print(g([1,2,3]))