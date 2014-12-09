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

class ScoringMatrixCell:
    '''A class implementing individual cells within the scoring matrix.'''
    def __init__(self, score=0.0):
        '''Initializes this ScoringMatrixCell instance.
        If the arguments are omitted, a cell with a score of 0 will be created
        by default.'''
        self.score = score
    
    def get_score(self):
        '''Returns this cell's current score.'''
        return self.score
    
    def set_score(self, score):
        '''Updates this cell's score to the new one supplied.'''
        self.score = score

class ScoringMatrix:
    '''A class implementing a scoring matrix.'''
    def __init__(self, sequences):
        '''Initializes a new scoring matrix with the supplied sequences.
        sequences isthe list of sequences to compute score for.'''
        self.matrix_size = len(sequences)
        if self.matrix_size < 1:
            self.matrix = []
        elif self.matrix_size < 2:
            self.matrix = [ScoringMatrixCell(0.0)]
        else:
            self.matrix = [[ScoringMatrixCell() for x in range(self.matrix_size)]
                           for x in range(self.matrix_size)]
    
    def get_size(self)
        '''Returns the number of sequences used to generate this matrix.'''
        return self.matrix_size
    
    def get_score(self, row, column):
        '''Gets the current score at the specified row and column.'''
        try:
            return self.matrix[row][column].get_score()
        except IndexError:
            print "IndexError in get_score({0!s}, {1!s})".format(row, column)
            exit(1)
    
    def set_score(self, row, column, score):
        '''Sets the score at the specified row and column.'''
        try:
            self.matrix[row][column].set_score(score)
        except IndexError:
            print "IndexError in set_score({0!s}, {1!s})".format(row, column)
            exit(1)
    
    def calculate_scores(self, sequences):
        '''Calculates the scores for all cells given the sequences.'''
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                set_score(i, j,
                          calculate_jukes_cantor(sequences[i], sequences[j]))

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

def calculate_matrix(sequences):
    '''Given a list list of sequences, construct a matrix of the Jukes-Cantor
    scores between all sequences. The matrix itself is a list of lists.'''
    if len(sequences) < 1:
        return []
    elif len(sequences) < 2:
        return [0.0]
    else:
        # Non-trivial case
