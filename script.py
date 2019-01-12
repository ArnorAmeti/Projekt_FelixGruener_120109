class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

def get_value(self):
    return self.value

 def get_next_node(self):
    return self.next_node

def set_next_node(self, next_node):
    self.next_node = next_node


class Food_Types:
 def __init__(self, value=None):
    self.head_node = Node(value)

 def get_head_node(self):
    return self.head_node

 def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

 def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

ft = LinkedList("german")
ft.insert_beginning("japanese")
ft.insert_beginning("vegetarian")
ft.insert_beginning("french")

class HashMap:
 def __init__(self, array_size):
  self.array_size = array_size
  self.array = [None for item in range(array_size)]

 def hash(self, key):
  key_bytes = key.encode()
  hash_code = sum(key_bytes)
  return hash_code

  def compressor(self, hash_code):
   return hash_code % self.array_size

  def assign(self, key, value):
   array_index = self.compressor(self.hash(key))
   self.array[array_index] = value

  def retrieve(self, key):
   array_index = self.compressor(self.hash(key))
   return self.array[array_index]

hash_map = HashMap(50)
hash_map.assign('y', 'yes')
hash_map.assign('n', 'no')
hash_map.assign('g', 'german')
hash_map.assign('j', 'japenese')
hash_map.assign('v', 'vegetarian')
hash_map.assign('f', 'french')
