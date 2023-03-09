import json, time
import matplotlib.pyplot as plt

def binary_search(array, x, start, end, mid):
    if start > end:
        return False
    print(x, array[mid])
    if array[mid] == x:
        return True
    elif array[mid] < x:
        return binary_search(array, x, mid+1, end, (mid+1+end)//2)
    else:
        return binary_search(array, x, start, mid-1, (start+mid-1)//2)


def main():
    with open('ex2data.json', 'r') as f1:
        array = json.load(f1)

    with open('ex2tasks.json', 'r') as f2:
        search_tasks = json.load(f2)
    
    array_length = len(array)
    end = array[array_length-1]
    midpoints = [0, array_length//3, array_length//2, end]

    process_time = []
    for mid in midpoints:
        start_time = time.time()
        binary_search(array, search_tasks[2], 0, len(array)-1, mid)
        elapsed_time = time.time() - start_time
        process_time.append(elapsed_time)

    print(process_time)
    
    plt.scatter(midpoints, process_time)
    plt.xlabel('Midpoint')
    plt.ylabel('Process Time')
    plt.title('Optimal Midpoints for Binary Search')
    plt.show()

   
if __name__ == "__main__":
    main()
