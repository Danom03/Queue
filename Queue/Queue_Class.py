class Empty(Exception):
    """Error attempting to access element"""
    pass


class Queue:
    """Defining methods for class Queue"""
    default_capacity = 10                                   # Static Variable

    def __init__(self):
        """Declaring instance variable"""
        self._data = [None] * Queue.default_capacity        # To store Queue data
        self._size = 0                                      # This is size of the Queue
        self._front = 0                                     # This is front of the Queue

    def __len__(self):
        """Returns length of the Queue."""
        return self._size

    def is_empty(self):
        """Check whether Queue is empty or not"""
        return self._size == 0

    def first(self):
        """Returns Front element of the Queue."""
        if self.is_empty():
            return Empty("Queue is Empty.")
        return self._data[self._front]

    def dequeue(self):
        """Removes an element from the Queue"""
        if self.is_empty():
            return Empty('Queue is Empty')
        answer = self._data[self._front]                    # Element which will be removed(FIFO)
        self._data[self._front] = None                      # Replacing value by None
        self._front = (self._front + 1) % len(self._data)   # Re-instantiating Front of the Queue
        self._size -= 1                                     # Size - 1 coz 1 element is removed

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def enqueue(self, e):
        if self._size == len(self._data):                   # If Queue is full
            self._resize(2 * len(self._data))               # Double the size of Queue

        avail = (self._front + self._size) % len(self._data)    # Index at which element to be entered
        self._data[avail] = e
        self._size += 1                                     # New element added

    def _resize(self, cap):                                # Assuming cap > default capacity
        old = self._data                                   # Storing already added data in temp var
        self._data = [None] * cap                          # Increasing Size
        walk = self._front                                 # Front of the Old Queue
        for i in range(len(self._data)):
            self._data[i] = old[walk]                      # Adding Data again to new Queue
            walk = (walk + 1) % len(old)
        self._front = 0                                    # Re-instantiating Front
