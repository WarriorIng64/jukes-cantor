jukes-cantor
============

An implementation of the Jukes-Cantor algorithm for Homework Assignment 5 in MCS 5603.

## Usage ##

    python jukes_cantor.py input_file.fasta

To redirect output to a text file, instead type:

    python jukes_cantor.py input_file.fasta -o output_file.txt

In either case, `input_file.fasta` must contain pre-aligned FASTA sequences for analogous genes from different species.

The output will be in the form of a matrix of Jukes-Cantor scores.

To see all available options, use the `-h` option.

## License ##

GNU GPLv3
