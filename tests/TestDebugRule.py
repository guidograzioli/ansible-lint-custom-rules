# Copyright (C) 2020, 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods,missing-class-docstring
# pylint: disable=missing-function-docstring
"""Test cases for the rule, DebugRule.
"""
import os
import unittest.mock

import pytest

from rules import DebugRule as TT
from tests import common


@pytest.mark.parametrize(
    ('env', 'exp'),
    (({}, False),
     ({TT.E_ENABLED_VAR: ''}, False),
     ({TT.E_ENABLED_VAR: '1'}, True),
     )
)
def test_is_enabled(env, exp):
    with unittest.mock.patch.dict(os.environ, env, clear=True):
        assert TT.is_enabled() == exp


class Base(common.Base):
    this_mod: common.MaybeModT = TT
    default_skip_list = ['no_unspecified_argument']


class RuleTestCase(common.RuleTestCase):
    base_cls = Base

    def test_base_get_filename(self):
        self.assertEqual(self.base.get_filename(), 'TestDebugRule.py')

    def test_base_get_rule_name(self):
        self.assertEqual(self.base.get_rule_name(), 'DebugRule')

    def test_base_get_rule_class_by_name(self):
        rule_class = self.base.get_rule_class_by_name(self.base.name)
        self.assertTrue(bool(rule_class))
        self.assertTrue(isinstance(rule_class(), type(self.base.rule)))

    def test_base_is_runnable(self):
        self.assertTrue(self.base.is_runnable())

    def test_list_test_data_dirs(self):
        self.assertTrue(self.list_test_data_dirs(True))
        self.assertTrue(self.list_test_data_dirs(False))

    def test_clear_fns(self):
        fns = self.base.clear_fns
        self.assertTrue(fns)
        self.assertTrue(len(fns) > 1)


class CliTestCase(common.CliTestCase):
    base_cls = Base
