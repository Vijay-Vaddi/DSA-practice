class Linked_list():
    '''creates a basic linked list
    instanciation, append, prepent takes one value 
    :param: <any> value to append/prepend'''
    def __init__(self, value):
        self.head  = { 
                        'data' : value,
                        'next' : None                      
                      }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.newNode = {
                        'data':value,
                        'next':None
        }
        self.tail['next'] = self.newNode
        self.tail = self.newNode
        self.length+=1
        return self
    
    def prepend(self,value):
        self.newNode = {
                        'data' : value,
                        "next" : None
        }
        self.newNode['next'] = self.head
        self.head = self.newNode
        self.length+=1
        return self

    def printList(self):
        list_values = []
        currentNode = self.head

        while (currentNode!=None):
            list_values.append(currentNode['data'])
            currentNode = currentNode['next']
        return list_values

    def insert(self, index, value):
        pass
        for i in range(index):
            pass
            

linked_list = Linked_list(5)
print(linked_list.head['data'])
print(linked_list.append(10))
print(linked_list.prepend(20).head)
print(linked_list.printList())