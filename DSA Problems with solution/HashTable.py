# Hash table data structure that python use to create the dictionary
# In this we have a key we find the index using that key and store the key value pair in the list

# Maximum size of the dataset
MAX_SIZE = 5000


# Function which will convert the string into the index
def get_idx(data, key):
    result = 0

    # Loop- we take each character find its ASCII code add them into result and
    # then finally we divide that with the length of list and the remainder of that division will act as a key'''
    for a_char in key:
        a_num = ord(a_char)
        result += a_num

    return result % len(data)

# Defining more suitable get_index function so that there will be a less collision
def valid_idx(data, key):
    # Index using normal idx function
    idx= get_idx(data, key)

    # Now check whether the given idx is empty or have a value in it
    while True:
        # values store at the index
        kvpair = data[idx]

        if kvpair is None:
            return idx

        if kvpair[0] == key:
            return idx
        idx += 1
        # If index reaches to the end of the data then
        if idx == len(data):
            idx = 0


# Basic class for the hash table which perform insertion, deletion, updation and so on
class Hashtable():
    def __init__(self, MAX_SIZE):
        self.keyvalue = [None] * MAX_SIZE

    # Function to insert the value
    def insert(self, key, value):
        # Getting index
        idx = valid_idx(self.keyvalue, key)
        # Storing the value in the given index
        self.keyvalue[idx] = (key, value)

    # Function to update the values
    def update(self, key, value):
        # getting the index of exisiting key
        idx = valid_idx(self.keyvalue, key)
        # Store the new value in the hash table
        self.keyvalue[idx]= (key, value)

    # Function to delete the existing key value pair
    def delete(self, key):
        # Getting the key
        idx = valid_idx(self.keyvalue, key)
        # Delete the value present value in the given key
        self.keyvalue[idx] = None

    # Function the find the value of the given key
    def find(self, key):
        # Getting the index
        idx = valid_idx(self.keyvalue, key)
        kv = self.keyvalue[idx]

        return None if kv[1] is None else kv[1]

    # Function to list all the index of hash table
    def listall(self):
        return [kv[0] for kv in self.keyvalue if kv is not None]


# Creating the hash table with 3085 spaces in it
phone_data = Hashtable(3085)

# Inserting some elements in the hash table
phone_data.insert('Lakshay', '9205105032')
phone_data.insert('Mehar', '9312397337')
phone_data.insert('Om', '9205105032')
phone_data.insert('Puneet', '8364883636')
phone_data.insert('Aakansha', '9845976315')
phone_data.insert('Tanu', '9874563210')
phone_data.insert('listen', '78')
phone_data.insert('silent', '156')

# Finding the values of particular key
print(phone_data.find('Aakansha'))

# Updating the value of the element in hash table
phone_data.update('Aakansha', '9856231470')
print('New Values: ',phone_data.find('Aakansha'))

# Delete the element from the hash table
pair = phone_data.find('Tanu')
print('Value which we are deleting: {} , {} '.format(pair[0], pair[1]))
phone_data.delete('Tanu')

# Listing all the keys of the hash table
print(phone_data.listall())

# Check weathe there is more colloision of the hash key
print('listen:', phone_data.find('listen'))
print('silent: ', phone_data.find('silent'))
