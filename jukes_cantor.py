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

version = "v0.0.0"
desc = "jukes-cantor " + version
desc += "\nPerforms the Jukes-Cantor algorithm on provided FASTA sequences."
input_help = "input file path containing all sequences in FASTA format"

#*****************************************************************************
# Main program
#*****************************************************************************

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("sequences-file", help=input_help, type=str)

if os.path.exists(args.sequences_file):
    try:
        with open(args.sequences_file, 'r') as infile:
            # TODO: Read sequences and store them
    except IOError:
        print "Error: could not open supplied file: " + args.sequence_file
        exit(1)
else:
    print "Error: supplied input file path does not exist: " + args.sequence_file
    exit(1)

# Perform Jukes-Cantor calculations on supplied sequences
# TODO

# Print results in a matrix format
# TODO

exit(0)
