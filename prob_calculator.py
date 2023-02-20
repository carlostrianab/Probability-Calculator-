import copy
import random
# Consider using the modules imported above.


class Hat:

  contents = []
  
  
  
  #Initializes the hat class, creates a contents array of strings with the balls on the hat
  def __init__(self, **args):
    partial_list = []
    for arg in args:
      element_counter = args[arg]
      while element_counter > 0:
        partial_list.append(arg)
        element_counter = element_counter - 1
    self.contents = partial_list
    
  
  def draw(self, number):

    
    popped_balls = []
    deep_copy = copy.deepcopy(self.contents)
    
    
    if number >= len(self.contents):
      popped_balls = self.contents
    else:
      
      number_counter = number
      while number_counter > 0:
        random_number = random.randint(0, len(self.contents) - 1)
        popped_balls.append(self.contents.pop(random_number))
        number_counter = number_counter - 1
      self.contents = deep_copy
        
    
        
    return popped_balls

  

#Function to calculate the probability of getting a set array of drawn balls, depending on the number and color of initial balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  meets_condition = 0
  experiments = num_experiments

  while experiments > 0:
    balls_drawn = hat.draw(num_balls_drawn)
    meets_condition_counter = 0

    for ball in expected_balls:
      ball_counter = 0
      for element in balls_drawn:
        if element == ball:
          ball_counter += 1

      if ball_counter >= expected_balls[ball]:
        meets_condition_counter += 1

    if meets_condition_counter == len(expected_balls):
      meets_condition += 1

    experiments = experiments - 1

  probability = meets_condition / num_experiments

  return probability


hat = Hat(blue=4, red=2, green=6)

#Testing the functions 
print('Showing hat contents')
print(hat.contents)
print('Printing the drawn balls')
print(hat.draw(2))


e_balls = {"blue":2, "red":1}
num_balls = 5
num_experiments = 100
print('The probability of having ' + str(e_balls['blue']) + ' blue balls and ' + str(e_balls['red']) + ' red ball drawn from our hat is ')
print(experiment(hat,e_balls,num_balls,num_experiments))



