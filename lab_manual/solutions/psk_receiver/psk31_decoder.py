#
# Copyright 2009 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gru
from datetime import datetime
import wx
import struct
import re

DEFAULT_WIN_SIZE = (600, 300)
APPEND_EVENT = wx.NewEventType()
EVT_APPEND_EVENT = wx.PyEventBinder(APPEND_EVENT, 0)

class AppendEvent(wx.PyEvent):
    def __init__(self, text):
        wx.PyEvent.__init__(self)
        self.SetEventType(APPEND_EVENT)
        self.text = text

    def Clone(self):
        self.__class__(self.GetId())

class psk31_decoder(wx.Panel):
	def __init__(self,
		     parent,
		     msgq,
                     capfile,
		     size=DEFAULT_WIN_SIZE,
		     ):

		wx.Panel.__init__(self,
				  parent,
				  size=size,
				  style=wx.SIMPLE_BORDER,
				  )

		self.text_ctrl = wx.TextCtrl(self,
					     wx.ID_ANY,
					     value="",
					     size=size,
					     style=wx.TE_MULTILINE|wx.TE_READONLY,
					     )

                self.capture_file = open(capfile, 'a')
                datestr = datetime.now().strftime("%d %B %Y, %H:%M:%S")
                self.capture_file.write(datestr + "\n")
                self.capture_file.write("=" * len(datestr) + "\n")

		main_sizer = wx.BoxSizer(wx.VERTICAL)
		main_sizer.Add(self.text_ctrl, 1, wx.EXPAND)
		self.SetSizerAndFit(main_sizer)

                EVT_APPEND_EVENT(self, self.evt_append)
		self.runner = gru.msgq_runner(msgq, self.handle_msg)

                self.partial = ''
                self.psk31_dict = {    
                    '1010101011' : '\x00',    '1011011011' : '\x01',
                    '1011101101' : '\x02',    '1101110111' : '\x03',
                    '1011101011' : '\x04',    '1101011111' : '\x05',
                    '1011101111' : '\x06',    '1011111101' : '\x07',
                    '1011111111' : '\x08',    '11101111'   : '\x09',
                    '11101'      : '\x0A',    '1101101111' : '\x0B',
                    '1011011101' : '\x0C',    '11111'      : '\x0D',
                    '1101110101' : '\x0E',    '1110101011' : '\x0F',
                    '1011110111' : '\x10',    '1011110101' : '\x11',
                    '1110101101' : '\x12',    '1110101111' : '\x13',
                    '1101011011' : '\x14',    '1101101011' : '\x15',
                    '1101101101' : '\x16',    '1101010111' : '\x17',
                    '1101111011' : '\x18',    '1101111101' : '\x19',
                    '1110110111' : '\x1A',    '1101010101' : '\x1B',
                    '1101011101' : '\x1C',    '1110111011' : '\x1D',
                    '1011111011' : '\x1E',    '1101111111' : '\x1F',
                    '1'          : ' ',       '111111111'  : '!',
                    '101011111'  : '"',       '111110101'  : '#',
                    '111011011'  : '$',       '1011010101' : '%',
                    '1010111011' : '&',       '101111111'  : '\'',
                    '11111011'   : '(',       '11110111'   : ')',
                    '101101111'  : '*',       '111011111'  : '+',
                    '1110101'    : ',',       '110101'     : '-',
                    '1010111'    : '.',       '110101111'  : '/',
                    '10110111'   : '0',       '10111101'   : '1',
                    '11101101'   : '2',       '11111111'   : '3',
                    '101110111'  : '4',       '101011011'  : '5',
                    '101101011'  : '6',       '110101101'  : '7',
                    '110101011'  : '8',       '110110111'  : '9',
                    '11110101'   : ':',       '110111101'  : ';',
                    '111101101'  : '<',       '1010101'    : '=',
                    '111010111'  : '>',       '1010101111' : '?',
                    '1010111101' : '@',       '1111101'    : 'A',
                    '11101011'   : 'B',       '10101101'   : 'C',
                    '10110101'   : 'D',       '1110111'    : 'E',
                    '11011011'   : 'F',       '11111101'   : 'G',
                    '101010101'  : 'H',       '1111111'    : 'I',
                    '111111101'  : 'J',       '101111101'  : 'K',
                    '11010111'   : 'L',       '10111011'   : 'M',
                    '11011101'   : 'N',       '10101011'   : 'O',
                    '11010101'   : 'P',       '111011101'  : 'Q',
                    '10101111'   : 'R',       '1101111'    : 'S',
                    '1101101'    : 'T',       '101010111'  : 'U',
                    '110110101'  : 'V',       '101011101'  : 'W',
                    '101110101'  : 'X',       '101111011'  : 'Y',
                    '1010101101' : 'Z',       '111110111'  : '[',
                    '111101111'  : '\\',      '111111011'  : ']',
                    '1010111111' : '^',       '101101101'  : '_',
                    '1011011111' : '`',       '1011'       : 'a',
                    '1011111'    : 'b',       '101111'     : 'c',
                    '101101'     : 'd',       '11'         : 'e',
                    '111101'     : 'f',       '1011011'    : 'g',
                    '101011'     : 'h',       '1101'       : 'i',
                    '111101011'  : 'j',       '10111111'   : 'k',
                    '11011'      : 'l',       '111011'     : 'm',
                    '1111'       : 'n',       '111'        : 'o',
                    '111111'     : 'p',       '110111111'  : 'q',
                    '10101'      : 'r',       '10111'      : 's',
                    '101'        : 't',       '110111'     : 'u',
                    '1111011'    : 'v',       '1101011'    : 'w',
                    '11011111'   : 'x',       '1011101'    : 'y',
                    '111010101'  : 'z',       '1010110111' : '{',
                    '110111011'  : '|',       '1010110101' : '}',
                    '1011010111' : '~',       '1110110101' : '\x7F' }

        def __del__(self):

            self.capture_file.write("\n")
            self.capture_file.close()

	def handle_msg(self, msg):

                ################################################################
                # PSK31 Decoder:

                # Unpack the bytes from the DBPSK demod
                bitstream = msg.to_string()
                for bit in struct.unpack('B'*len(bitstream), bitstream):
                    self.partial += str(bit)

                # Split it out into characters we can look up in the dictionary.
                # In PSK31, two or more zeros represents a space between chars.
                char_list = re.split('00+', self.partial)
                self.partial = char_list[-1]

                # Create a text string from the looked up chars
                text = ""
                if len(char_list) > 1:
                    for char in char_list[0:-1]:
                        if char in self.psk31_dict:
                            text += self.psk31_dict[char]
                        elif char != '':
                            text += "?"

                ################################################################
                
		# Create a wxPython event and post it to the event queue
		evt = AppendEvent(text)
		wx.PostEvent(self, evt)
		del evt

        def evt_append(self, evt):
		# This gets called by the wxPython event queue runner
		self.text_ctrl.AppendText(evt.text)
                self.capture_file.write(evt.text)
