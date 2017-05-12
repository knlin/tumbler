import random, math
from random import Random

class individual():
    def __init__(self,id, gender, hotness = None, threshold = None, 
                 distance = None, seed = None):
        if distance is None:
          distance = 0.1
        if seed is None:
          seed = Random(10001)
        self.person_id = id
        self.gender = gender
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
        return('person id:{} is {}. Currently lives at ({},{}). Has hotness:{} and threhold:{}, \
            and the current list of matches {}, has left swiped {} and right swiped {}'.format(self.person_id, 
                                self.gender, self.x, self.y, 
                                 self.hotness, self.threshold,self.matches,
                                self.right_swipes, self.left_swipes))
    def get_id(self):
        return(self.person_id)
    def get_gender(self):
        return(self.gender)
    def pos(self):
        return(self.x, self.y)
    def get_hot(self):
        return(self.hotness)
    def move(self, x = None, y = None):
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
        return(self.person_id, self.gender, self.x, self.y, self.hotness, self.threshold)
    def swipe(self, person_id, gender, x, y, hotness, threshold):
        if self.distance_between(x,y)<=self.distance and self.gender != gender:
            if self.threshold >= hotness and person_id not in self.right_swipes and \
                person_id not in self.matches:
                self.right_swipes.append(person_id)
                if self.hotness >= threshold:
                  self.matches.append(person_id)
            elif person_id not in self.left_swipes and person_id not in self.matches and \
                person_id not in self.matches:
                self.left_swipes.append(person_id)
    def add_match(self, person_id):
        self.matches.append(person_id)

def main():
    myRandom = Random(10001)
    x = individual(1,'male', seed = myRandom)
    y = individual(2,'female', seed = myRandom)
    z = individual(3,'female', seed = myRandom)

    print(x)
    print(y)
    print(z)
    (a , b , c, d, e,f) = z.profile()
    x.swipe(a,b,c,d,e,f)
    (a , b , c, d, e,f) = y.profile()
    x.swipe(a,b,c,d,e,f)
    print(x)
    x.move()
    print(x)

if __name__ == '__main__':
    main()



