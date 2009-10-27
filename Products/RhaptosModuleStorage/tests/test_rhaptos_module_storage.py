#------------------------------------------------------------------------------#
#   test_rhaptos_module_storage.py                                             #
#                                                                              #
#       Authors:                                                               #
#       Rajiv Bakulesh Shah <raj@enfoldsystems.com>                            #
#                                                                              #
#           Copyright (c) 2009, Enfold Systems, Inc.                           #
#           All rights reserved.                                               #
#                                                                              #
#               This software is licensed under the Terms and Conditions       #
#               contained within the "LICENSE.txt" file that accompanied       #
#               this software.  Any inquiries concerning the scope or          #
#               enforceability of the license should be addressed to:          #
#                                                                              #
#                   Enfold Systems, Inc.                                       #
#                   4617 Montrose Blvd., Suite C215                            #
#                   Houston, Texas 77006 USA                                   #
#                   p. +1 713.942.2377 | f. +1 832.201.8856                    #
#                   www.enfoldsystems.com                                      #
#                   info@enfoldsystems.com                                     #
#------------------------------------------------------------------------------#
"""Unit tests.
$Id: $
"""


import Products.RhaptosModuleStorage

from Products.RhaptosTest.base import RhaptosTestCase


class TestRhaptosModuleStorage(RhaptosTestCase):

    products_to_load_zcml = [('configure.zcml', Products.RhaptosModuleStorage),]

    def setUp(self):
        RhaptosTestCase.setUp(self)

    def test_module_version_storage(self):
        self.assertEqual(1, 1)

    def test_module_view(self):
        self.assertEqual(1, 1)

    def test_module_file(self):
        self.assertEqual(1, 1)

    def test_rhaptosdb_iterator(self):
        self.assertEqual(1, 1)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRhaptosModuleStorage))
    return suite