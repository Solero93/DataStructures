# Class that represents a Heap object
class Heap(object):
  def __init__(self):
    self.container = [] # Representation of the Heap as a list

  # Returns the heap as a list
  def getContainer(self):
    return self.container

  # Inserts a value into the correct position
  def insert(self, val):
    length = len(self.container)
    self.container.append(val) # append it to the end of the list
    self.bubbleUp(length) # find its place up

  # Finds the place of a value once inserted
  def bubbleUp(self, pos):
    if pos == 0: # if we are out of values, we end recursion
      return
    parent = self.getParent(pos) # we get the parent
    if self.container[pos] > self.container[parent]:
      self.exChange(pos, parent) # while the children is less than its father, we exchange them
      self.bubbleUp(parent) # we call the function with the parent

  # Finds the parent of a node
  def getParent(self, pos):
    if pos % 2 == 0:
      return (pos-2)/2
    else:
      return (pos-1)/2

  # Removes the largest element of the heap
  def remove(self):
    deleted = self.container[0] # we store the value to delete
    self.container[0] = self.container.pop() # we place the last element as root
    self.bubbleDown(0) # Move that element down to its place
    return deleted # Return the deleted element

  # Finds the place of a value once deleted
  def bubbleDown(self, pos):
    children = self.getChildren(pos)
    # No child
    if children == []:
      return
    # One child
    elif len(children) == 1:
      if self.container[children[0]] > self.container[pos]:
        self.exChange(children[0], pos)
        self.bubbleDown(children[0])
    # Two children
    else:
      left = self.container[children[0]]
      right = self.container[children[1]]
      root = self.container[pos]
      if left > root or right > root:
        if left > right:
          self.exChange(children[0], pos)
          self.bubbleDown(children[0])
        else:
          self.exChange(children[1], pos)
          self.bubbleDown(children[1])

  # Exchanges two nodes
  def exChange(self, p1, p2):
    tmp = self.container[p1]
    self.container[p1] = self.container[p2]
    self.container[p2] = tmp

  # Gets the children of a parent node
  def getChildren(self, pos):
    length = len(self.container)
    if length <= (2*pos+1):
      return []
    elif length == (2*pos+2):
      return [2*pos+1]
    else:
      return [2*pos+1, 2*pos+2]