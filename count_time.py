import time
import matplotlib.pyplot as plt

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A
def count_time(n):
    name = "./arrays/reverse_{}.txt".format(n)

    start = time.process_time()

    with open(name, 'r') as f:
        text = f.read()
    A = [float(i) for i in text.split(',')]
    insertion_sort(A)
    print("Done ",n)
    elapsed = (time.process_time() - start)
    print(elapsed)
    return elapsed

if __name__ == '__main__':


    X = [100 * i for i in range(1,11)]
    time_list = []
    for x in X:
        time_list.append(count_time(x)*1000)

    fig, ax = plt.subplots()
    ax.plot(X, time_list, 'o-')
    ax.set_ylabel('time,ms')
    ax.set_xlabel('length')

    plot = plt.plot(X,time_list,'o-')
    plt.show()