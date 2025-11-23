'''a=int(input("Enter the number:"))
b=a**0.5
print("The square root of the number is:",b)

import math
a=int(input("Enter the number:"))
b=math.sqrt(a)
print("The square root of the number is:",b)

import math
a=int(input("Enter the number:"))
b=math.pow(a,0.5)
print(b)

def primefactors(x):
    print(f"The factors of {x} are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)

primefactors(187)    
def compute_GCD(x, y):

  while(y):

   x, y = y, x % y

  return x

a = 60

b = 48

print ("The gcd of 60 and 48 is : ",end="")

print (compute_GCD(60,48))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # If no two elements were swapped by inner loop, then break
            break
    return arr

# Example usage:
mylist = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(mylist)
print("Sorted list:", sorted_list)

arr = [10,13,97,2,30,45,8]
n = len(arr)
swapped=False
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped=True

print("Sorted array is:", arr)'''
class Vehicle:
    def __init__(self, v_type, v_number):
        self.v_type = v_type  # 'C' for Car, 'B' for Bike, 'T' for Truck
        self.v_number = v_number

    def __str__(self):
        return self.v_type

class Slot:
    def __init__(self):
        self.vehicle = None

    def is_empty(self):
        return self.vehicle is None

class Parking:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.slots = [[Slot() for _ in range(columns)] for _ in range(rows)]

    def park_vehicle(self):
        print("Vehicle types: 1. Car (C), 2. Bike (B), 3. Truck (T)")
        v_type_choice = input("Enter the vehicle type number: ")
        v_type_map = {'1': 'C', '2': 'B', '3': 'T'}
        if v_type_choice not in v_type_map:
            print("Invalid vehicle type.")
            return
        v_type = v_type_map[v_type_choice]
        v_number = input("Enter vehicle number: ").strip()
        if not v_number:
            print("Vehicle number cannot be empty.")
            return
        
        print(f"Available slots: {self.count_empty_slots()}")
        self.show_layout()
        try:
            row = int(input(f"Enter row (1-{self.rows}) to park: ")) - 1
            col = int(input(f"Enter column (1-{self.columns}) to park: ")) - 1
        except ValueError:
            print("Rows and columns must be numbers.")
            return
        
        if not (0 <= row < self.rows and 0 <= col < self.columns):
            print("Invalid slot position.")
            return

        if not self.slots[row][col].is_empty():
            print("Slot is already occupied.")
            return
        
        self.slots[row][col].vehicle = Vehicle(v_type, v_number)
        print(f"Vehicle {v_number} parked at row {row+1} column {col+1}.")

    def remove_vehicle(self):
        v_number = input("Enter vehicle number to remove: ").strip()
        for i in range(self.rows):
            for j in range(self.columns):
                if not self.slots[i][j].is_empty() and self.slots[i][j].vehicle.v_number.lower() == v_number.lower():
                    self.slots[i][j].vehicle = None
                    print(f"Vehicle {v_number} removed from parking.")
                    return
        print("Vehicle not found.")

    def show_layout(self):
        print("Parking Layout:")
        print(" " + " ".join(f"{i+1:2}" for i in range(self.columns)))
        for i, row in enumerate(self.slots):
            row_str = f"{i+1:2} "
            for slot in row:
                if slot.is_empty():
                    row_str += "[ ]"
                else:
                    row_str += f"[{slot.vehicle}]"
            print(row_str)

    def count_empty_slots(self):
        count = 0
        for row in self.slots:
            for slot in row:
                if slot.is_empty():
                    count += 1
        return count

    def start(self):
        while True:
            print("\nMenu:\n1. Park vehicle\n2. Remove vehicle\n3. Show parking layout\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.park_vehicle()
            elif choice == '2':
                self.remove_vehicle()
            elif choice == '3':
                self.show_layout()
            elif choice == '4':
                print("Exiting parking system.")
                break
            else:
                print("Invalid choice. Please enter 1-4.")

def main():
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
    except ValueError:
        print("Rows and columns must be integers.")
        return

    parking = Parking(rows, columns)
    parking.start()

if __name__ == "__main__":
    main()



