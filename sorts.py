#implmenetations of various sorting algorithms
import random

UNSORTED_ARRAY1 =  map((lambda x: random.randint(1, 400)), range(1,1000) )

def genray(n):
  return map((lambda x: random.randint(1, 400)), range(1,n) )


def test_sorted(array):
  i = 0
  size = len(array)
  while(i < size):
    if(i >= 1):
        if(array[i] < array[i-1]):
          return False
    i = i + 1
  return True

def cmp(a, b):
    if (a == b):
        return 0
    elif (a > b):
        return 1
    else:
        return -1


def swap(i, j, array):
    swapv = array[i]
    array[i] = array[j]
    array[j] = swapv
    return array

def biggest(array):
    i = 0
    biggest_val = array[0]
    biggest_index = i
    while(i < len(array)):
        if (array[i] > biggest_val):
            biggest_val = array[i]
            biggest_index = i
        i = i + 1
    return (biggest_index, biggest_val)

def minv(array, start_index):
    i = start_index
    min_val = array[start_index]
    min_index = i
    while(i < len(array)):
        if (array[i] < min_val):
            min_val = array[i]
            min_index = i
        i = i + 1
    return (min_index, min_val)

def min(array):
    return minv(array, 0)

def selectionSort(array):
    i = 0
    array1 = array
    while (i < len(array1)):
        array1 = swap(i, minv(array1, i)[0], array1)
        i = i + 1
    return array1


def gapSort(array, gap):
    """helper function to aid insertion sort and shell sort"""
    i = 0
    array1 = array
    while (i < len(array)):
        if (i > 0):
            j = i
            while ((cmp(array1[j], array1[j-gap]) < 0) and (j != 0 ) ):
                #while object at i is less than the one before it
                swap(j, j-gap, array1)
                j = j - 1
        i = i + 1
    return array1

def insertionSort(array):
    return gapSort(array, 1)



def shellSort(array):
    """sorts using the shellsort algorithm"""
    vals = [3*h+1 for h in range(len(array)/3)][::-1]
    for val in vals:
        array = gapSort(array, val)
    return array


#merge sort
def merge(array, p, q, r):
    if ((r - p) > 1):
        left = array[p:q+1]
        loggr("left" + str(left))
        right = array[q+1:r+1]
        loggr("right"+ str(right))
        left.append('c')
        right.append('c')
        i = 0
        j = 0
        for k in range(p, r+1):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
    elif ((r - p) == 1 ):
        if (array[r] < array[p]):
            i = array[p]
            j = array[r]
            array[p] = j
            array[r] = i



def mergeSort(array):
    def sort(p, r, msg):
        #loggr(array)
        #loggr("p = "+ str(p) + ' r = '+ str(r) + " array[p]: " + str(array[p])+ " array[r] " + str(array[r]))
        #loggr(msg)
        if p < r:
            q = (p+r)/2
            if (r - p) > 1:
                #loggr("q = " + str(q) + " array[q] =  " + str(array[q]))
                sort(p, q, "in left array")
                #loggr([p, q])
                sort(q+1, r, "right array")
            #loggr([q, r])
            #loggr("merging")
            merge(array, p, q, r)
            #loggr(array)
    sort(0, len(array)-1, "root")
    return array




def loggr(data):
    f = open('./log.dat', 'a')
    f.write(str(data) + '\n')
    f.close()

