# Copyright (C) 2020,2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods,missing-class-docstring
# pylint: disable=missing-function-docstring
"""Test cases for the rule, BlockedModules.
"""
from rules import BlockedModules as TT
from tests import common


class Base(common.Base):
    this_mod: common.MaybeModT = TT
    default_skip_list = ['no_unspecified_argument']

class RuleTestCase(common.RuleTestCase):
    base_cls = Base


class CliTestCase(common.CliTestCase):
    base_cls = Base
