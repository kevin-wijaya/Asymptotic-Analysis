# Apply Big O Notation
# Made by : Kevin Wijaya
# -------------------------------
# Orders of common functions
# -------------------------------
# O(1)        : constant function
# O(log n)    : logarithmic function
# O(n)        : linear function
# O(n^2)      : quadratic function
# O(2^n)      : exponential function
# O(n^k)      : polynomial function
# O(n!)       : factorial function

import matplotlib.pyplot as plt
import math

class big_oh:
  def __init__(self, n=0):
    self.name = '' # name fucntion (ex: constant function)
    self.function = '' # expression (f(n) = ?)
    self.size = [] # input (n)     ---> [1, 2 , 3, ..., n]
    self.time = [] # itertaion (N) ---> [y1, y2, y3, , ..., yn] 
    self.n = n

  def plot(self):
    plt.figure(figsize=(5, 5))
    plt.plot(self.size, self.time)
    plt.xlabel('n - size / input')
    plt.ylabel('N - time / iteration')
    plt.title(self.name)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.show()

  def plot_all(self, temp_list):
    plt.xlabel('n - size / input')
    plt.ylabel('N - time / iteration')
    plt.title('All type')
    for i in temp_list:
      plt.plot(i.size, i.time, label=i.name)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.legend(loc='upper right', frameon=False)
    plt.show()

  def convert_string(self, string):
    string = string
    string = string.replace('log', ' math.log')
    string = string.replace('^', '**')
    if '!' in list(string):
      i = list(string).index('!')
      n = (list(string)[0:i]) 
      n = ''.join(n)
      string = string.replace('!', '')
      string = string.replace(n, f' math.factorial({n}) ')

    return string

  def function_to_time(self):
    temp_list = []
    for i in self.size:
      expression = self.function.replace('n', str(i))
      try:
        result = eval(self.convert_string(expression))
      except Exception as e:
        result = None  
      temp_list.append(result)
    self.time = temp_list

  def constant(self, n):
    self.name = 'Constant Function - O(1)'
    self.function = '1'
    self.size = [*range(n)]
    self.time = [i for s in [[int(self.function)]*(len(self.size))] for i in s]

  def logarithmic(self, n):
    self.name = 'Logarithmic Function - O(log n)'
    self.function = 'log(n,2) + 2'
    self.size = [*range(n)]
    self.function_to_time()

  def linear(self, n):
    self.name = 'Linear Function - O(n)'
    self.function = 'n + 2'
    self.size = [*range(n)]
    self.function_to_time()

  def quadratic(self, n):
    self.name = 'Quadratic Function - O(n^2)'
    self.function = 'n^2 + 2'
    self.size = [*range(n)]
    self.function_to_time()

  def polynomial(self, n, k=3):
    self.name = 'Polynomial Function - O(n^k) {k=3}'
    self.function = 'n^k + 2'.replace('k', str(k))
    self.size = [*range(n)]
    self.function_to_time()

  def exponential(self, n):
    self.name = 'Exponential Function - O(2^n)'
    self.function = '2^n + 2'
    self.size = [*range(n)]
    self.function_to_time()

  def factorial(self, n):
    self.name = 'Factorial Function - O(n!)'
    self.function = 'n! + 2'
    self.size = [*range(n)]
    self.function_to_time()

# -------------------------------
# Just to speed up the plot
# -------------------------------

class start:
  def __init__(self, option=1):
    self.option = option

  def main(self):
    n = 100
    list_all_type = ['constant', 'logarithmic', 'linear', 'quadratic', 'exponential', 'polynomial', 'factorial']
    if self.option == 1: # show all type in 1 plot
      list_o = []
      for i in list_all_type:
          o = big_oh(n)
          eval(f'o.{i}(n)')
          list_o.append(o)
      big_oh().plot_all(list_o)
    else: # show all type one by one
      for i in list_all_type:
        o = big_oh(n)
        eval(f'o.{i}(n)')
        o.plot()

if __name__ == '__main__':
  start().main()