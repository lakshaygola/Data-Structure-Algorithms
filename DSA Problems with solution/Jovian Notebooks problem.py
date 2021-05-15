'''Problem statement: - In the we have to write the function which able to sort the coding notebooks which already store
                        in Jovian platform we have to sort them according to likes given on the notebook or the username
                        or many be on other features as well. We have to write the effective version of the algorithms so
                        it work fast on millions of user notebooks.'''

# Function to print the list
def display_list(obj):
    for i in obj:
        print(i)


# Class which create the object in which we have like, username, title of the notebook which store in jovian
class Notebook():
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes= title, username, likes

    def __repr__(self):
        return "Notebook <'{}'/'{}'> '{}' likes".format(self.username, self.title, self.likes)


# Function to compare the objects
def default_compare(obj1, obj2):
    if obj1 > obj2:
        return 'lesser'
    elif obj1 < obj2:
        return 'greater'
    else:
        return 'equal'


# Function to compare the likes of the notebooks
def likes_comparsion(obj1, obj2):
    if obj1.likes > obj2.likes:
        return 'lesser'
    elif obj1.likes < obj2.likes:
        return 'greater'
    else:
        return 'equal'


# Function to sort the notebooks basis on the username
def user_comparsion(obj1, obj2):
    if obj1.username < obj2.username:
        return 'lesser'
    elif obj1.username > obj2.username:
        return 'greater'
    else:
        return 'equal'


# Function to apply merge sort of the notebooks
def merge_sort(notebooks, compare_func= default_compare):
    if len(notebooks) < 2:
        return notebooks

    mid= len(notebooks) // 2

    sorted_notebooks= merge(merge_sort(notebooks[:mid], compare_func), merge_sort(notebooks[mid:], compare_func), compare_func)

    return sorted_notebooks


def merge(left, right, compare= default_compare):
    i, j, merged_list = 0, 0, []
    while i < len(left) and j < len(right):
        result= compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    return merged_list + left[i:] + right[j:]


nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks= [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]
print('All the Notebooks that platform have in random orders: ')
display_list(notebooks)
print('\nNotebooks sorted according to the likes given on the notebooks: \n')
sorted_notebooks= merge_sort(notebooks, likes_comparsion)
display_list(sorted_notebooks)