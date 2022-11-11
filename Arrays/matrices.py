import numpy as np


def create_matrices():
    try:
        n = int(input("Enter size: "))
        arr1 = np.full((n, n), 0)
        arr2 = np.full((n, n), 0)
        return populate_matrices(arr1, n), populate_matrices(arr2, n)
    except ValueError:
        print("Invalid Input. Try again!")
        n = int(input("Enter size: "))
        arr1 = np.full((n, n), 0)
        arr2 = np.full((n, n), 0)
        return populate_matrices(arr1, n), populate_matrices(arr2, n)


def populate_matrices(arr, n):
    for i in range(n):
        for j in range(n):
            try:
                value = int(input(f"Enter value {[j+1]} for row {[i+1]}: "))
                arr[i][j] = value
            except ValueError:
                print("Invalid Input. Try again!")
                value = int(input(f"Enter value {[j + 1]} for row {[i + 1]}: "))
                arr[i][j] = value
        print(" ")
    return arr


def add_matrices(arr1, arr2):
    n = len(arr1)
    print(n)
    resultant = np.full((n, n), 0)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            resultant[i][j] = arr1[i][j] + arr2[i][j]
    return resultant


def multiply_matrices(arr1, arr2):
    resultant = np.full((len(arr1), len(arr1)), 0)
    i1, j1 = 0, 0
    i2, j2 = 0, 0
    value = 0
    while i1 < len(arr1):
        if j1 > len(arr1[i1])-1:
            resultant[i1][j2] = value
            value = 0
            j1, i2 = 0, 0
            j2 += 1
        if j2 > len(arr2[i2])-1:
            i1 += 1
            j1, i2, j2 = 0, 0, 0
        if i1 == len(arr1):
            break
        value += arr1[i1][j1] * arr2[i2][j2]
        j1 += 1
        i2 += 1
    return resultant


def sum_right_diagonals(arr1, arr2):
    i = 0
    diagonal_matrix = np.full((len(arr1), 1), 0)
    while i < len(arr1):
        diagonal_sum = arr1[i][i] + arr2[i][i]
        diagonal_matrix[i][0] = diagonal_sum
        i += 1
    return diagonal_matrix


def sum_left_diagonals(arr1, arr2):
    i = 0
    j = len(arr1)-1
    diagonal_matrix = np.full((len(arr1), 1), 0)
    while i < len(arr1):
        diagonal_sum = arr1[i][j] + arr2[i][j]
        diagonal_matrix[i][0] = diagonal_sum
        i += 1
        j -= 1
    return diagonal_matrix


def average_matrice(arr):
    arr_length = arr.size
    arr_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr_sum += arr[i][j]
    return arr_sum / arr_length


def average_of_both_matrices(arr1, arr2):
    no_of_elements = arr1.size * 2
    sum_of_elements = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            sum_of_elements += arr1[i][j] + arr2[i][j]
    return sum_of_elements / no_of_elements


array1, array2 = create_matrices()
print(f"Array 1:\n {array1}\n")
print(f"Array 2:\n {array2}\n")
