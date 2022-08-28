from imp import reload
import hello

for i in range(5):
    reload(hello)

a = hello.add(4, 5)
print(a)
reload(hello)

sample = {1:'coffee', 2:'tea'}
for x in sample:
    print(x)    