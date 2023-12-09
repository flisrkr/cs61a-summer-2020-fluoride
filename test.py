def memo(f):
    cache={}
    def cached_f(*args):
        if args not in cache:cache[args]=f(*args)
        return cache[args]
    return cached_f

class Tree:
    def __init__(self,label,branches=[]):
        self.label=label
        self.branches=[]
        for branch in branches:
            assert isinstance(branch,Tree)
            self.branches+=[branch]

@memo
def fib_tree(n):
    assert n>=0
    if n<=1:return Tree(n)
    left,right=fib_tree(n-1),fib_tree(n-2)
    return Tree(left.label+right.label,[left,right])