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

from Products.RhaptosTest import base


base.PRODUCTS_TO_LOAD_ZCML = [('configure.zcml', Products.RhaptosModuleStorage),]
base.PRODUCTS_TO_INSTALL = ['RhaptosModuleStorage',]


# TODO:  I need to set up a Z Psycoppg database connection here.


class TestRhaptosModuleStorage(base.RhaptosTestCase):

    def test_pass(self):
        assert 1 == 1


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRhaptosModuleStorage))
    return suite
