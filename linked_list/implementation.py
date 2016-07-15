from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        #self.elements = elements
        self.start = None
        self.end = None
        
        if elements:
            e = elements[0]
            n = Node(e)
            self.start = n
            self.end = n
            if len(elements) > 1:
                remaining_elements_range = range(1,len(elements))
                for e in remaining_elements_range:
                    self.append(elements[e])
            

    def __str__(self):
        # string representation str()
        elemlist = []
        readnode = self.start
        if readnode is None:
            return str(elemlist)
        while readnode.next != None:
            elemlist.append(readnode.elem)
            readnode = readnode.next
        elemlist.append(readnode.elem)
        return str(elemlist)
    

    def __len__(self):
        # calculate length of list len()
        return self.count()

    def __iter__(self):
	    iterlist = self.start
	    while iterlist != None:
		    yield iterlist
		    iterlist = iterlist.next
	    raise StopIteration
		
         

    def __getitem__(self, index):
        # get an item based on index x[y]
        
        # make sure we have a valid index
        if type(index) != int:
            raise TypeError("Wrong type given for element index")
        if index >= self.count() or index < 0:
            raise KeyError("Index out of valid range for linked list")

        if index == 0:
            return self.start
        if index == 1:
            return self.start.next

        # start with first item:
        current_node = self.start
        next_node = self.start.next 
        for x in range(0,index - 1):
            current_node = next_node
            next_node = next_node.next
        return next_node
            
    def __add__(self, other):
        newlist = LinkedList()
        for i in self:
            newlist.append(i.elem)
        for i in other:
            newlist.append(i.elem)
        return newlist
        # implements addition +
   

    def __iadd__(self, other):
        if other is None:
            return self
        if len(self) == 0:
            self.start = other.start
            self.end = other.end
        else:
        #print other.end.elem
            self.end.next = other.start
            self.end = other.end
        return self


    def __eq__(self, other):
        # test for equality ==
        if other is None:
            if self is not None:
                return False
            else:
                return True

        if len(self) != len(other):
            return False
        if len(self) == 0:
            return True
        readnode, comparenode = self.start, other.start
        while readnode.next != None:
            if readnode.elem != comparenode.elem:
                return False
            readnode = readnode.next
            comparenode = comparenode.next
        if readnode.elem != comparenode.elem:
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other
        

    def append(self, elem):
        # add a new node to the end .append
        new_node = Node(elem)
        if not self.start:
            self.start, self.end = new_node, new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        # count the total number of nodes 
        count = 0 
        readnode = self.start
        if readnode is None:
            return 0
        while readnode.next != None:
            count += 1
            readnode = readnode.next
        count += 1
        return count    
        

    def pop(self, index=None):
        # remove and return the last node
        # Have to set self.last to second last
        # element and return last element.
        if not self.start:
            raise IndexError("List is empty, nothing to pop")
        if index == None or index == self.count()-1:
            # pop the last element
            if self.count() == 1:
                tmp_node = self.start
                self.start = None
                self.end = None
                return tmp_node.elem
            # first, we need to get 2nd last element
            old_last_node = self.end
            new_last_index = self.count() - 2
            new_last_node = self.__getitem__(new_last_index)
            self.end = new_last_node
            self.end.next = None
            return old_last_node.elem
        if index < 0 or index > self.count()-1:
            raise IndexError("Index out of valid range for linked list") 
        if index == 0:
            node_to_remove = self.__getitem__(index)
            node_after_index = self.__getitem__(index+1)
            self.start = node_after_index
            return node_to_remove
        if index < (self.count()):
            # do the index stuff
            node_before_index = self.__getitem__(index-1)
            node_to_remove = self.__getitem__(index)
            node_after_index = self.__getitem__(index+1)
            node_before_index.next = node_after_index
            return node_to_remove.elem