
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,a):
        self.queue.append(a)
    def dequeue(self):
        if self.empty():
            return "Empty"
        else:
            return self.queue.pop(0)
    def peek(self):
        return queue[0]
    def empty(self):
        return len(self.queue)==0
    def length(self):
        return len(self.queue)
class node:
    def __init__(self,x,y,num):
        self.x,self.y=x,y
        self.num=num
class graph:
    def __init__(self):
        self.graph={}
    def addnode(self,node,adjacent):
        self.graph.update({node:adjacent})
    def bfs(self,root,targetnode):
        visited={}
        for i in self.graph:
            visited.update({i:i==root})
        q=queue()
        q.enqueue(root)
        parentmap={}
        while q.queue:
            currentnode=q.dequeue()
            if (currentnode)==(targetnode):
                return self.pathreconstruct(parentmap,targetnode,root)
            for i in self.graph[currentnode]:
                if not visited[i]:
                    q.enqueue(i)
                    visited[i]=True
                    parentmap.update({i:currentnode})
    def pathreconstruct(self,parentmap,targetnode,root):
        currentnode=targetnode
        path=[]
        while currentnode != root:
            path.append(currentnode)
            currentnode=parentmap[currentnode]
        path.append(root)
        return path

g=graph()
node1=node(0,0,1)
node2=node(1,0,2)
node3=node(2,0,3)
node4=node(0,1,4)
node5=node(1,1,5)
node6=node(2,1,6)
node7=node(0,2,7)
node8=node(1,2,8)
node9=node(2,2,9)
g.addnode(node1,[node2,node4])
g.addnode(node2,[node1,node3,node5])
g.addnode(node3,[node2,node6])
g.addnode(node4,[node1,node5])
g.addnode(node5,[node2,node4,node6,node8])
g.addnode(node6,[node3,node5,node9])
g.addnode(node7,[node4,node8])
g.addnode(node8,[node5,node7,node9])
g.addnode(node9,[node6,node8])
for i in g.bfs(node3,node7):
    #print(i.x,i.y)
    print(i.num,end=" ")