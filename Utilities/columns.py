"""
:mod:`columns` -- load delimited data files
===========================================

.. module:: columns
    :synopsis: Load csv formatted data into a numpy array

.. moduleauthor:: Craig Arthur <craig.arthur@ga.gov.au>

"""

import numpy as np
from Utilities.config import ConfigParser

def colReadCSV(configFile, dataFile, source):
    """
    Loads a csv file containing 'column' data into a record (numpy)
    array with columns labelled by 'fields'. There must be a section in
    the ``configFile`` named ``source`` that sets out the format of the
    data file.

    :param str configFile: Path to a configuration file that holds details
                           of the input data.
    :param str dataFile: Path to the input file to load.
    :param str source: Name of the source format. There must be a
                       corresponding section in the ``configFile``.

    :returns: A :class:`numpy.ndarray` that contains the input data.
    
    """
    config = ConfigParser()
    config.read(configFile)
    delimiter = config.get(source, 'FieldDelimiter')
    numHeadingLines = config.getint(source, 'NumberOfHeadingLines')
    cols = config.get(source, 'Columns').split(delimiter)

    usecols = [i for i,c in enumerate(cols) if c != 'skip']

    data = np.genfromtxt(dataFile, dtype=None, delimiter=delimiter,
            usecols=usecols, comments=None, skip_header=numHeadingLines, 
            autostrip=True)

    data.dtype.names = [c for c in cols if c != 'skip']

    return data
