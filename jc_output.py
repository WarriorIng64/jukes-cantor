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

import sys

FIELD_WIDTH = 9

def formatted_jc_string(jukes_cantor_score):
    '''Return a formatted Jukes-Cantor score string with required precision.'''
    format_string = "{:0." + str(FIELD_WIDTH - 2) + "f}"
    return format_string.format(jukes_cantor_score + 0) # Last part fixes -0.0

def output_matrix(labels, jc_matrix, outfile=""):
    '''Given sequence labels and a pre-computed Jukes-Cantor scoring matrix,
    print all the scores in the terminal.'''
    sys.stdout = sys.__stdout__
    if outfile != "" and outfile != None:
        try:
            sys.stdout = open(outfile, 'w')
        except Exception as e:
            print "Failed to redirect output to", outfile
            exit(1)
    print " " * (FIELD_WIDTH),
    for label in labels:
        print label[0:FIELD_WIDTH],
    print
    for i in range(jc_matrix.get_size()):
        print (labels[i])[0:FIELD_WIDTH],
        for j in range(jc_matrix.get_size()):
            print formatted_jc_string(jc_matrix.get_score(i, j)),
        print
    sys.stdout = sys.__stdout__
