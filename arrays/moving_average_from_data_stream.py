class MovingAverage(object):
    def __init__(self, size):
        # Have a queue of numbers representing the current window
        self.window = []
        # Store the window size as a float so we can have real division
        self.size = float(size)
        # Store the avg in the current window
        self.avg = 0
        # Sum of all numbers in window
        self.sum = 0

    def next(self, val):
        # Always add new val
        self.window.append(val)
        # Always increase sum by new value
        self.sum += val
        if (len(self.window) <= self.size):
            self.avg = self.sum / float(len(self.window))
        else:
            # Need to pop the front since currently we have self.size+1
            self.sum = self.sum - self.window.pop(0)
            self.avg = self.sum / float(self.size)

        return self.avg