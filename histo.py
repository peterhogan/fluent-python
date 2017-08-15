from random import betavariate as bv,seed
#seed(231012)
letters = 'abcdefghijklmnopq'
betas = tuple(round(bv(6,5)*10,5) for i in range(15**2))
lookup = {}
print('Length of betas:',len(betas))
print('Max betas:',max(betas))
print('Min betas:',min(betas))
for b in betas:
    for let in letters:
        if letters[round(b)-1] == let:
            lookup.setdefault(let, []).append(b)
for i in letters:
    try:
        print('#'*len(lookup[i]))
    except KeyError:
        print('')
