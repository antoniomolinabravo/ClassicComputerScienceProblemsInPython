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

# solucion con menos iteraciones
# tengo otra version mas simplificada pero la estoy probando, que calcula a la iteracion 30 y otra a la 10

def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    pi_ant1: float = 4  # mem_pi_prev
    pi_ant2: float = 0  # men_pi_prev_prev
    pi_prom1: float = 0 # pi_mean_1
    pi_prom2: float = 0 # pi_mean_2

    for _ in range(n_terms):
        pi_ant2 = pi_ant1       # backup1
        pi_ant1 = pi            # backup2
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    pi_prom1 = (pi + pi_ant1) /2    # pi_mean_1
    pi_prom2 = (pi_ant1 + pi_ant2) /2   # pi_mean_2
    pi = (pi_prom1 + pi_prom2) /2   # pi_mean(pi_means)

    return pi

if __name__ == "__main__":
    #print(calculate_pi(350)) # PAR:POR ABAJO  IMPAR:POR ARIBA
    pi1 = calculate_pi(99)  # impar
    pi2 = calculate_pi(100) # par
    print(pi1)
    print(pi2)
    print( (pi1 + pi2) /2 ) # pi_mean(means)
