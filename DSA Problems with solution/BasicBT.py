# Basic structure of tree
class treenodes:
    def __init__(self, key, left= None, right= None):
        self.key= key
        self.left= left
        self.right= right

# User class which help us to create the user obect with parameters like (name, email, phone number)
class User():
    def __init__(self, name, email, phone_num):
        self.name= name
        self.email= email
        self.phone_no= phone_num

    def __repr__(self):                      # __repr__ function is used to represent the object as a string
        return "User(Name: {}, Email_ID: {}, Phone_number: {})".format(self.name, self.email, self.phone_no)

    def __str__(self):                       # __str__ function is used to represent the object as a string
        return "Name: {}, Email_ID: {}, Phone_number: {}".format(self.name, self.email, self.phone_no)

if __name__ == '__main__':
    # Some objects of user class
    vishal = User('vishal',  'vishal@example.com', 9874563)
    hemanth = User('hemanth', 'hemanth@example.com', 78965)
    jadhesh = User('jadhesh', 'jadhesh@example.com',741258)
    siddhant = User('siddhant', 'siddhant@example.com',8564123)
    users= [vishal, hemanth, jadhesh, siddhant]
    print(users)

# Class to store the user in the database and perform some operation on the data
class UserDatabases():
    def __init__(self):
        self.users= []

    def insert(self, user):
        position= 0
        while position < len(self.users):
            if self.users[position].name < user.name:
                break
            position += 1
        self.users.insert(position, user)

    def update_reset(self, user):
        target= self.find_name(user.name)
        target.name, target.email, target.phone_no= user.name, user.email, user.phone_no

    def update_name(self, user):
        target= self.find_email(user.email)
        target.email, target.phone_no = user.email, user.phone_no

    def find_email(self, email):
        for user in self.users:
            if user.email == email:
                return user

    def find_name(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def alluser(self):
        return self.users

# Creating the object of the user database
database = UserDatabases()

# Inserting some user class object into the database
database.insert(vishal)
database.insert(hemanth)
database.insert(jadhesh)
database.insert(siddhant)

# Performing some operation on the items present in the database
user= database.find_name('vishal')
print(user)

database.update_reset(User(name= 'vishal', email= 'vishalgola@gmail.com', phone_num= 987456302))
print(vishal)

# Now lets create the nodes for the formation of tree
node0= treenodes(3)
node1= treenodes(4)
node2= treenodes(10)

# Lets connnect this node
node1.left= node0
node1.right= node2
tree0= node1

# Printing the element of the tree
print(tree0.left.key, tree0.key, tree0.right.key)


