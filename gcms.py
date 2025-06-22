from bin import Bin
from avl import AVLTree
from avl import BinLocatorAVL    
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_locator = BinLocatorAVL()
        self.bins = AVLTree()
        self.objects = AVLTree()
        pass

    def add_bin(self, bin_id, capacity):
        bin = Bin(bin_id, capacity)
        self.bins.insert(bin_id, bin)
        self.bin_locator.insert(bin.capacity, bin.bin_id)
        pass

    def add_object(self, object_id, size, color):
        
        def compact_fit_id(object_id, size, least_id = True):
            if self.bin_locator.size == 0:
                raise NoBinFoundException
            bin = self.bin_locator.min_greater_than_eq(size, least_id)
            if bin is None:
                raise NoBinFoundException
            return bin.value
        
        def largest_fit_id(object_id, size, least_id = True):
            if self.bin_locator.size == 0:
                raise NoBinFoundException
            bin = self.bin_locator.largest(least_id)
            if bin is None:
                raise NoBinFoundException
            return bin.value

        object = Object(object_id, size, color)
        
        if object.color == Color.BLUE:
            bin_id = compact_fit_id(object_id, size, least_id = True)
            self.bins.search(bin_id).add_object(object)
            self.objects.insert(object_id, bin_id)
            prev_capacity = self.bins.search(bin_id).capacity + size
            self.bin_locator.delete(prev_capacity, bin_id)
            self.bin_locator.insert(prev_capacity - size, bin_id)
            
        elif object.color == Color.YELLOW:
            bin_id = compact_fit_id(object_id, size, least_id = False)
            self.bins.search(bin_id).add_object(object)
            self.objects.insert(object_id, bin_id)
            prev_capacity = self.bins.search(bin_id).capacity + size
            self.bin_locator.delete(prev_capacity, bin_id)
            self.bin_locator.insert(prev_capacity - size, bin_id)
            
        elif object.color == Color.RED:
            bin_id = largest_fit_id(object_id, size, least_id = True)
            if self.bins.search(bin_id).capacity < size:
                raise NoBinFoundException
            self.bins.search(bin_id).add_object(object)
            self.objects.insert(object_id, bin_id)
            prev_capacity = self.bins.search(bin_id).capacity + size
            self.bin_locator.delete(prev_capacity, bin_id)
            self.bin_locator.insert(prev_capacity - size, bin_id)
            
        elif object.color == Color.GREEN:
            bin_id = largest_fit_id(object_id, size, least_id = False)
            if self.bins.search(bin_id).capacity < size:
                raise NoBinFoundException
            self.bins.search(bin_id).add_object(object)
            self.objects.insert(object_id, bin_id)
            prev_capacity = self.bins.search(bin_id).capacity + size
            self.bin_locator.delete(prev_capacity, bin_id)
            self.bin_locator.insert(prev_capacity - size, bin_id)
            
        else:
            raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        if self.objects.search(object_id) is None:
            return None
        temp_bin_id = self.objects.search(object_id)
        ini_cap = self.bins.search(temp_bin_id).capacity
        self.bins.search(temp_bin_id).remove_object(object_id)
        final_cap = self.bins.search(temp_bin_id).capacity
        self.bin_locator.delete(ini_cap, temp_bin_id)
        self.bin_locator.insert(final_cap, temp_bin_id)
        self.objects.delete(object_id)
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        curr_cap = self.bins.search(bin_id).capacity
        obj_list = []
        obj_list = self.bins.search(bin_id).bin_objects.inorder()
        tup = (curr_cap, obj_list)
        return tup
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        if self.objects.search(object_id) is None:
            return None
        return (self.objects.search(object_id))
        pass