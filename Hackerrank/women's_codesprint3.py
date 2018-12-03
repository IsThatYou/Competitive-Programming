##!/bin/python3
#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/hackathon-shirts
#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/choosing-recipes
import math
import sys
#sys.stdin = open("in","r")
def hackathon_shirts():
	t = int(input())

	for case in range(t):
	    n = int(input())
	    guests = map(int, input().split())
	    guests = sorted(guests)
	    m = int(input())
	    ranges = []
	    for i in range(m):
	        b,e = map(int, input().split())
	        ranges.append((b,1))
	        ranges.append((e,2))
	    
	    ranges = sorted(ranges)

	    ans = 0
	    j = 0
	    start = 0
	    start_point = 0
	    for cr in ranges:
	        if cr[1]==1:
	            if start==0:
	                start_point = cr[0]
	            start=start+1
	        if cr[1]==2:
	            start=start-1
	        if start==0:   #a group of overlapped ranges ended
	            end_point = cr[0]
	            while j<n and guests[j]<=end_point:
	                if guests[j]>=start_point:
	                    ans = ans + 1
	                j = j + 1
	        
	    
	    print(ans)
def choosing_recipes():
	q = int(input().strip())
	for a0 in range(q):
	    r,p,n,m = input().strip().split(' ')
	    r,p,n,m = [int(r),int(p),int(n),int(m)]
	    pantry = list(map(int, input().strip().split(' ')))
	    cost = list(map(int, input().strip().split(' ')))
	    recipe = []
	    for recipe_i in range(r):
	       recipe_t = [int(recipe_temp) for recipe_temp in input().strip().split(' ')]
	       recipe.append(recipe_t)
	    rec = []
	    for a1 in recipe:
	    	count = 0
	    	for i in range(len(a1)):
	    		if i not in pantry:
	    			count+=a1[i]*cost[i]
	    	rec.append(count)
	    print(rec)

choosing_recipes()