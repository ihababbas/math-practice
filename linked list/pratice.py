class Node:
    def __init__(self, value):
      self.value = value
      self.next = None


class LinkedList():
  def __init__(self):
    self.head=None

  def append(self,node):
    if self.head is None:
      self.head=node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next=node 
  def __str__(self):
    output=""
    if self.head is None : 
      output = "Empty linked list"
    else :
      current=self.head
      while current : 
        output+=f'{current.value}-->'
        current=current.next
      output+= "None"
    return output
if __name__=="__main__":
  ll = LinkedList()
  a=Node(0)
  b=Node(1)
  c=Node(3)
  d= Node(0)
  e=Node(2)
  f=Node(4)
  g=Node(5)
  h= Node(0)
  ll.append(a)
  ll.append(b)
  ll.append(c)
  ll.append(d)
  ll.append(e)
  ll.append(f)
  ll.append(g)
  ll.append(h)
  print(ll)
  
def margenodes(head):
    sum_list=[]
    new_linked_list = []
    nxt = head.next
    def getvalue(nxt):
        if nxt.value != 0:
            sum_list.append(nxt.value)
            nxt = nxt.next
        if nxt.value == 0 and nxt.next is None:
            f_node = sum(sum_list) 
            new_linked_list.append(f_node) 
            return new_linked_list
        if nxt.value == 0 and nxt.next is not None:
            f_node = sum(sum_list)
            for _ in range(len(sum_list)):
                sum_list.pop()
            new_linked_list.append(f_node)
            nxt = nxt.next
            
        getvalue(nxt)
    getvalue(nxt)
    new_ll = LinkedList()
    for i in range(len(new_linked_list)):
        new_ll.append(Node(new_linked_list[i]))
                
    
    return new_ll  


print(margenodes(a))