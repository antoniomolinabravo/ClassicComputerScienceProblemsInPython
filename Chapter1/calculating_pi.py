# calculating_pi.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# calcula Pi en una secuencia con promedios en cascada
# reduce el numero de iteraciones y aumenta la precision rapidamente
# aporte realizado por Antonio Molina
def calculate_pi(n_iter: int, n_prom = 1) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    dato = []
    prom = []

    #calcula secuencia
    for i in range(n_iter):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
        #acumula ultimos N resultados para promediar
        if(i>=n_iter-n_prom): dato.append(pi)

    #calcula promedios en cascada
    while(len(dato) > 1):
      prom = []
      for i, num in enumerate(dato[0:-1]):
          prom.append( (num + dato[i+1]) /2 )
      dato = prom.copy()

    return dato[0]

if __name__ == "__main__":
    print(calculate_pi(n_iter=29, n_prom=18))

#bulk test
#Pi = 3.141592653589793
#for i in range(1, 30):
#  for N in range(1, i+1):
#    P = calculate_pi(i, N)
#    print(i, N, P, Pi-P)
#print("Pi  ", Pi)

#results
#iter, prom   error      result
#  9,   6   err:5e-5    3.14153820036173
# 11,   7   err:6e-6    3.1415986833943497
# 29,   18  err:9e-15   3.1415926535897833
