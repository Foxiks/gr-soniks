# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Stratosat X-Band Scrambler
# GNU Radio version: 3.10.7.0

from gnuradio import gr
import pmt
    
class stratosat_xband_scrambler(gr.sync_block):
    """
    Stratosat X-Band Scrambler
    """
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='Stratosat X-Band Scrambler',
            in_sig=[],
            out_sig=[])

        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.message_port_register_out(pmt.intern('out'))
        self.mask=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0xF7, 0x0B, 0x36, 0xF4, 0x39, 0x84, 0x8A, 
                   0xEB, 0xC9, 0x73, 0x81, 0xDD, 0x3D, 0x4A, 0x05, 0x57, 0xD6, 0x83, 0x76, 0xD6, 0x0B, 0xBE, 0x3C, 
                   0xD3, 0x5C, 0x68, 0xBF, 0xA5, 0x8A, 0x63, 0x01, 0x99, 0x59, 0x3F, 0x69, 0x26, 0xFC, 0xB5, 0x0A, 
                   0x27, 0x65, 0xEC, 0x35, 0x4E, 0x43, 0x10, 0x80, 0x44, 0x64, 0x75, 0x6C, 0x71, 0x2A, 0x36, 0x7C, 
                   0xF1, 0x6E, 0x52, 0x09, 0x9D, 0x1F, 0x78, 0x3F, 0xE1, 0xEE, 0x16, 0x6D, 0xE8, 0x73, 0x09, 0x15, 
                   0xD7, 0x92, 0xE7, 0x03, 0xBA, 0x7A, 0x94, 0x0A, 0xAF, 0xAD, 0x06, 0xED, 0xAC, 0x17, 0x7C, 0x79, 
                   0xA6, 0xB8, 0xD1, 0x7F, 0x4B, 0x14, 0xC6, 0x03, 0x32, 0xB2, 0x7E, 0xD2, 0x4D, 0xF9, 0x6A, 0x14, 
                   0x4E, 0xCB, 0xD8, 0x6A, 0x9C, 0x86, 0x21, 0x00, 0x88, 0xC8, 0xEA, 0xD8, 0xE2, 0x54, 0x6C, 0xF9, 
                   0xE2, 0xDC]

    def handle_msg(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print('[ERROR] Received invalid message type. Expected u8vector')
            return
        arr=[]
        msg = pmt.u8vector_elements(msg)
        for i in range(len(msg)):
            try:
                arr.append(msg[i]^self.mask[i])
            except IndexError:
                arr.append(msg[i])
        msg_out = arr
        msg_out = pmt.init_u8vector(len(msg_out), msg_out)
        msg_out = pmt.cons(pmt.car(msg_pmt), msg_out)
        self.message_port_pub(pmt.intern('out'), msg_out)