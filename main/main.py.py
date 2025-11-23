class Vehicle:
    def __init__(self, v_type, v_number):
        self.v_type = v_type  
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
            return
        v_type = v_type_map[v_type_choice]
        v_number = input("Enter vehicle number: ").strip()
        if not v_number:
            return
        
        print(f"Available slots: {self.count_empty_slots()}")
        self.show_layout()
        try:
            row = int(input(f"Enter row (1-{self.rows}) to park: ")) - 1
            col = int(input(f"Enter column (1-{self.columns}) to park: ")) - 1
        except ValueError:
            return
        
        if not (0 <= row < self.rows and 0 <= col < self.columns):
            print("Invalid slot position")
            return

        if not self.slots[row][col].is_empty():
            return
        
        self.slots[row][col].vehicle = Vehicle(v_type, v_number)

    def remove_vehicle(self):
        v_number = input("Enter vehicle number to remove: ").strip()
        for i in range(self.rows):
            for j in range(self.columns):
                if not self.slots[i][j].is_empty() and self.slots[i][j].vehicle.v_number.lower() == v_number.lower():
                    self.slots[i][j].vehicle = None
                    return
        print("Vehicle not found.")

    def show_layout(self):
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
                break
            else:

def main():
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
    except ValueError:
        return

    parking = Parking(rows, columns)
    parking.start()

if __name__ == "__main__":
    main()



