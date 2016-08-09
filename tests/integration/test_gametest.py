# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import os
from tests import unittest

import mock

import kscore.session


class TestGameTestService(unittest.TestCase):
    def setUp(self):
        self.environ = os.environ.copy()
        self.patched = mock.patch('os.environ', self.environ)
        self.patched.start()
        self.environ.pop('AWS_DATA_PATH', None)

        self.session = kscore.session.get_session()
        self.client = self.session.create_client("gametest", "cn-beijing-6")

    def tearDown(self):
        self.patched.stop()

    def test_project_list(self):
        self.assertTrue(isinstance(self.client.get_project_list(), []))