import random


def random_list(lenth):

    with open('random.txt', 'w') as f:
        l = [str(random.randint(0,lenth)) for _ in range(lenth)]
        f.write(",".join(l))


def reverse_list(lenth):
    name = "./arrays/reverse_{}.txt".format(lenth)
    with open(name, 'w') as f:
        l = [str(lenth - i) for i in range(lenth)]
        f.write(",".join(l))

random_list(50)
X = [100*i for i in range(1,11)]

l = [reverse_list(i) for i in X]