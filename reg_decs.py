registry = []

def register(func):
    print("appending function:",func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1")

@register
def f2():
    print('Running f2')

def f3():
    print('Running f3')

def main():
    print('running main')
    print('reg ->',registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()
