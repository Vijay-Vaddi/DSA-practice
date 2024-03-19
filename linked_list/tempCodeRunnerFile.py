class Linked_list():

    def __init__(self, value):
        self.head  = { 'value' : value,
                        'next' : None                      
                      }
        self.tail = self.head