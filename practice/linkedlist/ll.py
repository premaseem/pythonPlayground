class n:
    def __init__(self,v):
        self.v=v
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,v):
        nn = n(v)
        if not self.head:
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn

    def append(self,v):
        cn = self.head
        
        while cn.next:
            cn = cn.next
        cn.next = n(v)

    def print(self):
        print()
        nn = self.head
        while nn:
            print(nn.v,end="-")
            nn = nn.next

    def delete(self,v):

        if self.head.v == v:
            self.head = self.head.next
            return

        pn = self.head
        cn = pn.next
        while cn:
            if cn.v == v:
                pn.next = cn.next
            pn = cn
            cn = cn.next
            
    def delete_by_position(self, i):
        if i == 0:
            self.head = self.head.next
            return

        pn = self.head 
        cn = self.head.next
        position = 1
        while cn: 
            if position == i:
                pn.next = cn.next
                return 
            pn = cn 
            cn = cn.next
            position += 1 
        
    def size_itr(self):
        n = self.head
        size = 0
        while n:
            size += 1
            n = n.next
        print("\nsize is")
        print(size)
        return size
    
    def size_rec(self,n):
        if not n:
            return 0
        return 1 + self.size_rec(n.next)

    def swap1(self,k1,k2):
        cn = self.head
        while cn: 
            if cn.v == k1:
                cn.v =  float('inf')
            if cn.v == k2:
                cn.v = k1
            cn = cn.next

        cn = self.head
        while cn:
            if cn.v == float('inf'):
                cn.v = k2
            cn = cn.next

    def swap2(self,k1,k2):
        cn = self.head
        p1 = 0
        p2 = 0
        i = 0
        while cn:
            if cn.v == k1:
                p1 = i
            if cn.v == k2:
                p2 = i
            cn = cn.next
            i += 1

        cn = self.head

        j=0
        while cn:
            if j == p1:
                cn.v = k2
            if j == p2:
                cn.v = k1
            cn = cn.next
            j += 1

    def swap3(self,k1,k2):
        p1 = p2 = None
        pn = self.head
        cn = self.head.next
        if pn.v == k1 or pn.v == k2:
            p1 = pn

        while cn:
            if cn.v == k1:
                p1 = pn
            if cn.v == k2:
                p2 = pn
            pn = cn
            cn = cn.next

        p1.next, p2.next = p2.next,p1.next
        p1.next.next, p2.next.next = p2.next.next,p1.next.next

    def reverse(self):
        pn = None
        cn = self.head
        while cn:
            nxt = cn.next
            cn.next = pn
            pn = cn
            cn = nxt
        self.head = pn
        self.print()


    def reverse_stack(self):
        stk = []
        cn = self.head
        while cn:
            stk.append(cn)
            cn = cn.next

        self.head = stk.pop()
        cn = self.head
        while len(stk) > 0 and cn:
            cn.next = stk.pop()
            cn = cn.next
        cn.next = None
        self.print()

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def sort_merge(self,l1,l2):
        c1 = l1.head
        c2 = l2.head
        new_head = None
        if c1.v <= c2.v:
            new_head = c1
            c1 = c1.next
        else:
            new_head = c2
            c2 = c2.next
        p = new_head
        while c1 and c2:
            if c1.v <= c2.v:
                p.next = c1

                c1 = c1.next
            else :
                p.next = c2
                # p = c2
                c2 = c2.next
            p= p.next

        if c1:
            p.next = c1
        if c2:
            p.next = c2

        print("merged list")
        nn = new_head
        while nn:
            print(nn.v,end="-")
            nn = nn.next
# ll = LinkedList()
# ll.add(10)
# ll.add(9)
# ll.add(8)
# ll.append(100)
# ll.print()
# ll.delete(9)
# ll.print()
# ll.delete_by_position(3)
# ll.print()
# ll.size_itr()
# print(ll.size_rec(ll.head))
# ll.add(110)
# ll.add(19)
# ll.add(18)
# ll.print()
# ll.swap3(18,100)
# ll.add(10)
# ll.add(20)
# ll.add(30)
# ll.add(40)
# ll.print()
# print("reverse")
# ll.reverse_recursive()
# # ll.reverse_stack()
# ll.print()


### Merge 2 linked lists ###

l1 = LinkedList()
l1.add(40)
l1.add(30)
l1.add(20)
l1.add(10)
l1.print()

l2 = LinkedList()
l2.add(45)
l2.add(35)
l2.add(25)
l2.add(15)
l2.print()

l1.sort_merge(l1,l2)

### Merge 2 linked lists ###
