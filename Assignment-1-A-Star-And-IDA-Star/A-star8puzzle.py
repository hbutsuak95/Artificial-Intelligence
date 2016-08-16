
# To solve 8 puzzle problem using A*
from heapq import heappush, heappop
from random import shuffle
import time
import copy
import numpy as np
import sys
import random

sys.setrecursionlimit(1500000)
# node_expanded = 0

def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)
print " Assignment 2  ( Programming Language Used : Python )  Author : Kaustubh Mani, Roll No: 13EX20013"
print
INFINITY = 999999999999

def index_2d(l,v):
	for i, x in enumerate(l):
		if v in x:
			return (i, x.index(v))

class State:

	def __init__(self,config,type_heuristic,parent = None,moves = 0):
		self.config = config
		self.parent = parent
		self.goal = [[1,2,3],[8,0,4],[7,6,5]]
		self.moves = moves
		self.type_heuristic = type_heuristic
		# self.h = h(self,type_heuristic)
		# self.f = self.moves + self.h


	def h(self):
		heuristic = 0
		if self.type_heuristic == 0: 
			pass
		if self.type_heuristic == 1: # heuristic of misplaced tiles
			for i in range(3):
				for j in range(3):
					if ((self.config[i][j] != self.goal[i][j]) and (self.config[i][j] != 0)):
						heuristic += 1
		if self.type_heuristic == 2: 
			for i in range(1,9):
				heuristic += abs(index_2d(self.config,i)[0] - index_2d(self.goal,i)[0]) + abs(index_2d(self.config,i)[1] - index_2d(self.goal,i)[1])
		# print "Heuristic is %d" % heuristic
		return heuristic

	def g(self):
		return self.moves

	def f(self):
		return self.h() + self.g()

	def possible_moves(self):

		i,j = index_2d(self.config,0)
		# print "Dfksjfdhkjsg" + str(i)+str(j)

		if i in [1,2]:
			new_config = copy.deepcopy(self.config[:])
			new_config[i][j] , new_config[i-1][j] = new_config[i-1][j] , new_config[i][j]
			yield State(new_config,self.type_heuristic,self,self.moves+1)
 
		if i in [0,1]:
			new_config = copy.deepcopy(self.config[:])
			new_config[i][j] , new_config[i+1][j] = new_config[i+1][j] , new_config[i][j]
			yield State(new_config,self.type_heuristic,self,self.moves+1)

		if j in [1,2]:
			new_config = copy.deepcopy(self.config[:])
			new_config[i][j] , new_config[i][j-1] = new_config[i][j-1] , new_config[i][j]
			yield State(new_config,self.type_heuristic,self,self.moves+1)

		if j in [0,1]:
			new_config = copy.deepcopy(self.config[:])
			new_config[i][j] , new_config[i][j+1] = new_config[i][j+1] , new_config[i][j]
			yield State(new_config,self.type_heuristic,self,self.moves+1)


	def __cmp__(self,other):
		return self.config == other.config

	def __lt__(self, other):
		return self.f() < other.f()

	def __gt__(self, other):
		return self.f() > other.f()

	def __eq__(self,other):
		return self.config == other.config

	def __hash__(self):
		return hash(str(self.config))


class AStar:

	def __init__ (self,initial_state = None,type_heuristic=0):
		self.initial_state = State(initial_state,type_heuristic)
		self.goal = [[1,2,3],[8,0,4],[7,6,5]]

	def trace_path(self,end):
	    path = [end]
	    state = end.parent
	    while state.parent:
	      path.append(state)
	      state = state.parent
	    return path

	def search(self):

		start = time.time()
		OPEN = []
		heappush(OPEN,self.initial_state)
		CLOSED = set()
		nodes_expanded = 0

		while OPEN:
			f = []
			for state in OPEN:
				f.append(state.f())
			node = heappop(OPEN)
			if node.config == self.goal:
				if (node.type_heuristic == 0):
					print "A Star with Heuristic 1 : ha(n)=0; i.e. leading to breadth-first search"
				elif (node.type_heuristic == 1):
					print "A Star with Heuristic 2 : hb(n)=the number of misplaced tiles (excluding the blank tile)"
				elif (node.type_heuristic == 2):
					print "A Star with Heuristic 3 : hc(n)= the sum of the distances of the tiles from their goal positions (excluding the blank tile)"

				end = time.time()
				print "Search time is %f" % float(end-start)
				print "Depth is %d" % node.moves
				print "Number of Nodes expanded are %d" % nodes_expanded
				print "##########################################################################"
				path = self.trace_path(node)
				for i in reversed(path):     # printing the path from initial state to goal state
						print i.config
						print "-->"
				break;
			nodes_expanded += 1
			if nodes_expanded > factorial(9):
				break
			for state in node.possible_moves(): 
				if (state not in CLOSED) or (state not in OPEN):
					heappush(OPEN,state)
			CLOSED.add(node)
		return node.moves


class IDAstar:

	def __init__(self,initial_state,type_heuristic = 0):
		self.initial_state = State(initial_state,type_heuristic = type_heuristic)
		self.goal = [[1,2,3],[8,0,4],[7,6,5]]


	def trace_path(self,end):
	    path = [end]
	    state = end.parent
	    while state.parent:
	      path.append(state)
	      state = state.parent
	    return path

	def search(self):
		start = time.time()
		bound = self.initial_state.h()
		node_expanded = 0
		
		while True:
			t = self.bound_search(self.initial_state,bound,start,node_expanded)
			if t == "Goal Found":
				return 
			if t == INFINITY:
				return "Goal Not Found"
			bound = t 

	def bound_search(self,node,bound,start,node_expanded):
		# print node.config
		if node.f() > bound:
			return node.f()
		if node.config == self.goal:
			if (node.type_heuristic == 0):
				print "IDAStar with Heuristic 1 : ha(n)=0; i.e. leading to breadth-first search"
			elif (node.type_heuristic == 1):
				print "IDAStar with Heuristic 2 : hb(n)=the number of misplaced tiles (excluding the blank tile)"
			elif (node.type_heuristic == 2):
				print "IDAStar with Heuristic 3 : hc(n)= the sum of the distances of the tiles from their goal positions (excluding the blank tile)"

			end = time.time()
			print "Search time is %f" % float(end-start)
			print "Depth is %d" % node.moves
			print "Number of nodes expanded is %d" % node_expanded
			path = self.trace_path(node)
			for i in reversed(path):     # printing the path from initial state to goal state
					print i.config
					print "-->"
			return "Goal Found"
		min_bound = 99999999
		for state in node.possible_moves():
			node_expanded += 1
			t = self.bound_search(state,bound,start,node_expanded)
			if t == "Goal Found":
				return "Goal Found"
			if t < min_bound:
				min_bound = t 
		return min_bound

def num_inversions(l):
	inversions = 0
	for i in range(len(l)-1):
		for j in range(i,len(l)):
			if (l[i] == 0) or (l[j] == 0) :
				continue
			if l[i] > l[j]:
				inversions += 1
	return inversions

def depth_return(node):

	start = time.time()
	OPEN = []
	heappush(OPEN,node)
	CLOSED = set()
	nodes_expanded = 0

	while OPEN:
		f = []
		for state in OPEN:
			f.append(state.f())
		node = heappop(OPEN)
		if node.config == node.goal:
			# if (node.type_heuristic == 0):
			# 	# print "A Star with Heuristic 1 : ha(n)=0; i.e. leading to breadth-first search"
			# elif (node.type_heuristic == 1):
			# 	print "A Star with Heuristic 2 : hb(n)=the number of misplaced tiles (excluding the blank tile)"
			# elif (node.type_heuristic == 2):
			# 	print "A Star with Heuristic 3 : hc(n)= the sum of the distances of the tiles from their goal positions (excluding the blank tile)"

			end = time.time()
			# print "Search time is %f" % float(end-start)
			# print "Depth is %d" % node.moves
			# print "Number of Nodes expanded are %d" % nodes_expanded
			# print "##########################################################################"
			# path = node.trace_path(node)
			# for i in reversed(path):     # printing the path from initial state to goal state
			# 		print i.config
			# 		print "-->"
			break;
		nodes_expanded += 1
		if nodes_expanded > factorial(9):
			break
		for state in node.possible_moves(): 
			if (state not in CLOSED) or (state not in OPEN):
				heappush(OPEN,state)
		CLOSED.add(node)
	return node.moves


count = 1
while (count < 101):
	puzzles = []
	newpuzzle = [1,2,3,4,5,6,7,8,0]
	il = random.choice([0,1])
	if il == 0:
		new = newpuzzle[3:]
		shuffle(new)
		newpuzzle = newpuzzle[:3] + new
	elif il == 1:
		new = newpuzzle[:6]
		shuffle(new) 
		newpuzzle = new + newpuzzle[6:] 
	if newpuzzle in puzzles:
		continue
	if num_inversions(newpuzzle) % 2 != 0:
		# print "TRUE"
		print " Puzzle Not Solvable"
		print newpuzzle
		continue
	puzzle = []
	puzzle.append(newpuzzle[:3])
	puzzle.append(newpuzzle[3:6])
	puzzle.append(newpuzzle[6:]) 
	if depth_return(State(puzzle,type_heuristic = 2)) > 12:
		continue
	else:
		
		print "Puzzle %d" % count
		print puzzle
		puzzles.append(newpuzzle)
		count += 1
		astar = AStar(puzzle,type_heuristic = 2)
		astar.search()
		astar = AStar(puzzle,type_heuristic = 1)
		astar.search()
		astar = AStar(puzzle,type_heuristic = 0)
		astar.search()
		idastar = IDAstar(puzzle,type_heuristic = 0)
		idastar.search()
		idastar = IDAstar(puzzle,type_heuristic = 1)
		idastar.search()
		idastar = IDAstar(puzzle,type_heuristic = 2)
		idastar.search()


		# print " Breadth First Search  and IDA* with heuristic 1 taking a long time to terminate, so this puzzle is ignored "

