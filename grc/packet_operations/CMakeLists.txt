# Copyright 2011 Free Software Foundation, Inc.
#
# This file was generated by gr_modtool, a tool from the GNU Radio framework
# This file is a part of gr-soniks
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

install(FILES
    soniks_messages_mixer_pdu.block.yml
    soniks_fengyun2_bytes_inverter.block.yml
    soniks_fengyun2_data_saver.block.yml
    soniks_messages_skip_head.block.yml
    soniks_message_chunks_strip.block.yml
    soniks_fengyun2_frames_collector.block.yml
    soniks_fengyun2_decoder.block.yml
    soniks_pdu_hash_analyzer.block.yml
    soniks_messages_skip_last.block.yml
    soniks_fengyun2_relevance_check.block.yml
    DESTINATION share/gnuradio/grc/blocks
)
