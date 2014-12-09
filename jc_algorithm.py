# This file is part of jukes-cantor.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# jukes-cantor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# jukes-cantor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with jukes-cantor. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 12/9/2014

def calculate_jukes_cantor(sequence1, sequence2):
    '''Calculate the Jukes-Cantor distance between the two provided aligned
    sequences.
    
    Based on pseudocode provided on page 116 of the textbook.'''
    
    # Initialization
    difference_counter = 0
    length_counter = 0
    
    # Step 1: Count differences between sequences, ignoring gaps
    for i in range(min(len(sequence1), len(sequence2))):
        if sequence1[i] != '-' and sequence2[i] != '-':
            length_counter += 1
            if sequence1[i] != sequence2[i]:
                difference_counter += 1
    
    # Step 2: Calculate and return results
    substitutions_fraction = float(difference_counter) / float(length_counter)
    jukes = -3.0/4.0 * math.log(1 - (4.0/3.0 * substitutions_fraction))
    return jukes
