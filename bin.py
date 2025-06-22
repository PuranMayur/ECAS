from avl import AVLTree

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.bin_objects = AVLTree()
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.bin_objects.insert(object.object_id, object)
        self.capacity -= object.size
        object.bin_id = self.bin_id
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        if self.bin_objects.search(object_id) is None:
            return None
        object = self.bin_objects.search(object_id)
        self.capacity += object.size
        self.bin_objects.delete(object_id)
        pass
    