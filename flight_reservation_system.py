from collections import deque
import hashlib
import heapq

def string_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

def email_hash(s):
    return hashlib.sha512(s.encode()).hexdigest()

def customer_hash(s):
    return email_hash(string_hash(string_hash(s)))


customer_map = {
    "customer1": [string_hash("password1"), email_hash("customer1@example.com"), "John", "Doe"],
    "customer2": [string_hash("password2"), email_hash("customer2@example.com"), "Jane", "Smith"],
    "customer3": [string_hash("password3"), email_hash("customer3@example.com"), "Bob", "Johnson"],
}

states = ['Kochi', 'Trivandrum', 'Chennai', 'Pune', 'Bengaluru', 'Hyderabad', 'Aurangabad', 'Coimbatore',
          'Visakhapatnam', 'Kolkata', 'Delhi', 'Lucknow', 'Agra']


def check_customer_credentials(customer_id, password, email):
    if customer_id in customer_map:
        hashed_password, hashed_email, _, _ = customer_map[customer_id]
        if hashed_password == string_hash(password) and hashed_email == email_hash(email):
            return True
    return False


def get_customer_list():
    customer_list = [(last_name, first_name, customer_id) for customer_id, (_, _, first_name, last_name) in customer_map.items()]
    heapq.heapify(customer_list)
    return customer_list

def signup():
    customer_id = input("Enter customer ID: ")
    password = input("Enter password: ")
    email = input("Enter email address: ")
    if customer_id in customer_map:
        print("Customer ID already exists!")
        return
    hashed_password = string_hash(password)
    hashed_email = email_hash(email)
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    customer_map[customer_id] = [hashed_password, hashed_email, first_name, last_name]
    print("Signup successful!")


def booking(path, departure, arrival):
    cost_per_place = 500
    total_cost = (len(path) - 1) * cost_per_place
    print("Total charge from", states[departure], 'to', states[arrival], "is Rs", total_cost)
    print('Have a safe trip')

def bfs(places, departure, arrival):
    queue = deque()
    visited = []
    queue.append([departure])

    while queue:
        path = queue.popleft()
        current_place = path[-1]

        if current_place == arrival:
            return path

        if current_place not in visited:
            visited.append(current_place)

            for destination in range(len(places)):
                if places[current_place][destination] == 1 and destination not in visited:
                    new_path = path + [destination]
                    queue.append(new_path)

    return None

places = [
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

def airportmap():
    print('Airports in the Network :')
    for i in range(len(states)):
        print(i, ' ', states[i])

    while True:
        departure = int(input('Enter the departure place in index format: '))
        if 0 <= departure < len(states):
            break
        print('Invalid input! Please enter a valid index.')

    while True:
        arrival = int(input('Enter the arrival place in index format: '))
        arrival = int(arrival)
        if 0 <= arrival < len(states):
            break
        print('Invalid input! Please enter a valid index.')

    print('Departure place:', states[departure])
    print('Arrival place:', states[arrival])
    path = bfs(places, departure, arrival)
    if path:
        print('Path:', ' -> '.join(states[place] for place in path))
        if len(path) == 2:
            print('Direct flight')
        else:
            print('Indirect flight')
        num_of_flights = len(path) - 1
        print('Number of flights:', num_of_flights)
    else:
        print('No path found')

    while True:
        choice = input('Do you want to book the ticket yes/no : ')
        if choice == 'yes':
            booking(path, departure, arrival)
            break
        elif choice == 'no':
            print('exiting')
            break
        else:
            print('Enter an valid input')

while True:
    print("1. Customer login")
    print("2. Signup")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        customer_id = input("Enter customer ID: ")
        password = input("Enter password: ")
        email = input("Enter email address: ")
        if check_customer_credentials(customer_id, password, email):
            print("Access granted")
            airportmap()
        else:
            print("Access denied")
    elif choice == "2":
        signup()
    elif choice == "3":
        break
    else:
        print("Invalid choice")