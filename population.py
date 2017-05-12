import individual as ind
import numpy as np
import pandas as pd
import random
from random import Random
class population():
	def __init__(self, ratio, n, seed = None, distance = None):
                if distance is None:
                  distance = 0.1
                if seed is None:
                  seed = Random(10001)
		self.length = n
		self.ratio = ratio
		self.stack = np.empty( (n), dtype = object)
                self.seed = seed
                self.distance = distance
		for i in range(n):
			if i < ratio * n:
				gender = 'male'
			else:
				gender = 'female'
			self.stack[i] = ind.individual(i, gender, seed = seed, distance = distance)
	def as_df(self):
          all = pd.DataFrame()
          for i in range(self.length):
              row = {}
              #return(self.person_id, self.gender, self.x, self.y, self.hotness)
              (row['id'], row['gender'], row['x'], row['y'], row['hotness'], row['threshold']) = self.stack[i].profile()
              #row['threshold'] = self.stack[i].get_threshold()
              row['matches'] = ",".join(str(x) for x in self.stack[i].get_matches())
              row['left_swipes'] = ",".join(str(x) for x in self.stack[i].get_left_swipes())
              row['right_swipes'] = ",".join(str(x) for x in self.stack[i].get_right_swipes())
              all = all.append(row, ignore_index = 1)
          return(all)
	def new_day(self, move_x = None, move_y = None):
          #new day, decide to move people
          for i in range(self.length):
            self.stack[i].move(move_x, move_y)
        def seek_profiles(self):
          for i in range(self.length):
            for j in range(self.length):
              if i!=j:
                (a, b, c, d, e,f) = self.stack[j].profile()
                self.stack[i].swipe(a,b,c,d, e,f)
        def add_profile(self, gender, hotness = None, threshold = None,
            distance = None, seed = None, move = True,  move_x = None, move_y = None):
            if distance is None:
              distance = self.distance
            if seed is None:
              seed = self.seed
            temp = ind.individual(self.length, gender, hotness, threshold,
                distance, seed)
            if move:
              temp.move(move_x, move_y)
            self.stack.append(temp)
            self.length = self.length + 1
def main():
  test = population(0.5 , 1000, distance = 0.1)
  test.new_day()
  test.seek_profiles()
  print(test.as_df().head())
  test.as_df().to_csv('temp.csv')

if __name__ == '__main__':
  main()
