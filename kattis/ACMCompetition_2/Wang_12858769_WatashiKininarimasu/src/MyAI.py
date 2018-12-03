# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent
import queue
class MyAI ( Agent ):

    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        
        self.graph = {}
        self.Dir = 1 #right
        self.where = [0,1,2,3]
        self.actions = queue.Queue()
        self.cur = (1,1)
        self.stack = []
        self.visited = set()
        self.track = []
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
        self.n = 99
        self.m = 99
    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        #print("actions:",self.actions)
        #print("cur:",self.cur)
        #print("track:", self.track)
        #print("stacks:",self.stack)
        #print("visited:",self.visited)

        if not self.actions.empty():
            return self.actions.get()
        
        if (breeze or stench):
            self.visited.add(self.cur)
            if (self.cur == (1,1)):
                return Agent.Action.CLIMB
            #print("rua")
            #self.move_left()
            #self.move_left()
            #self.actions.put(Agent.Action.CLIMB)
            self.go_back()
        if bump:
            if self.Dir == 1:
                self.m = self.cur[1]-1
                self.cur = (self.cur[0],self.cur[1]-1)
            if self.Dir == 2:
                self.n = self.cur[0]-1
                self.cur = (self.cur[0]-1,self.cur[1])
        if (glitter):
            self.visited.add(self.cur)
            self.go_back()
            return Agent.Action.GRAB


        if self.cur not in self.visited:
            for i in self.neib(self.cur):
                self.stack.append(i)

        self.visited.add(self.cur)

        if (len(self.stack)==0):
            self.go_back()
            self.actions.put(Agent.Action.CLIMB)
        else:    
            next_node = self.stack.pop()
            self.go_go(next_node)
            self.move_to(next_node)
            self.track.append(self.cur)
            self.cur = next_node
        if not self.actions.empty():
            return self.actions.get()
        
        #return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def neib(self, node):
        result = []
        if ((node[0]+1,node[1]) not in self.visited) and (node[0]+1 <=self.n):
            result.append((node[0]+1,node[1]))
        if ((node[0]-1>= 1) and (node[0]-1,node[1])not in self.visited):
            result.append((node[0]-1,node[1]))
        if ((node[0],node[1]+1) not in self.visited) and (node[1]+1<=self.m):
            result.append((node[0],node[1]+1))
        if ((node[1]-1 >= 1) and ((node[0],node[1]-1) not in self.visited)):
            result.append((node[0],node[1]-1))
        return result
    def go_go(self, node):
        a = abs(self.cur[0] - node[0]) + abs(self.cur[1] - node[1])
        while a > 1:
            self.go_back()
            a -=1
    def go_back(self):
        if (self.cur == (1,1)):
            if (len(self.neib(self.cur)) == 0):
                self.actions.put(Agent.Action.CLIMB)
        else:
            a = self.track.pop()
            self.move_to(a)
            self.cur = a
            b = self.neib(a)
            if (len(b)==0):
                self.go_back()
            else:
                pass
    def move_to(self,next_node):
        if (self.cur[0] - next_node[0]) == 1:
            self.move_down()
        elif (self.cur[0] - next_node[0]) == -1:
            self.move_up()
        if (self.cur[1] - next_node[1]) == 1:
            self.move_left()
        elif (self.cur[1] - next_node[1]) == -1:
            self.move_right()
    def move_up(self):
        if self.Dir == 2:
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 0:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 1:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 3:
            self.actions.put(Agent.Action.TURN_RIGHT)
            self.actions.put(Agent.Action.FORWARD)
        self.Dir = 2
    def move_down(self):
        if self.Dir == 0:
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 2:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 3:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 1:
            self.actions.put(Agent.Action.TURN_RIGHT)
            self.actions.put(Agent.Action.FORWARD)
        self.Dir = 0
    def move_right(self):
        if self.Dir == 1:
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 3:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 0:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 2:
            self.actions.put(Agent.Action.TURN_RIGHT)
            self.actions.put(Agent.Action.FORWARD)
        self.Dir = 1
    def move_left(self):
        if self.Dir == 3:
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 1:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 2:
            self.actions.put(Agent.Action.TURN_LEFT)
            self.actions.put(Agent.Action.FORWARD)
        elif self.Dir == 0:
            self.actions.put(Agent.Action.TURN_RIGHT)
            self.actions.put(Agent.Action.FORWARD)
        self.Dir = 3
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
