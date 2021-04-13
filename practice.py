#runtime analysis is all about how your prolem grows 

def print_one_item(items):
    print(items[0])

#Linear
def print_every_item(items):   
    for item in items:
        print(item)            

#number of items 
#number of steps
#all about relationship number of items vs number of steps 



def print_pairs(items):  
    for item_one in items:
        for item_two in items: 
            print(item_one, item_two)



def do_a_bunch_of_stuff(items):
    last_idx = len(items) = 1