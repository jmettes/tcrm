#!/usr/bin/env python
"""
    Tropical Cyclone Risk Model (TCRM) - Version 1.0 (beta release)
    Copyright (C) 2011  Geoscience Australia

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Title: testWindProfile.py

Author: Nicholas Summons, nicholas.summons@ga.gov.au
CreationDate: 2011-06-10
Description: Unit test for the windProfile class

"""
import os, sys
import unittest
import cPickle
import NumpyTestCase
try:
    import pathLocate
except:
    from unittests import pathLocate

# Add parent folder to python path
unittest_dir = pathLocate.getUnitTestDirectory()
sys.path.append(pathLocate.getRootDirectory())
from WindfieldInterface import windProfile
from Utilities.files import flStartLog


class TestWindProfile(NumpyTestCase.NumpyTestCase):
    
    pkl_file = open(os.path.join(unittest_dir, 'test_data', 'windProfile_testdata.pck'), 'rb')
    R = cPickle.load(pkl_file)
    pEnv = cPickle.load(pkl_file)
    pCentre = cPickle.load(pkl_file)
    rMax = cPickle.load(pkl_file)
    cLat = cPickle.load(pkl_file)
    cLon = cPickle.load(pkl_file)
    beta = cPickle.load(pkl_file)
    rMax2 = cPickle.load(pkl_file)
    beta1 = cPickle.load(pkl_file)
    beta2 = cPickle.load(pkl_file)
    test_wP_rankine = cPickle.load(pkl_file)
    test_wP_jelesnianski = cPickle.load(pkl_file)
    test_wP_holland = cPickle.load(pkl_file)
    test_wP_willoughby = cPickle.load(pkl_file)
    test_wP_doubleHolland = cPickle.load(pkl_file)
    test_wP_powell = cPickle.load(pkl_file)    
    pkl_file.close()
    
    wP = windProfile.WindProfile(R, pEnv, pCentre, rMax, cLat, cLon, beta, rMax2, beta1, beta2)


    def test_rankine(self):
        """Testing rankine
        """
        wP_rankine = self.wP.rankine()
        self.numpyAssertAlmostEqual(wP_rankine, self.test_wP_rankine)

    def test_jelesnianski(self):
        """Testing jelesnianski
        """
        wP_jelesnianski = self.wP.jelesnianski()
        self.numpyAssertAlmostEqual(wP_jelesnianski, self.test_wP_jelesnianski)

    def test_holland(self):
        """Testing holland
        """
        wP_holland = self.wP.holland()
        self.numpyAssertAlmostEqual(wP_holland, self.test_wP_holland)

    def test_willoughby(self):
        """Testing willoughby
        """
        wP_willoughby = self.wP.willoughby()
        self.numpyAssertAlmostEqual(wP_willoughby, self.test_wP_willoughby)

    def test_doubleHolland(self):
        """Testing doubleHolland
        """
        wP_doubleHolland = self.wP.doubleHolland()
        self.numpyAssertAlmostEqual(wP_doubleHolland, self.test_wP_doubleHolland)

    def test_powell(self):
        """Testing powell
        """
        wP_powell = self.wP.powell()
        self.numpyAssertAlmostEqual(wP_powell, self.test_wP_powell)

if __name__ == "__main__":
    flStartLog('', 'CRITICAL', False)
    testSuite = unittest.makeSuite(TestWindProfile,'test')
    unittest.TextTestRunner(verbosity=2).run(testSuite)
