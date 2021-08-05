import sys, os, math

#Function for determining the circumcircle of any three points
def circumcircle(tri):
	try:
		D = ( (tri[0][0] - tri[2][0]) * (tri[1][1] - tri[2][1]) - (tri[1][0] -  tri[2][0]) * (tri[0][1] - tri[2][1]) )
		
		center_x = (((tri[0][0] - tri[2][0]) * (tri[0][0] + tri[2][0]) + (tri[0][1] - tri[2][1]) * (tri[0][1] + tri[2][1])) / 2 * (tri[1][1] - tri[2][1]) - ((tri[1][0] - tri[2][0]) * (tri[1][0] + tri[2][0]) + (tri[1][1] - tri[2][1]) * (tri[1][1] + tri[2][1])) / 2 * (tri[0][1] - tri[2][1])) / D
		
		center_y = (((tri[1][0] - tri[2][0]) * (tri[1][0] + tri[2][0]) + (tri[1][1] - tri[2][1]) * (tri[1][1] + tri[2][1])) / 2 * (tri[0][0] - tri[2][0]) - ((tri[0][0] - tri[2][0]) * (tri[0][0] + tri[2][0]) + (tri[0][1] - tri[2][1]) * (tri[0][1] + tri[2][1])) / 2 * (tri[1][0] - tri[2][0])) / D
		
		radius = math.sqrt ((tri[2][0] - center_x)**2 + (tri[2][1] - center_y)**2 )
		
		return [[center_x, center_y], radius]
	except:
		print("Divide By Zero error")
		print(tri)


#Determine if any given point lies inside a circle
def pointInCircle(point, circle):
	#This is pretty simple; just find the distance between the point and the center. If it's less than or equal to the radius, the point is inside the circle
	
	d = math.sqrt( math.pow(point[0] - circle[0][0], 2) + math.pow(point[1] - circle[0][1],2) )
	if d < circle[1]:
		return True
	else:
		return False
	
#Basic Point class
class Point():
	def __init__(self, x, y):
		self._x = x
		self._y = y
	
	#Position of the point
	def pos(self):
		return [self._x, self._y]
			
	#Determines if two points are equivalent
	def isEqual(self, other_point):
		if(self._x == other_point._x and self._y == other_point._y): return True
		else: return False
	
	#Convert the point into a string (for debugging purposes)
	def pointToStr(self):
		return str(self.pos())

#Basic Edge class
class Edge():
	def __init__(self, a, b):
		if a is not b:
			self._a = a
			self._b = b
	
	#Tests if two edges are equivalent to each other
	def isEqual(self, other_edge):
		if (self._a.isEqual(other_edge._a) or self._b.isEqual(other_edge._a)) and (self._a.isEqual(other_edge._b) or self._b.isEqual(other_edge._b)):
			return True
		elif self == other_edge:
			return True
		else:
			return False
	
	#Converts an edge to a string (for debugging purposes)
	def edgeToStr(self):
		return str([self._a.pos(), self._b.pos()])
	
	#Calculate the length of an edge
	def length(self):
		return math.sqrt( math.pow(self._b.pos()[0] - self._a.pos()[0],2) + math.pow(self._b.pos()[1] - self._a.pos()[1],2))
	
	#Determine if two edges intersect
	def edgeIntersection(self, other_edge):

		if self.isEqual(other_edge):
			return False
		else:
			try:
				x1 = self._a.pos()[0]
				x2 = self._b.pos()[0]
				x3 = other_edge._a.pos()[0]
				x4 = other_edge._b.pos()[0]
				y1 = self._a.pos()[1]
				y2 = self._b.pos()[1]
				y3 = other_edge._a.pos()[1]
				y4 = other_edge._b.pos()[1]
				t = (((x1 - x3)*(y3 - y4)) - ((y1 - y3)*(x3 - x4))) / (((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4)))
				u = (((x2 - x1)*(y1 - y3)) - ((y2 - y1)*(x1 - x3))) / (((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4)))
				
				#If 0 <= t <= 1 or 0 <= u <= 1, then an intersection occurs. 
				if (t >= 0 and t <= 1) and (u >= 0 and u <= 1):
					int_x = int(x1 + t*(x2 - x1))
					int_y = int(y1 + t*(y2 - y1))
					int_point = Point(int_x, int_y)
					
					#If the intersection point is one of the edge points, then an intersection is not considered to have occurred (i.e., these are edges connected at the same point)
					if self._a.isEqual(int_point) or self._b.isEqual(int_point) or other_edge._a.isEqual(int_point) or other_edge._b.isEqual(int_point):
						return False
					
					#If there is no point, these edges intersect
					else:
						return True
					
				else:
					return False
			except:
				#A divide-by-zero error is interpreted as the edges not intersecting
				return False

#Basic Triangle class
class Triangle():
	
	#Cannot create a triangle if any two points are the same
	def __init__(self, a, b, c):
		if a is not b and a is not c:
			self._a = a
		if b is not a and b is not c:
			self._b = b
		if c is not a and c is not b:
			self._c = c
	
	#Test if any two triangles are equal (defined as sharing all three points)
	def isEqual(self, other_tri):
		if (self._a is other_tri._a or self._a is other_tri._b or self._a is other_tri._c) and (self._b is other_tri._a or self._b is other_tri._b or self._b is other_tri._c) and (self._c is other_tri._a or self._c is other_tri._b or self._c is other_tri._c): return True
		else: return False
	
	#Prints the triangle in a neat format (for debugging purposes)
	def printTriangle(self):
		print("A: " + self._a.pointToStr() + " B: " + self._b.pointToStr() + " C: " + self._c.pointToStr())

#Graph class
class Graph():
	def __init__(self):
		
		#This will be a list of point objects as defined above
		self._points = []
		
		#This will be a list of triangle objects as defined above
		self._triangles = []
		
		#This is a list of edges as defined above
		self._edges = []
		
		#Point boundaries for sorting purposes
		self._point_min_x = 0
		self._point_max_x = 0
		
	def addPoint(self, point):
	
		#Check to see if an equivalent point exists
		for x in self._points:
			if x.isEqual(point): 
				return False
		
		#If the point has an X value lower than any other point
		if self._point_min_x > point.pos()[0] or self._point_min_x == 0:
			self._points.insert(0,point)
			self._point_min_x = point.pos()[0]
			return True
		
		#If the point has an X value higher than any other point
		elif self._point_max_x < point.pos()[0]:
			self._points.append(point)
			self._point_max_x = point.pos()[0]
			return True
		
		#If the X value is somewhere in the middle
		else:
			same_x = []
			for x in self._points:
				if x.pos()[0] == point.pos()[0]:
					same_x.append(x)
			
			#If no point has the same X value as the new point, find the first point that has a greater X value and insert the new point before it
			if len(same_x) == 0:
				first_greater = 0
				for x in self._points:
					if x.pos()[0] > point.pos()[0]:
						first_greater = self._points.index(x)
						break
				self._points.insert(first_greater, point)
				return True
			
			#If there's only one point in the graph with the same X value, compare the Y values to find which order they go in
			elif len(same_x) == 1:
				index = self._points.index(same_x[0])
				if same_x[0].pos()[1] > point.pos()[1]:
					self._points.insert(index - 1, point)
					return True
				else:
					self._points.insert(index + 1, point)
					return True
			
			#If multiple points have the same X value, find where the new point needs to go based on its Y value
			else:
				first_greater_y = 0
				for x in same_x:
					if x.pos()[1] > point.pos()[1]:
						first_greater_y = self._points.index(x)
						break
				if(first_greater_y != 0):
					self._points.insert(first_greater_y, point)
					return True
				else:
					self._points.insert(self._points.index(same_x[len(same_x) - 1]), point)
					return True
		
	def addEdge(self, edge):
		
		#Check for an equivalent edge in the graph, add it if one doesn't exist
		for x in self._edges:
			if x.isEqual(edge):
				return False
		self._edges.append(edge)
		return True
		
	#Adds a triangle to the list of triangles and returns true if successful, checking if it is equal to any other triangle. Returns false if an equivalent triangle exists
	def addTriangle(self, triangle):
		
		#First check if an equivalent triangle already exists
		for x in self._triangles:
			if x.isEqual(triangle): return False
		
		#If not, we can add the triangle to the graph
		self._triangles.append(triangle)
		tri = [ triangle._a.pos(), triangle._b.pos(), triangle._c.pos() ]
		return True
		
	#Tests if a given triangle is Delaunay (i.e., no other points lie within the circumcircle of the triangle)
	def triangleIsDelaunay(self, triangle):
		tri = [ triangle._a.pos(), triangle._b.pos(), triangle._c.pos() ]
		cc = circumcircle(tri)
		for x in self._points:
			#print(x.pos())
			#If we get the divide-by-zero error, we assume the triangle is non-Delaunay
			if not (x.isEqual(triangle._a) and x.isEqual(triangle._b) and x.isEqual(triangle._c)):
				try:
					if pointInCircle(x.pos(), cc):
						return False
				except:
					return False
		#self._circles.append(cc)
		return True
	
	#Generates the complete Delaunay mesh by testing every possible triangle for the Delaunay condition, then marking any edges that intersect, and removing the longer of the intersecting edges
	def generateDelaunayMesh(self):
	
		#Create every possible triangle and test it for the Delaunay condition
		for p1 in self._points:
			for p2 in self._points:
				for p3 in self._points:
					if not p1.isEqual(p2) and not p2.isEqual(p3) and not p3.isEqual(p1):
						test_tri = Triangle(p1,p2,p3)
						if self.triangleIsDelaunay(test_tri):
							self.addTriangle(test_tri)
		
		#One more check for the Delaunay condition (probably redundant) and then adding the edges of the triangle to the graph
		for t in self._triangles:
			if not self.triangleIsDelaunay(t):
				self._triangles.remove(t)
			else:
				self.addEdge(Edge(t._a, t._b))
				self.addEdge(Edge(t._b, t._c))
				self.addEdge(Edge(t._c, t._a))
				
		#Checking for intersecting edges
		bad_edges = []
		for e1 in self._edges:
			for e2 in self._edges:
				if not e1.isEqual(e2):
					if e1.edgeIntersection(e2):
						len_e1 = e1.length()
						len_e2 = e2.length()
						if len_e1 >= len_e2:
							bad_edges.append(e1)
							
						else:
							bad_edges.append(e2)
		
		#Removing any bad (intersecting) edges from the graph
		for x in bad_edges:
			for y in self._edges:
				if x.isEqual(y):
					self._edges.remove(y)
					continue