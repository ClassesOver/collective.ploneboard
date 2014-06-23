# -*- coding: utf-8 -*-
"""Functional Doctests for plone.app.discussion.

   These test are only triggered when Plone 4 (and plone.testing) is installed.
"""
import doctest

import unittest2 as unittest
import pprint

from plone.testing import layered

from collective.ploneboard.testing import (
    COLLECTIVE_PLONEBOARD_INTEGRATION_TESTING
)

optionflags = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_ONLY_FIRST_FAILURE
)
testfiles = [
    '../../../../README.rst',
    'functional_test_messageboard_workflow.txt',
    'functional_test_try_conv_no_review_w.txt',
    'functional_test_try_conv_w.txt',
]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(
            test,
            optionflags=optionflags,
            globs={'pprint': pprint.pprint, }
        ), layer=COLLECTIVE_PLONEBOARD_INTEGRATION_TESTING)
        for test in testfiles
    ])
    return suite
