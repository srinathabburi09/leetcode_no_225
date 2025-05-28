class MyStack:

    def __init__(self):
        self.q1 = []                                          
        self.q2 = []
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
    def pop(self) -> int:
        return self.q1.pop(0)
    def top(self) -> int:
        return self.q1[0]
    def empty(self) -> bool:
        return len(self.q1) == 0

#Explanation -->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # example test case :
#s = MyStack()
#s.push(1)   --> q2 = [1] 
#q1 = [] there are no elements in q1 while loop fails and changing q1 = q2 and q2 = q1 so, q1 = [1] and q2 = []
#s.push(2) --> q2 = [1,2]
#after pushing q2 = [2] and q1 consists of elements, it enters the while loop and the popping element at the index 0 that is first element will be append to the q2, in while loop q1 = [], and q2 = [2,1] we attains LIFO behaviour in this case(stack behaviour)
#and we interchange = q1 = [2,1] and q2 = []
#s.push(3)
#and same process continues q2 = [3] and q1 = [2,1], q1 enters the while loop, POPs the first element and append it to q2 and q2 becomes = [3,2,1] lifo behaviour
#and we exchange q1 = [3,2,1] and q2 = []
# so we do q2 as an empty to queue is because to allow appending elementing should be placed at top to perform LIFO
#print(s.top())   # Should print 3
#q1's first element will be stacks top element
#print(s.pop())   # Should print 3
#q1's first element will be the popping element as to perfrom as a stack
#print(s.top())   # Should print 2
#print(s.empty()) # Should print False
# if the len(q1) == 0 : return True else: return false,we check only for the q1 because q2 always remains empty





# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

