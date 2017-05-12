import random, math

class individual():
    def __init__(self,id, gender):
        self.person_id = id
        self.gender = gender
        self.x = self.y = 0.0
        self.hotness = random.uniform(0,1)
        self.threshold = random.uniform(0,1)
        self.matches = []
        self.right_swipes = []
        self.left_swipes = []
        self.distance = 0.1
    def __str__(self):
        return('person id:{} is {}. Currently lives at ({},{}). Has hotness:{} and threhold:{},    and the current list of matches {}, has left swiped {} and right swiped {}'.format(self.person_id, 
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
    def move(self, x = random.uniform(0,1), y = random.uniform(0,1)):
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
        return(self.person_id, self.gender, self.x, self.y, self.hotness)
    def swipe(self, person_id, gender, x, y, hotness):
        if self.distance_between(x,y)<=self.distance and self.gender != gender:
            if self.threshold >= hotness and person_id not in self.right_swipes and \
                person_id not in self.matches:
                self.right_swipes.append(person_id)
            elif person_id not in self.left_swipes and person_id not in self.matches and \
                person_id not in self.matches:
                self.left_swipes.append(person_id)
    def add_match(self, person_id):
        self.matches.append(person_id)

def main():
    random.seed(10001)
    x = individual(1,'male')
    y = individual(2,'female')
    z = individual(3,'female')

    print(x)
    print(y)
    print(z)
    (a , b , c, d, e) = z.profile()
    x.swipe(a,b,c,d,e)
    (a , b , c, d, e) = y.profile()
    x.swipe(a,b,c,d,e)
    print(x)
    x.move()
    print(x)

if __name__ == '__main__':
    main()



