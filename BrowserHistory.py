class Node(object):
    def __init__(self,val = 0 ,pre = None ,next = None) :
        self.val = val
        self.next = next
        self.pre = pre

class BrowserHistory(object):
    def __init__(self, homepage) :
        self.head = self.current = Node(val = homepage)
    
    def visit(self, url):
        new_node = Node(url)
        self.current.next = new_node
        new_node.pre = self.current
        self.current = self.current.next

    def back(self, steps):
        while(steps > 0 or self.current.pre != None):
            steps -= 1
            self.current = self.current.pre
        return self.current.val
    def forward(self, steps):
        """
        :type steps : int
        :rtype : str
        """
        while(steps > 0 or self.current.next != None):
            steps -= 1
            self.current = self.current.next
        return self.current.val
bh = BrowserHistory("naver")
bh.visit("google")
bh.visit("daum")
bh.visit("instagram")
bh.back(1)
bh.forward(2)