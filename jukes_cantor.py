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

import argparse

from fasta_processing import get_sequences
from jc_algorithm import ScoringMatrix
from jc_output import output_matrix

version = "v0.0.0"
desc = "jukes-cantor " + version
desc += "\nPerforms the Jukes-Cantor algorithm on provided FASTA sequences."
input_help = "input file path containing all aligned sequences in FASTA format"

#*****************************************************************************
# Main program
#*****************************************************************************

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("sequences-file", help=input_help, type=str)

labels, sequences = get_sequences(args.sequences_file)

# Perform Jukes-Cantor calculations on supplied sequences
jc_matrix = ScoringMatrix(sequences)

# Print results in a matrix format
output_matrix(labels, jc_matrix)

exit(0)
