# Scientific Computing with Python
# Probability Calculator
# prob_calculator.py
import random
import copy

class Hat:

    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            #print(f"{key}: {value}")
            for i in range(balls[key]):
                self.contents.append(key)

    def draw(self,ndraws):
        drawBalls = []
        allBalls = copy.deepcopy(self.contents)
        for i in range(ndraws):
             rball = random.choice(allBalls)
             allBalls.remove(rball)
             drawBalls.append(rball)
        drawBalls.sort()
        return drawBalls

def dict2list(d):
    lst = []
    [lst.append(k) for (k, v) in d.items() for i in range(v)]
    lst.sort()
    return lst

def list2dict(l):
    dit = {}
    l.sort()
    dit = dict.fromkeys(l, 0)

    for i in range(len(l)):
        if l[i] in dit:
            dit[l[i]] +=1
    return(dit)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # convert expected ball dictionary to list
    lst = dict2list(expected_balls)
    # convert expected ball list to dictionary
    ebList = list2dict(lst)
    # kind of expected balls
    noEballs = len(list(ebList.keys()))
    # counter of expected ball
    eballCnt = 0
    # no. of successful draw
    success = 0
    # Probability
    prob = 0

    drawnList = {}
    #dit = list2dict(lst)
    for i in range(num_experiments):
        drawnList = list2dict(hat.draw(num_balls_drawn))
        #print(ebList, " <--> ", drawnList)
        for (k, v) in ebList.items():
            if k in drawnList:
                if (drawnList[k] >= ebList[k]):
                    eballCnt +=1
                else:
                    eballCnt = 0
                    continue
            else:
                continue
        if eballCnt == noEballs:
            #print(drawnList)
            success +=1
        eballCnt = 0
    prob = "{:.4f}".format(success/num_experiments)
    print("[Probability]: " + prob + " (" + str(success) + "/" + str(num_experiments) +")\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():

    prob1 = 0
    prob2 = 0
    prob3 = 0
    prob4 = 0

    hat1 = Hat(yellow=3, blue=2, green=6)
    print("Case 1")
    print("[Balls]: yellow=3, blue=2, green=6; \n[Draw]: yellow=1, green=1 \n[Balls drawn]: 2 \n[Attempts]: 100")
    prob1 = experiment(hat1, expected_balls={"yellow":1,"green":1}, num_balls_drawn=2, num_experiments=100)

    hat2 = Hat(red=5, orange=4)
    print("Case 2")
    print("[Balls]: red=5, orange=4; \n[Draw]: red=1, orange=1 \n[Balls drawn]: 3 \n[Attempts]: 500")
    prob2 = experiment(hat2, expected_balls={"red":1,"orange":1}, num_balls_drawn=3, num_experiments=500)

    print("Case 3")
    print("[Balls]: red=5, orange=4, black=1 \n[Draw]: red=1, green=1 \n[Balls drawn]: 4 \n[Attempts]: 1,000")
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    prob3 = experiment(hat3, expected_balls={"red":1,"green":1}, num_balls_drawn=4, num_experiments=1000)

    print("Case 4")
    print("[Balls]: black=6, red=4, green=3 \n[Draw]: red=2, green=1 \n[Balls drawn]: 5 \n[Attempts]: 2,000")
    hat4 = Hat(black=6, red=4, green=3)
    prob4 = experiment(hat4, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)

if __name__ == "__main__":
    main()
