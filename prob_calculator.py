import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ballType in kwargs:
            for x in range(0, kwargs[ballType]):
                self.contents.append(ballType)

    def draw(self, number):
        ballsDrawn = []
        if number > len(self.contents):
            ballsDrawn = self.contents
            self.contents = []
        else:
            for x in range(0, number):
                ballToDraw = random.randint(0, len(self.contents) - 1)
                ballsDrawn.append(self.contents.pop(ballToDraw))
        return ballsDrawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successfulExperiments = 0
    for expIndex in range(1, num_experiments):
        experimentHat = copy.deepcopy(hat)
        drawnBalls = experimentHat.draw(num_balls_drawn)
        expResults = []
        for expectedBall in expected_balls:
            expResults.append(drawnBalls.count(expectedBall)>=expected_balls[expectedBall])
        if expResults.count(False) == 0:
            successfulExperiments = successfulExperiments + 1

    print(str(successfulExperiments), str(num_experiments))

    result = successfulExperiments/num_experiments
    result = round(result, 2)

    return result

