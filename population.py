import individual as ind
import numpy as np
import pandas as pd

class population():
	def __init__(self, ratio, n):
		self.length = n
		self.ratio = ratio
		self.stack = np.empty( (n), dtype = object)
		for i in range(n):
			if i < ratio * n:
				gender = 'male'
			else:
				gender = 'female'
			self.stack[i] = ind.individual(i, gender)
	def as_df(self):
		all = pd.DataFrame()
		for i in range(self.length):
			row = {}
			#return(self.person_id, self.gender, self.x, self.y, self.hotness)
			(row['id'], row['gender'], row['x'], row['y'], row['hotness']) = self.stack[i].profile()
			row['threshold'] = self.stack[i].get_threshold()
			row['matches'] = ",".join(str(x) for x in self.stack[i].get_matches())
			row['left_swipes'] = ",".join(str(x) for x in self.stack[i].get_left_swipes())
			row['right_swipes'] = ",".join(str(x) for x in self.stack[i].get_right_swipes())
			all = all.append(row, ignore_index = 1)
		return(all)
	def new_dat(self):
		

test = population(0.5 , 10)
print(test.as_df())
