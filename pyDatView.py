#!/usr/bin/env python
import sys

#import click
#@click.option('-i','--inputfile', default='', help='Input file to read')
#@click.command()
#@click.argument('inputfile', default='')
def main(inputfiles=[]):
    import pydatview
    pydatview.show(filenames=inputfiles)

if __name__ == '__main__':
    main(sys.argv[1:])
