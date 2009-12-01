#  Copyright 2008 Nokia Siemens Networks Oyj
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest 

from robotide.action.shortcut import Shortcut
# wx needs to imported last so that robotide can select correct wx version.
import wx


class TestShortcutParsing(unittest.TestCase):

    def test_single_character(self):
        self._test([('A', (wx.ACCEL_NORMAL, 65)),
                    ('a', (wx.ACCEL_NORMAL, 65)),
                    ('R', (wx.ACCEL_NORMAL, 82))])

    def test_single_key(self):
        self._test([('Insert', (wx.ACCEL_NORMAL, wx.WXK_INSERT)),
                    ('DEL', (wx.ACCEL_NORMAL, wx.WXK_DELETE)),
                    ('DeLeTE', (wx.ACCEL_NORMAL, wx.WXK_DELETE))])

    def test_control_key(self):
        self._test([('Ctrl-A', (wx.ACCEL_CTRL, 65)),
                    ('Shift-DEL', (wx.ACCEL_SHIFT, wx.WXK_DELETE)),
                    ('Alt-DELETE', (wx.ACCEL_ALT, wx.WXK_DELETE))])

    def test_two_control_keys(self):
        self._test([('Ctrl-Alt-A', (wx.ACCEL_CTRL+wx.ACCEL_ALT, 65)),
                    ('Shift-Ctrl-DEL', (wx.ACCEL_SHIFT+wx.ACCEL_CTRL, wx.WXK_DELETE)),
                    ('Alt-Cmd-DELETE', (wx.ACCEL_ALT+wx.ACCEL_CMD, wx.WXK_DELETE))])

    def test_invalid_shortcut(self):
        self.assertRaises(ValueError, Shortcut('InvaLid').parse)

    def _test(self, data):
        for shortcut, expected in data:
            self.assertEquals(Shortcut(shortcut).parse(), expected)


if __name__ == '__main__':
    unittest.main()
