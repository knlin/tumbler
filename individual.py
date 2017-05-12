import random, math
from random import Random

convert_gender_flag = False
verbose_flag = False

def convert_gender(gender):
    if gender.lower() == 'male':
        return 0
    if gender.lower() == 'female':
        return 1
    else:
        raise Exception("For simplicity's sake, please use only 'male' or 'female'.")

class Individual():
    def __init__(self, id, gender, hotness=None, threshold=None, distance=None, seed=None):
        if distance is None:
          distance = 0.1
        if seed is None:
          seed = Random(10001)
        self.id = id
        self.gender = convert_gender(gender) if convert_gender_flag else gender
        self.x = self.y = 0.0
        if hotness is None:
          hotness = seed.uniform(0,1)
        if threshold is None:
          threshold = seed.uniform(0,1)
        self.hotness = hotness
        self.threshold = threshold
        self.matches = []
        self.right_swipes = []
        self.left_swipes = []
        self.distance = distance
        self.seed = seed
    def __str__(self):
        if verbose_flag == True:
            return('person #{} is {}. Currently lives at ({},{}). Has hotness:{} and threhold:{}, \
                and the current list of matches {}, has right swiped {} and left swiped {}'.format(self.id, 
                                    self.gender, self.x, self.y, 
                                     self.hotness, self.threshold,self.matches,
                                    self.right_swipes, self.left_swipes))
        else:
            return("User ID:        {:>10}\n" \
                   "Gender:         {:>10}\n" \
                   "Position: ({:.4}, {:.4})\n" \
                   "Hotness:        {:>10.4}\n" \
                   "Threshold:      {:>10.4}\n" \
                   "Matches:        {:>10}\n" \
                   "Right swipes:   {:>10}\n" \
                   "Left swipes:    {:>10}\n".format(
                        self.id,
                        self.gender,
                        self.x, self.y,
                        self.hotness, self.threshold,
                        self.matches, self.right_swipes, self.left_swipes))
    def get_id(self):
        return(self.id)
    def get_gender(self):
        return(self.gender)
    def pos(self):
        return(self.x, self.y)
    def get_hotness(self):
        return(self.hotness)
    def move(self, x=None, y=None):
        if x is None:
          x = self.seed.uniform(0,1)
        if y is None:
          y = self.seed.uniform(0,1)
        self.x = x
        self.y = y
    def get_threshold(self):
        return(self.threshold)
    def get_matches(self):
        return(self.matches)
    def get_left_swipes(self):
        return(self.left_swipes)
    def get_right_swipes(self):
        return(self.right_swipes)
    def distance_between(self, v1, v2):
        (x1,y1) = self.pos()
        return math.sqrt((x1 - v1)**2 + (y1 - v2)**2)
    def profile(self):
        return(self.id, self.gender, self.x, self.y, self.hotness, self.threshold)
    def swipe(self, id, gender, x, y, hotness, threshold):
        if self.distance_between(x,y) <= self.distance and self.gender != gender:
            if hotness >= self.threshold and id not in self.right_swipes and id not in self.matches:
                self.right_swipes.append(id)
                if self.hotness >= threshold:
                  self.matches.append(id)
            elif id not in self.left_swipes and id not in self.right_swipes and id not in self.matches:
                self.left_swipes.append(id)
    def swipe(self, other):
        if self.distance_between(other.x, other.y) <= self.distance and self.gender != other.gender:
            if other.hotness >= self.threshold and other.id not in self.right_swipes and other.id not in self.matches:
                self.right_swipes.append(other.id)
                if self.hotness >= other.threshold:
                    self.matches.append(other.id)
            elif other.id not in self.left_swipes and other.id not in self.right_swipes and other.id not in self.matches:
                self.left_swipes.append(other.id)
    def add_match(self, id):
        self.matches.append(id)

def main():
    myRandom = Random(111)
    p1 = Individual(1, 'male', seed=myRandom)
    p2 = Individual(2, 'female', seed=myRandom)
    p3 = Individual(3, 'female', seed=myRandom)

    print(p1)
    print(p2)
    print(p3)
    (a, b, c, d, e, f) = p2.profile()
    # x.swipe(a,b,c,d,e,f)
    p1.swipe(p2)
    (a, b, c, d, e, f) = p3.profile()
    # x.swipe(a,b,c,d,e,f)
    p1.swipe(p3)
    print(p1)
    p1.move()
    print(p1)

if __name__ == '__main__':
    main()
