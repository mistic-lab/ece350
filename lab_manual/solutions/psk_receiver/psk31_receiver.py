#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: PSK31 Receiver
# Author: ELEC350
# Generated: Fri Sep 13 16:48:22 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import digital;import cmath
from gnuradio import elec350
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class psk31_receiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="PSK31 Receiver")

        ##################################################
        # Variables
        ##################################################
        self.squelch = squelch = 0.07
        self.samp_rate = samp_rate = 48000
        self.freq = freq = 0
        self.decim = decim = 6
        self.bandwidth = bandwidth = 50
        self.attack = attack = 0.0001

        ##################################################
        # Message Queues
        ##################################################
        blocks_message_sink_0_msgq_out = varicode_decoder_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.psk_notebook = self.psk_notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.psk_notebook.AddPage(grc_wxgui.Panel(self.psk_notebook), "Decode")
        self.psk_notebook.AddPage(grc_wxgui.Panel(self.psk_notebook), "Tuning")
        self.psk_notebook.AddPage(grc_wxgui.Panel(self.psk_notebook), "Squelch")
        self.Add(self.psk_notebook)
        _squelch_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_text_box = forms.text_box(
        	parent=self.psk_notebook.GetPage(2).GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	label="Squelch",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_slider = forms.slider(
        	parent=self.psk_notebook.GetPage(2).GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.psk_notebook.GetPage(2).Add(_squelch_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label="Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=-samp_rate/12,
        	maximum=samp_rate/12,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        _bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bandwidth_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	label="Bandwidth",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bandwidth_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bandwidth_sizer,
        	value=self.bandwidth,
        	callback=self.set_bandwidth,
        	minimum=16,
        	maximum=100,
        	num_steps=100-16,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bandwidth_sizer)
        _attack_sizer = wx.BoxSizer(wx.VERTICAL)
        self._attack_text_box = forms.text_box(
        	parent=self.psk_notebook.GetPage(2).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	label="Attack",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._attack_slider = forms.slider(
        	parent=self.psk_notebook.GetPage(2).GetWin(),
        	sizer=_attack_sizer,
        	value=self.attack,
        	callback=self.set_attack,
        	minimum=0.0001,
        	maximum=0.001,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.psk_notebook.GetPage(2).Add(_attack_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.psk_notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/decim,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.psk_notebook.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.psk_notebook.GetPage(2).GetWin(),
        	unit="",
        	minval=0,
        	maxval=1,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate/decim,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="RMS",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.psk_notebook.GetPage(2).Add(self.wxgui_numbersink2_0.win)
        self.varicode_decoder_0 = elec350.varicode_decoder(
        	parent=self.psk_notebook.GetPage(0).GetWin(),
        	capfile="default_cap.txt",
        	msgq=varicode_decoder_0_msgq_in,
        )
        self.psk_notebook.GetPage(0).Add(self.varicode_decoder_0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=6,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, bandwidth, 100, firdes.WIN_HAMMING, 6.76))
        self.digital_mpsk_receiver_cc_0 = digital.mpsk_receiver_cc(2, 0, cmath.pi/100.0, -0.5, 0.5, 0.25, 0.01, 256, 0.001, 0.001)
        self.digital_diff_phasor_cc_0 = digital.diff_phasor_cc()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(squelch, squelch + .01, 0)
        self.blocks_rms_xx_0 = blocks.rms_cf(attack)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_sink_0 = blocks.message_sink(gr.sizeof_char*1, blocks_message_sink_0_msgq_out, True)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, 256)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_and_xx_0 = blocks.and_bb()
        self.audio_source_0 = audio.source(samp_rate, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/decim, analog.GR_COS_WAVE, -freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.digital_mpsk_receiver_cc_0, 0), (self.digital_diff_phasor_cc_0, 0))
        self.connect((self.digital_diff_phasor_cc_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_and_xx_0, 0), (self.blocks_message_sink_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_mpsk_receiver_cc_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_and_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_and_xx_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.audio_source_0, 1), (self.blocks_float_to_complex_0, 1))


# QT sink close method reimplementation

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self.blocks_threshold_ff_0.set_hi(self.squelch + .01)
        self.blocks_threshold_ff_0.set_lo(self.squelch)
        self._squelch_slider.set_value(self.squelch)
        self._squelch_text_box.set_value(self.squelch)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decim)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.bandwidth, 100, firdes.WIN_HAMMING, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.analog_sig_source_x_0.set_frequency(-self.freq)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decim)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.bandwidth, 100, firdes.WIN_HAMMING, 6.76))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self._bandwidth_slider.set_value(self.bandwidth)
        self._bandwidth_text_box.set_value(self.bandwidth)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.bandwidth, 100, firdes.WIN_HAMMING, 6.76))

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack
        self.blocks_rms_xx_0.set_alpha(self.attack)
        self._attack_slider.set_value(self.attack)
        self._attack_text_box.set_value(self.attack)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = psk31_receiver()
    tb.Start(True)
    tb.Wait()

