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

import os

def get_sequences(input_path):
    '''Given an input file path, return the individual sequences in a list.'''
    if os.path.exists(input_path):
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
                # TODO: Read sequences and store them
        except IOError:
            print "Error: could not open supplied file: " + input_path
            exit(1)
    else:
        print "Error: supplied input file path does not exist: " + input_path
        exit(1)
