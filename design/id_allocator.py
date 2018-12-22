from bitarray import bitarray

class id_allocator():

    def __init__(self, size):
        self.ids = bitarray(size) # 0 is available, 1 is unavailable

    def alloc(self):
        for idx, _id in enumerate(self.ids):
            if not _id:
                self.ids[idx] = True
                return idx
        raise Exception('no ids available')

    def release(self, _id):
        if _id > len(self.ids) or self.ids[_id] == True:
            raise Exception('invalid id')
        self.ids[_id] = False

# Without bit array
class IdAllocator():
    
    def __init__(self, size):
        self.free_ids = set(range(size))
        self.used_ids = set()

    def alloc(self):
        try:
            id = self.free_ids.pop()
            self.used_ids.add(id)
            return id

        except KeyError:
            raise Exception('No id available')

    def release(self, id):
        if id in self.used_ids:
            self.used_ids.remove(id)
            self.free_ids.add(id)