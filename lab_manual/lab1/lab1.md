Lab 1 - GNU Radio Tutorials
==========================

The following tutorials were adapted from [Dr. Sharlene Katz\' SDR
Project](http://www.csun.edu/~skatz/katzpage/sdr_project/sdrproject.html)
website and updated for GNU Radio 3.7. They are designed to get you
familiar with various aspects of the GNU Radio Companion. You will also
learn some basic tuning and demodulation techniques.

In addition to providing you with a great introduction to GNU Radio
Companion, this material can also be used as a reference for future labs

As you work through the material, try to keep these following questions
in mind:

-   What do the different colors of input and output terminals
    represent?

-   How is the computer\'s audio input/output hardware represented in
    GRC?

-   What is the Throttle block for? When should it be used?

-   How are block parameters linked to GUI controls?

-   How is an AM signal demodulated into an audio signal?

-   How is an SSB signal demodulated into an audio signal?

-   What methods are used to tune to a desired signal?

To understand how these demodulation techniques work, please review the
theory of [AM and SSB signals](./data/Theory_AM_SSB.pdf).

Other tutorials are also available, see for example

-   [Video
    tutorials](http://www.ettus.com/kb/detail/software-defined-radio-usrp-and-gnu-radio-tutorial-set)

-   [Python and 5 GRC labs](http://files.ettus.com/tutorials/)

-   [gnuradio.org
    tutorials](http://gnuradio.org/redmine/projects/gnuradio/wiki/Tutorials)

-   [Gnuradio and RTL-SDR USB
    stick](http://www.rtl-sdr.com/tutorial-creating-fm-receiver-gnuradio-rtl-sdr/?PageSpeed=noscript)

Deliverables
------------

-   GRC file of AM transmitter and receiver as described in Tutorial 3A.

-   GRC file of AM receiver with AGC as described in Tutorial 3B.

-   block diagram of AM receiver showing mathematical representation of
    signals at all points

-   GRC file of SSB receiver using Weaver\'s method as described in
    Tutorial 4.

-   block diagram of SSB receiver showing mathematical representation of
    signals at all points

-   There are a number of questions included within the text. Written
    answers to these questions are not required, but an effort should be
    made to think about and answer these questions as they are
    encountered.

Tutorial 1: Using GNU Radio Companion
-------------------------------------

### Objectives

GNU Radio Companion (GRC) is a graphical user interface that allows you
to build GNU Radio flowgraphs. It is an excellent way to learn the
basics of GNU Radio. This is the first in a series of tutorials that
will introduce you to the use of GRC. In this tutorial you will learn
how to:

-   launch the GNU Radio Companion (GRC) software.

-   create and execute a GRC flowgraph.

-   use basic blocks such as signal sources and graphical sinks.

-   use the computer\'s audio hardware with GRC.

### Launching GNU Radio Companion

Launch GNU Radio companion by selecting Applications-\>Programming-\>GRC
as shown in [figure\_title](#GRC_Location).

An untitled GRC window similar to [figure\_title](#blank_flowgraph)
should open.

### Configuring the Flowgraph

The *Options* block sets some general parameters for the flow graph.
Double-click on the *Options* block. You should now see a properties
dialog similar to [figure\_title](#options_properties).

-   Leave the ID as \"top\_block\".

-   Enter \"Tutorial 1\" as the title.

-   Enter your name as the Author.

-   Set Generate Options to WX GUI.

    Note: This setting controls the way that GUIs are generated for flow
    graph output. Many of the output plots used in these labs will not
    be available if this option is set to the default QT GUI

-   Set Run to Autostart, and Realtime Scheduling to Off.

-   Click OK to close the properties dialog.

-   The other block in the flowgraph is a
    [variable](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s04s01.html)
    block that sets the sample rate. Click on this block to see the
    variable name and value. The variable block will be discussed later
    in the tutorial.

### Adding Blocks to the Flowgraph

On the right side of the window is a list of the blocks that are
available. By expanding any of the categories (click on triangle to the
left) you can see the blocks available. Explore each of the categories
so that you have an idea of what blocks are available.

You can also click on the magnifying glass in the upper right side of
the window and simply type a search term (e.g. *receiver*) to search all
categories. A small text window will appear above the list of blocks in
which your search term will be entered. This will filter the list
leaving only blocks with *receiver* in their name. Try a few searches
such as *filter* and *source* to see what comes up.

-   Open the *Waveform Generators* category and double-click on the
    [Signal
    Source](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s02s01.html).
    Note that a *Signal Source* block will now appear in the main
    window.

-   Double-click on the *Signal Source* block and the properties dialog
    will open. Adjust the settings to match those as shown in
    [figure\_title](#signal_source_properties) and close the dialog.

    This *Signal Source* is now set to output a real-valued 1 kHz
    sinusoid with a peak amplitude of 0.5.

-   In the flowgraph, the *Signal Source* block will have an orange
    output tab, representing a float (real) data type. If the block
    settings is chosen as complex instead of float, then the output tab
    will be blue. In order to view this wave we need one of the
    graphical sinks. Expand the *Instrumentation* category and then the
    *WX* subcategory.

-   Double-click on the *WX GUI Scope Sink*. It should appear in the
    main window. Double-click on the block and change the *Type* to
    *Float*. Leave the other Parameters at their default values as shown
    in [figure\_title](#scope_sink_properties). Click *OK* to close the
    properties dialog.

-   In order to connect these two blocks, click once on the *out* port
    of the *Signal Source*, and then once on the *in* port of the *Scope
    Sink*. The flow graph in
    [figure\_title](#signal_source_scope_sink_only) should be displayed.

-   The problem with this flowgraph is that although the sample rate is
    set to 32000, there is no block which enforces this sample rate.
    Therefore, the flowgraph will consume as much of the computer\'s
    resources as it possibly can which can cause the GRC software to
    lock up. To fix this problem, disconnect the *Signal Source* from
    the *WX GUI Scope Sink* by clicking on the arrow and pressing the
    Delete key. Expand the *Misc* category and double-click on the
    [Throttle](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s03s07.html).
    Connect this block between the *Signal Source* and the *WX GUI Scope
    Sink* as shown in [figure\_title](#scope_source_scope_sink) (click
    once on the out port of one block and the in port of the next
    block).

-   Note that the input and output arrowheads will change to red. This
    indicates a problem with the flowgraph, in this case, the data types
    do not match. To fix the problem, double-click the *Throttle* and
    change the *Type* to *Float*.

### Executing the Flowgraph

In order to observe the operation of this simple system we must generate
the flowgraph and then execute it.

-   Click first on the ![](images/generate.png) icon (or press F5) to
    generate the flowgraph.

-   If the flowgraph has not yet been saved, a file dialog will appear
    when you click this button. Name this file *tutorial1.grc* and save
    it to a folder on your home drive. The generation stage converts
    your flowgraph into executable Python code.

-   Click the ![](images/execute.png) icon (or press F6) to execute the
    flowgraph. The execution stage runs the Python code that was
    generated in the previous step. A scope plot should open displaying
    several cycles of the sinusoid. Confirm that the frequency and
    amplitude match the value that you expect. What is the period of one
    cycle of the sine wave, and thus what is the frequency? Experiment
    with the controls on the scope plot.

### Working with the Scope Sink

-   Change the *Channel Options / Marker* setting to *Dot Large*. As
    shown in [figure\_title](#scope_sink_dot_large), you can now see the
    actual sample values. Recall that the *Variable* block set the
    sampling rate to 32000 samples/second or 32 samples/ms. Note that
    there are in fact 32 samples within one cycle of the wave.

-   Close the scope and reduce the sample rate to 10000 by
    double-clicking on the *Variable* block and entering 10e3 in the
    *Value* box. Note that you can use this exponential notation
    anywhere that GNURadio requires a number.

-   Re-generate and execute the flow graph. Note that there are now
    fewer points per cycle. How low can you drop the sample rate? Recall
    that the Nyquist sampling theorem requires that we sample at more
    than two times the highest frequency. Experiment with this and see
    how the output changes as you drop below the Nyquist rate.

### Working with the FFT Sink

-   The FFT Sink acts as a Spectrum Analyzer by doing a short time
    discrete Fourier transform (STFT). Review the [theory of the
    Spectrum Analyzer](data/Theory_Spectrum_Analyzer.pdf)

-   Close the scope and change the sample rate back to 32000. Add a *WX
    GUI FFT Sink* (under *Instrumentation-\>WX*) to your window. Change
    the Type to Float and leave the remaining parameters at their
    default values.

-   Connect this to the output of the *Signal Source* by clicking on the
    *out* port of the *Throttle* and then the *in* port of the *WX GUI
    FFT Sink*. Generate and execute the flow graph. You should observe
    the scope as before along with an FFT plot correctly showing the
    frequency of the input at 1KHz. Close the output windows.

-   Explore other graphical sinks (*WX GUI Number Sink*, *WX GUI
    Waterfall Sink*, and *WX GUI Histo Sink*) to see how they display
    the *Signal Source*

    -   The number sink is typically used to monitor slowly-changing
        signals such as the RMS input level. In this example, the sine
        wave changes too fast for the numbers to keep up.

    -   The waterfall sink is used to display amplitude vs. frequency
        vs. time with amplitude represented as a variation in color. The
        waterfall is a time frequency diagram with time on the vertical
        axis. Note that for a single 1 Khz sine wave input, the
        frequency does not change with time, thus a vertical line is
        displayed at 1 Khz.

    -   The histo sink displays a histogram of the input values, which
        can be used to monitor the symbol distribution in a digital
        signal or the distribution of a noise source.

### Working with Audio I/O

-   Create the flow graph shown in
    [figure\_title](#signal_source_fft_sink_audio_sink).

-   The *Audio Sink* is found in the *Audio* category. The [Audio
    Sink](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s05s03.html) block
    directs the signal to the audio card of your computer. Note that the
    sample rate is set to 48000, a sample rate that is usually, but not
    always supported by computer audio hardware. 44100 is supported by
    every sound card. Other commonly-supported rates are 8000, 11025
    and 22050. Some audio hardware may support higher rates such as
    88200 and 96000. Also note that there is no *Throttle* block. This
    is because the audio hardware enforces the desired sample rate by
    only accepting samples at this rate.

    -   It is worth noting that sample rates, especially related to
        audio output are a common source of frustration in these labs so
        it is worth spending some time to ensure the concepts are
        understood here. More information about how GNU Radio
        communicates with the computer\'s audio hardware can be found
        [here](http://gnuradio.org/redmine/projects/gnuradio/wiki/ALSAPulseAudio#Solution)

-   Generate and execute this flow graph. The graphical display of the
    scope and FFT should open as before. However, now you should also
    hear the 1 kHz tone. If you do not hear the tone, ensure that the
    output from the computer is connected to the speakers and that the
    volume is turned up. Experiment with changing both the overall
    sample rate in the flow graph as well as the sample rate in the
    audio sink to see how the tone is affected.

### Math Operations

-   Construct the flow graph in [figure\_title](#add_sinusoids). Set the
    sample rate to 32000. The two Signal Sources should have frequencies
    of 1000 and 800, respectively. The
    [Add](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s08s01.html) block
    is found in the *Math Operators* category.

-   Generate and execute the flow graph. On the Scope plot you should
    observe a waveform corresponding to the sum of two sinusoids. On the
    FFT plot you should see components at both 800 and 1000 Hz.
    Unfortunately, the FFT plot does not provide enough resolution to
    clearly see the two distinct components. Note that the maximum
    frequency displayed on this plot is 16 kHz. This is one-half of the
    32 kHz sample rate. In order to obtain better resolution, we can
    lower the sample rate. Try lowering the sample rate to 10 kHz.
    Recall that for an FFT, the frequency resolution *f0=fs/N* where
    *fs* is the sample rate and *N* is the FFT block size. Thus for
    fixed value of *N*, *f0* goes down as *fs* goes down.

-   Replace the *Add* block with a
    [Multiply](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s08s04.html)
    block. What output do you expect from the product of two sinusoids?
    Confirm your result on the Scope and FFT displays.

-   Take note of the other math operations under the *Math Operators*
    category and experiment with a few to see if the result is as
    expected.

### Filters

-   Modify the flow graph to include a [Low Pass
    Filter](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s01.html)
    block as shown in [figure\_title](#lowpass_filter). This block is
    found in the *Filters* category and is the first Low Pass Filter
    listed.

-   Recall that the Multiply block outputs a 200 Hz and a 1.8 kHz
    sinusoid. We want to create a filter that will pass the 200 Hz and
    block the 1.8 kHz component. This can be done with a low pass
    filter, whose frequency response is shown in
    [figure\_title](#transition_band). Double-click the block to open
    the properties dialog. Set the low pass filter to have a cutoff
    frequency of 1 kHz and a transition width of 200 Hz.

    Select the *FIR Type* to be *Float-\>Float (Decimating)*.

-   Generate and execute the flow graph. You should observe that only
    the 200 Hz component passes through the filter and the 1.8 KHz
    component is attenuated. How many dB down is the 1.8. KHz wave
    compared to the 200 Hz wave? Experiment with the High Pass Filter.

-   Using the same flow graph, change the sample rate variable to 20000.
    Change the Decimation in the Low Pass Filter to 2. Decimation
    decreases the number of samples that are processed. A decimation
    factor of two means that the output of the filter will have a sample
    rate equal to one-half of the input sample rate, or in this case
    only 10000 samples/sec. This is a sufficient sample rate for the
    frequencies that we are dealing with. Generate and execute the flow
    graph. What frequency do you observe on the FFT? Measure it
    precisely by letting the cursor hover over the peak of the observed
    component.,

-   You should have observed that the FFT is now measuring a signal
    around 400 Hz, rather than the expected 200Hz. Why is this error
    occurring? It is because the sample rate on the FFT has not been
    adjusted to properly measure its input. Double-click on the FFT Sink
    block and change the sample rate to samp\_rate/2. Generate and
    execute the flow graph. You should now read the correct frequency.
    **It is important to be aware of the sample rate in each branch of
    your flowgraph.** Decimation and Interpolation options decrease and
    increase the sample rate respectively.

### Running Generated Python Code

-   Open a file browser by going to Places-\>Home Folder as shown in
    [figure\_title](#home_folder).

-   Browse to the directory that contains the GRC file that you have
    been working on. If you are unsure as to where this is, the path to
    this file is shown in the bottom portion of the GRC window. In
    addition to saving a \".grc\" file with your flow graph, note that
    there is also a file titled \"top\_block.py\", as shown in
    [figure\_title](#python_code). This is the Python file that is
    generated by GRC. It is this file that is being run when you execute
    the flow graph.

-   Double-click on this file. You will be given the option to Run or
    Display this file (see [figure\_title](#python_code_run)).

-   Select Display. You can modify this file and run it from the
    terminal window. This allows you to use features that are not
    included in GRC. Keep in mind that every time you run your flow
    graph in GRC, it will overwrite the Python script that is generated.
    So, if you make changes directly in the Python script that you want
    to keep, save it under another name.

-   To learn more about writing flowgraphs directly in Python, see this
    [code
    example](http://gnuradio.org/redmine/projects/gnuradio/wiki/TutorialsWritePythonApplications#A-first-working-code-example).

-   It is possible to change the file name of the generated Python code
    by changing the *ID* field in the flowgraph\'s *Options* block.

### Conclusions

In this tutorial, you have learned several of the basic concepts in
using GRC. Make a brief list of these concepts. When you are comfortable
with this material, feel free to move on to tutorial 2.

Tutorial 2: Variables and Controls
----------------------------------

### Objectives

This tutorial illustrates some of the features available in GNU Radio
Companion when using WX GUI, such as sliders and other variable input
options. It is valuable to keep in mind while working through this
material that the visual flow graph is just a wrapper for the underlying
python code, and that the choosers and sliders represent variables in
the code.

In this tutorial you will learn how to:

-   add GUI controls such as sliders and radio buttons to your
    flowgraph.

-   use variables to connect controls to different flowgraph parameters.

### Working with Sliders

-   Launch GRC as done in the previous tutorial. If GRC is already open,
    simply create a new flowgraph by selecting File-\>New.

-   Construct the flow graph shown in
    [figure\_title](#tutorial2_fft_sink). Note that the sample rate is
    set to 48000 in this example.

-   Execute the flow graph. You should hear the composite tone and see
    the FFT sink display of the spectrum. Experiment with the FFT size
    in the FFT sink. It should be a power of two. Note that as you
    increase the FFT size the resolution of the display increases. Reset
    the FFT size to 1024 when you are done.

-   Add a *WX GUI Slider* (from the *GUI Widgets-\>WX* category) to the
    flow graph. Double-click on the block and set the parameters as
    shown in [figure\_title](#slider_properties).

-   The ID box is the name of the variable that will be used to assign
    control. The Label box is optional. If filled, it will be used as a
    label for the controller in the output display.

-   Execute the flow graph. This time when the FFT sink display opens
    you will see a horizontal slider at the top. Move the slider back
    and forth to change the value of freq2 between 10 and 2000. You
    should observe that this does not change the spectrum or the sound.
    This is because freq2 has not been assigned to control anything.

-   Double-click on the bottom *Signal Source* (the one set to 800 Hz).
    Replace the frequency (800) with freq2. Execute the flow graph. You
    should now observe that both the spectrum and the sound change as
    you vary the frequency of the Signal Source using the slider.

### Working with Text Boxes

-   Add a *WX GUI Text Box* to the flow graph (*GUI Widgets-\>WX*
    category). Set the parameters as shown in
    [figure\_title](#textbox_properties).

-   Double-click on the bottom Signal Source and replace the Amplitude
    (0.5) with the variable, level2. Execute the flow graph. Note that a
    text box will now appear in the display. The default value of 0.5
    will be entered. Change the value to 0.1 followed by Enter. The
    volume of the 800 Hz tone will decrease and this will be reflected
    on the spectrum plot. Do not vary the level above 1.0.

### Working with Choosers

-   Add a *WX GUI Chooser* block to the flow graph. This block will add
    either a drop down menu, radio buttons or a button. Input the
    parameters as shown in [figure\_title](#chooser_properties).

-   Change the Frequency of the top Signal Source (1 kHz) to freq1.
    Execute the flow graph and change the frequency of the top Signal
    Source using the radio buttons. Experiment with the Drop Down menu
    and the Button to see how they work.

### Working with Notebooks

-   Add a *WX GUI Notebook* block to the flow graph. This control allows
    you to arrange large GUI components (scope, FFT, waterfall, etc)
    into a tabbed notebook.

-   Set the *ID* field to notebook\_0 (this should be the default). Set
    the *Labels* field to \[\'Scope\', \'Spectrum\'\]. Note that this
    field is entered in Python list syntax and is expecting a list of
    strings. The square brackets indicate the list while the single
    quotes indicate the string. The comma is the separator between list
    items.

-   Add a *WX GUI Scope Sink* to the flowgraph and connect it to the
    output of the *Throttle* block. Double click this block and set the
    *Type* to *Float* and set the *Notebook* to *notebook\_0,0*, where
    notebook\_0 indicates the notebook control where you would like the
    element to appear and the second 0 indicates the list index of the
    label you would like it to appear under. In this case, 0 points to
    the list index of \'Scope\'. Close the properties dialog.

-   Double click the *WX GUI FFT Sink* to open the properties dialog.
    Set the *Notebook* to *notebook\_0,1*. The 1 points to the list
    index of \'Spectrum\' that was configured in the *Labels* field of
    notebook\_0. Close the properties dialog.

-   Execute the flowgraph. The scope and FFT views should now be visible
    on separate tabs labeled \"Scope\" and \"Spectrum\" repsectively.

### Conclusions

In this tutorial you have learned how to add GUI controls to your
flowgraph and how to use them to control different parameters of the
flowgraph. These skills will be useful when creating a tunable AM
receiver in the next tutorial. When you feel comfortable with this
material, please feel free to move on to Tutorial 3.

Tutorial 3A: AM Signal waveforms
--------------------------------

### Objectives

This tutorial is a guide to AM signal waveforms. In this tutorial you
will learn:

-   Theory and equations of AM signals and the complex mixer

-   How to construct an AM transmitter flowgraph to generate an AM
    waveform with a sinusoidal message and observe the waveform and
    spectrum

-   Construction of AM transmitter flowgraphs with square wave and
    pseudo-random data messages

-   AM receivers are covered in the next Tutorial 3B

### AM flowgraphs

-   Review the theory in the [AM transmitter
    theory](./data/35015-PSK-FSK-12.pdf) section 2.1.

-   Using the following GRC files as a starting point:

    -   [AM\_TX.grc](data/AM_TX.grc)

    -   [different\_waveforms.grc](data/different_waveforms.grc)

    Carry out the steps in the [AM Transmitter
    procedures](data/AM_procedures_TX.pdf)

-   Start GRC as was done in the previous tutorials. If GRC is already
    open, open the .grc files by selecting File-\>Open, or clicking on
    the Open logo, ![](images/open_logo.png)

-   If you are unsure of the functionality of any of the blocks in the
    linked tutorial, please consult the
    [Documentation](http://www.ece.uvic.ca/~ece350/grc_doc/) , or ask
    your TA.

-   Questions to be answered during the lab

    -   For an AM signal as written in the text section 2.1 page 35,
        what is the acceptable range of the parameter k\_a so that the
        message can be recovered perfectly in the receiver?

    -   Sketch the spectrum of an AM signal with a message signal that
        is the sum of two cosine waves. Repeat for a message signal that
        is the product of two cosine waves.

    -   What is the cutoff frequency of the low pass filter used in a
        synchronous AM receiver (where the received signal is multiplied
        with the carrier waveform and lowpass filtered).

    -   Consider a signal with sampling rate of 256KHz. We use rational
        resampler block with decimation factor of 3 and interpolation
        factor of 4. What would be the new sampling rate of the signal?

Tutorial 3B: Receiving AM Signals
---------------------------------

### Objectives

This tutorial is a guide to building a practical AM receiver for
receiving real AM signals. In section 2.5.2 you will learn how to
demodulate an AM signal using only real signals. A data file with one AM
signal, which was generated using the flowgraphs in section 3A, will be
used.

In section 2.5.2, a data file will be used that contains several seconds
of recorded signals from the AM broadcast band. In this section you will
learn how to:

-   use a pre-recorded file as the input to your flowgraph.

-   tune to a specific (desired) AM signal on a given carrier frequency.

-   filter out the undesired signals using other (different) carrier
    frequencies.

-   demodulate the desired AM signal using complex signals.

### Real signals, basic AM receiver

-   Review the [theory of AM receivers using real
    signals](data/AM_theory_RX.pdf)

-   Using the following file as a starting point:

    [AM\_PB\_RX.grc](data/AM_PB_RX.grc)

    Carry out the steps in the [AM receiver
    procedures](data/AM_procedures_RX.pdf)

### Complex signals, receiver with channel selection (tuning)

-   Review the [theory of AM receivers using complex
    signals](data/35015-PSK-FSK-12.pdf) section 3.2.

-   Click on the link below to download the data file used in this
    section. Save it in a location that you can access later. This file
    was created using a USRP receiver.

    -   [am\_usrp710.dat](data/am_usrp710.dat)

-   Start GRC as was done in the previous tutorials. If GRC is already
    open, simply create a new flowgraph by selecting File-\>New.

#### Playing a Data File

-   Construct the flow graph shown in [figure\_title](#am_data_file)
    consisting of a [File
    Source](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s07s03.html),
    *Throttle*, and *WX GUI FFT Sink*. Set the sample rate in the
    variable block to 256000. This is the rate at which the saved data
    was sampled.

-   Double-click on the *File Source* block. Click on the ellipsis (...)
    next to the *File* entry box. Locate the am\_usrp710.dat file that
    you saved in the previous step. The path to your file will appear as
    shown in [figure\_title](#file_source_dialog). Set the *Output Type*
    to *Complex*. The use of complex data to describe and process
    waveforms in SDR will be discussed in the next tutorial. Set
    *Repeat* to *Yes*. This will cause the data to repeat so that you
    have a continuously playing signal.

-   Save and execute the flow graph. You should observe an FFT display
    similar to the one shown in [figure\_title](#am_fft). You may need
    to click on *Autoscale* button to scale the data as shown. Note the
    following:

    -   This data was recorded with a USRP set to 710KHz. Thus, the
        signal you see at the center (indicated as 0 KHz) is actually at
        710 KHz. Similarly, the signal at 80 KHz is actually at 710KHz +
        80KHz = 790KHz.

    -   The display spans a frequency range from just below -120KHz to
        just above 120KHz. This exact span is 256KHz, which corresponds
        to the sample rate that the data was recorded at.

    -   The peaks that you observe on this display correspond to the
        carriers for AM broadcast signals. You should also be able to
        observe the sidebands for the stronger waveforms.

#### Frequency Display Resolution

In this step we will expand the frequency scale on the FFT display so
that you can view the signals with greater resolution. Recall from the
previous tutorial that the span of the frequency axis is determined by
the sample rate (256 kHz for this file). While we cannot change the
original data, we can resample it to either increase or decrease the
sample rate. We will decrease the sample rate by using decimation.
Modify the flow graph as follows:

-   Add a *Variable* block (under *Variables* category). Set the ID to
    resamp\_factor and the Value to 4 as shown in
    [figure\_title](#resamp_factor).

-   Add the *Rational Resampler* block from the *Filters* menu as shown
    below. Set its decimation factor to resamp\_factor. It will use the
    value of the variable set in the previous step (4) to decimate the
    incoming data. That means that it will divide the incoming data rate
    by the decimation factor. In this example, the incoming 256K
    samp/sec data will be converted down to 256K/4 = 64K samp/sec.

-   Note that the *Throttle* and *FFT Sink* now need their sample rates
    changed to correspond to this new rate. Change the sample rate in
    both of these blocks to samp\_rate/resamp\_factor. Now we can change
    the decimation factor in the *Variable* block and it will be
    reflected in each of the other blocks automatically.

-   Your flow graph should now appear as shown in
    [figure\_title](#fft_decim_graph).

-   Execute the new flow graph. You should now observe a frequency span
    of only 64 kHz (-32 kHz to +32 kHz). What actual frequency range
    does this correspond to?

#### Selecting one channel by filtering

The bandwidth of an AM broadcast signal is 10 kHz (+/- 5 kHz from the
carrier frequency). You may find it useful to click the *Stop* button on
the FFT plot to see this more clearly. Also, note that many stations
also include additional information outside of the 10 kHz bandwidth.

In order to select the station at 710 kHz (0 kHz on the FFT display) we
need to insert a filter to eliminate all but the one station that we
want to receive. This is often referred to as a channel filter. Since
the station at 710 kHz has been moved to 0 kHz (in the USRP) we will use
a low pass filter. The station bandwidth is 10 kHz, so we will use a low
pass filter that cuts off at 5 kHz.

-   Insert the [Low Pass
    Filter](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s01.html)
    (from the *Filters* menu) between the [Rational
    Resampler](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s07.html)
    and the *Throttle.*Set the parameters as shown in
    [figure\_title](#low_pass_dialog).

-   Execute the flow graph. You should see that only the station between
    +/- 5 kHz remains.

#### AM Demodulation

The next step is to demodulate the signal. In the case of AM, the
baseband signal is the envelope or the magnitude of the modulated
waveform. GNU Radio contains a *Complex to Mag* block (in the *Type
Converters* category) that can be used for this purpose. Again, the use
of complex signal representation will be dealt with in depth in the
future.

-   Insert the [Complex to
    Mag](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s11s06.html) block
    between the *Low Pass Filter* and the *Throttle*.

    -   Note that the titles of some of the blocks are now red and the
        Execute Flow Graph icon is dimmed. This indicates an error.
        Prior to adding this block, all of the block inputs and outputs
        were complex values. However, the output of the *Complex to Mag*
        block is *Float* (a real number). Thus, any blocks following
        this block should be Type: Float. **Modify the** *Throttle*
        **and** *WX GUI FFT Sink* **accordingly**.

-   Execute the flow graph. You should now observe the spectrum of the
    baseband signal in the *FFT Sink*. Note that since the input data
    type to the *FFT Sink* is Float, only the positive frequency
    spectrum is displayed.

#### Matching the Audio Sample Rate

The next step is to listen to this demodulated waveform to confirm that
it is in fact receiving the baseband signal.

-   Remove the *Throttle* and the *FFT Blocks*.

-   Add an *Audio Sink* block to the output of the *Complex to Mag*
    block. Set the sample rate of the *Audio Sink* to 48 kHz.

-   Note that the sample rate out of the *Complex to Mag* block is 64
    kHz and the input to the *Audio Sink* is 48 kHz. In order to convert
    64 kHz to 48 kHz we need to divide (decimate) by 4 and multiply
    (interpolate) by 3. Insert a *Rational Resampler* between the
    *Complex to Mag* and *Audio Sink* blocks and set the decimation and
    interpolation as noted above. Also set its Type to *Float-\>Float
    (Real Taps)*.

-   Since the output of the *Complex to Mag* is always positive, there
    will be a DC offset on the audio signal. The signal going to the
    audio hardware should not have any DC offset. Place a [DC
    Blocker](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s05.html) (in
    the *Filters* category) between the *Complex to Mag* block and the
    *Rational Resampler* added in the previous step.

-   Place a *WX GUI Scope Sink* at the output of the *Rational
    Resampler* (in addition to the *Audio Sink*). Change its Type to
    Float and set its sample rate to 48000. The flow graph should be
    similar to the one shown in
    [figure\_title](#am_receiver_no_tuning_no_volume).

-   Execute the flow graph. The *WX GUI Scope Sink* should open and
    display the output waveform. However, you may not yet hear the audio
    from your speaker or it may be very distorted. This is due to the
    fact that the values of the samples going in to the *Audio Sink*
    block are outside the range expected by the *Audio Sink*. The *Audio
    Sink* requires that the sample values are between -1.0 and 1.0 in
    order to play them back through the audio hardware.

#### Adding a Volume Control

-   Insert a [Multiply
    Const](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s08s05.html) block
    from the *Math Operators* category between the *DC Blocker* and the
    *Rational Resampler*. Set the IO Type of the block to Float.

-   Add a *WX GUI Slider* block. Set the parameters as shown in
    [figure\_title](#am_volume).

-   Set the constant in the *Multiply Const* block to \"volume\" so that
    the slider controls it. The final flow graph is shown in
    [figure\_title](#am_receiver_no_tuning).

-   Execute the flow graph. You should now hear the demodulated AM
    signal. Stop the flowgraph.

-   Double click on the *Low Pass Filter*. Note that it can also
    decimate. Change the decimation in the *Low Pass Filter* block to
    resamp\_factor and set the sample rate back to samp\_rate. Remove
    the *Rational Resampler* between the *File Source* and the *Low Pass
    Filter*. The filter now handles both operations. Test the receiver
    again.

#### Tuning to a desired station (channel)

-   Review the [section 3.2.2 theory of tuning to a radio
    station](data/35015-PSK-FSK-12.pdf).

-   Place an *FFT Sink* at the output of the *File Source*, leaving the
    rest of the flow graph unchanged as shown in
    [figure\_title](#am_receiver_fixed_tuning).

-   Execute the flow graph and observe the location of the other
    stations in the spectrum. Note that there is a fairly strong signal
    at 80 KHz (really 710 + 80 = 790 KHz).

-   In order to receive this signal we need to shift it down to zero
    frequency so that it will pass through the low pass filter. One way
    to accomplish this is to multiply it by a sinusoid. Modify the flow
    graph as shown below. Add a *Signal Source* and set its parameters
    to output a cosine at a frequency of -80000. This negative frequency
    will shift the entire spectrum to the left by 80KHz. Use a
    *Multiply* block and move the *FFT Sink* to observe its output. Test
    this receiver.

-   Add another *WX GUI Slider* so that you can adjust the frequency
    with a slider. Set the minimum to (-samp\_rate/2) and the maximum to
    (samp\_rate/2). Test your flow graph and demonstrate that it works.
    You may need to adjust your volume slider for each station. This is
    because the stations are at varying distances away from the receiver
    and have different transmitted power. (Remember the link equation?)

#### Automatic Gain Control

The volume adjustment can be automated with an [Automatic Gain Control
(AGC) block](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s01s01.html).
This block works by sampling its own output and adjusting its gain to
keep the average output at a particular level.

-   Insert the *AGC* block (found under *Level Controls*) between the
    *Low Pass Filter* and the *Complex to Mag* block. The *AGC* will
    adjust the gain so that the sample values are always in a suitable
    range for the audio hardware. Leave the parameters at their default
    values.

-   You can now remove the *Multiply Const* and volume slider. Test the
    receiver again. Adjust the volume to a comfortable level using the
    computer\'s volume control on the first station you hear. Now tune
    up and down the band and notice that you no longer need to adjust
    the volume, but the noise level increases for weaker stations. The
    radio functions the same as a hardware radio.

Tutorial 4: Complex Signals and Receiving SSB
---------------------------------------------

### Objectives

This tutorial is a guide to receiving SSB signals. It will also
illustrate some of the properties of complex (analytic) signals and show
why we use them in communications systems. In this tutorial you will:

-   Use the discrete Hilbert transform to create a complex signal from a
    real signal.

-   Use a frequency-translating filter to perform filtering and tuning
    in one step.

-   Construct an SSB demodulator using Weaver\'s Method.

### Complex/Analytic Signals

-   Review the [sections 2.3 and 3.4 theory of analytic signals and SSB
    receivers](data/35015-PSK-FSK-12.pdf).

#### Hilbert Transforms

-   Open a new flow graph in GRC. Create the simple flow graph shown in
    [figure\_title](#tutorial4_sinewave). Set the Type in each of the
    three blocks to Float as you have in the past. Other than that you
    can leave all of the values at their default settings.

-   Execute the flow graph. The scope sink should open and display a
    sinusoidal signal. Convince yourself that this signal has the
    amplitude and frequency that you expect.

-   Modify the flow graph by changing the Type in each of the three
    blocks to *Complex*. Execute the flow graph. Your scope plot should
    now display two sinusoids that are 90° out of phase with each other.
    The leading (channel 1) wave is the I or in-phase component of the
    complex signal and the lagging (channel 2) wave is the Q or
    quadrature component. When a signal source is set to *Complex*, it
    will output both the I and Q components.

-   Modify your flow graph as shown in
    [figure\_title](#tutorial4_square). The *Signal Source* should be
    set to output a Square wave with a Type of Float. Thus, the first
    *Scope Sink* and the *Throttle* must also be set to accept Float
    values.

-   The
    [Hilbert](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s06.html)
    block is found in the *Filters* category. This block outputs both
    the real input signal and the Hilbert transform of the input signal
    as a complex signal. Leave the number of taps at its default setting
    of 64. Since the output of this block is complex, the second *Scope
    Sink* must be set to accept complex inputs.

-   Execute the flow graph. Two scope plots should open. One should
    contain the square wave output from the *Signal Source* only. The
    other should include both the original square wave and its Hilbert
    Transform. Do you understand why the Hilbert transform of a square
    wave looks this way?

-   As shown in [figure\_title](#tutorial4_square), the *Signal Source*
    can be set to output a complex signal and display both the I and Q
    components. Modify the flow graph as shown in
    [figure\_title](#tutorial4_square2).

-   Set the *Signal Source* to output a complex waveform. Make sure the
    *Throttle* and *Scope Sink* are also set to complex.

-   Execute the flow graph. Is the complex waveform displayed here the
    same as the one obtained from the Hilbert transform? Your answer
    should be NO. This is incorrect. GRC is NOT displaying the correct Q
    component of a complex square wave. The Hilbert transform did output
    the proper waveform.

#### Complex Multiplication

-   Create the flow graph shown in [figure\_title](#tutorial4_multiply).
    Make sure that all of the blocks are set to Type: Float. This flow
    graph takes two sinusoids, at frequencies of 1KHz and 10 KHz and
    multiplies them together. Using a trigonometric identity we know
    that the product of two cosines gives two cosines at the sum and
    difference frequencies of the original signals. In this case we
    expect outputs at 9 kHz (difference) and 11 kHz (sum).

-   Execute the flow graph and confirm this result. Note that the FFT
    plot only shows the positive frequency spectrum when it is set to
    Type: Float. We know that for real inputs the negative frequency
    components are the same as positive frequency components.

-   Change ALL of the blocks to Type: Complex and execute the flow graph
    again. You should now observe a single output at 11 kHz. This is the
    original 10 kHz signal shifted by the 1 kHz signal. If we want to
    shift in the negative direction a frequency of -1000 can be used.
    Try this. From this example we see two of the primary advantages of
    using analytic signals. A signal can be shifted (sum) without
    creating an additional difference signal. Also, note that there are
    NO negative frequency components. Why is this?

### Single Sideband (SSB) Signals

In this section you will learn one technique for demodulating Single
Sideband Signals. The following data file will be used for the first
part of this tutorial:

[ssb\_lsb\_256k\_complex2.dat](data/ssb_lsb_256k_complex2.dat)

This data file was recorded by a USRP set to a center frequency of
50.3MHz with a sample rate of 256KHz

-   Create a new flow graph as shown in
    [figure\_title](#tutorial4_file_source). The *File Source* should be
    set to the data file that you just downloaded. The *Variable* block
    which sets the sampling rate (samp\_rate) should be set to 256000 as
    this is the data rate that the received signal was sampled at. The
    *Throttle* and *FFT Sink* can be left at their default settings.

-   Execute the flow graph. After the FFT Plot window opens, adjust the
    *Ref Level* so that the amplitude values start at 10 dB and set the
    *dB/div* to 10dB/div. You should view a section of the spectrum that
    is 256 kHz wide (due to the sample rate). Note that there is one
    signal visible between 40 and 60 kHz.

-   When this signal was recorded, the USRP was set to a frequency of
    50.3 MHz. Thus, the 0 kHz point on the display corresponds to 50.3
    MHz. While the FFT Plot is displayed move the cursor over the signal
    and note the frequency along its right edge. It should be
    approximately 53 kHz. Since this is a lower sideband (LSB) signal,
    this corresponds to the carrier frequency. Because the \"zero\"
    frequency corresponds to 50.3 MHz, the original carrier frequency of
    signal was 50.3 MHz + 53 kHz = 50.353 MHz. However, now that the
    spectrum has been shifted down by 50.3 MHz, we use the carrier
    frequency of 53 kHz.

### Frequency Translating Filter

The first step in building a receiver is to use a channel filter to pass
the signal of interest and filter out the rest of the signals in the
band. This is done as follows

1.  First the signal of interest is shifted down to zero frequency as
    shown in [figure\_title](#tutorial4_shift1).

2.  Next a low pass filter is applied so that the other signals will be
    filtered out as shown in [figure\_title](#tutorial4_shift2).

In GRC, the *Frequency Xlating FIR Filter* performs both of these
operations.

-   Insert [Frequency Xlating FIR
    Filter](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s12s08.html)
    block between the *File Source* and the *Throttle*.

-   Complete the properties window as shown in
    [figure\_title](#tutorial4_freq_xlating_properties). The center
    frequency of 51500 will shift the entire spectrum down by 51500 Hz.

    -   Note: The function indicated in the *Taps* parameter generates
        the taps for a low pass filter with a gain of 1 (in the pass
        band), a sampling rate equal to samp\_rate (256 kHz), a cutoff
        frequency of 2 kHz and a transition width of 100 Hz.

-   Execute the flow graph. You will see that your signal has now moved
    down to the origin and is the only signal present.

-   Now that we have located the signal of interest, there is no reason
    that we need to be concerned with so much of the adjacent spectrum.
    We can reduce the range of frequencies that are being processed by
    reducing the sample rate (decimation). Re-open the *Frequency
    Xlating FIR Filter* block and change the *Decimation* parameter
    to 8. This will reduce the sample rate to 256000/8 = 32000. Change
    the sample rate of the *Throttle* and *FFT Sink* to this new rate.
    What frequency range to you expect the FFT to display now?

-   Execute the flow graph again to see if you are correct. You should
    now observe an expanded version of your signal. Select *Autoscale*
    on the FFT Plot so that the peaks of the signal are observed. Notice
    that after a while, the signal level will be reduced for a few
    seconds. That occurs when the station stops transmitting.

### Using the firdes Module

In the previous step, we used the firdes module of GNU Radio. For more
information on this tool, follow the link below.

[gr::filter::firdes Class
Reference](http://gnuradio.org/doc/doxygen/classgr_1_1filter_1_1firdes.html#details)

This module is used for generating finite impulse response (FIR) filters
in GNU Radio. There are a number of filters available that can be
explored in the API Reference link above. Some of the commonly used
filters are listed below. The basic usage format is
**firdes.filter\_type(args)** where **filter\_type(args)** is one of:

-   band\_pass(gain, sampling\_freq, low\_cutoff\_freq,
    high\_cutoff\_freq, transition\_width)

-   band\_reject(gain, sampling\_freq, low\_cutoff\_freq,
    high\_cutoff\_freq, transition\_width)

-   complex\_band\_pass(gain, sampling\_freq, low\_cutoff\_freq,
    high\_cutoff\_freq, transition\_width)

-   high\_pass(gain, sampling\_freq, cutoff\_freq, transition\_width)

-   low\_pass(gain, sampling\_freq, cutoff\_freq, transition\_width)

This list indicates the minimum number of arguments required for the
filter to be generated. Each filter can also take an argument for
the**type of window** it uses and the **beta value**. Additionally, each
of these filter types has a \"\_2\" version (ie: band\_pass\_2,
low\_pass\_2). These versions take an extra parameter which specifies
the stop band attenuation in dB. It is worthwhile to familiarize
yourself with the usage of this module as it will be used throughout
these labs.

### Weaver Demodulator

Recall that the signal is a complex (analytic) signal. One method of
demodulating SSB voice is to operate on the real and imaginary parts of
the signal separately. The *Complex to Float* block will take a complex
signal and output its real (re) and imaginary (im) parts separately.

-   Modify the flow graph to appear as shown in
    [figure\_title](#tutorial4_real_imag_spectrum). The outputs of the
    [Complex to
    Float](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s11s03.html) block
    are both real so the *FFT Sinks* need to be changed to Type: Float.

-   Execute the flow graph. You should now observe the spectra of the
    real and imaginary parts of the signal. Note that the signals extend
    out to 2KHz, the cutoff frequency of the filter.

-   One method of demodulating this SSB voice signal, known as Weaver's
    method, takes the real and imaginary part of the signal and
    processes them as shown in [figure\_title](#tutorial4_weaver_demod).
    Use the *Signal Source* in GRC to generate the cosine and sine waves
    needed to implement this demodulator. The *Multiply* and *Add*
    blocks can be found in the *Math Operators* category.

-   Observe the output of the *Add* block using an *FFT sink*. This is
    the baseband signal that has been extracted from the modulated SSB
    signal.

-   The final step is to listen to the demodulated signal. Add an *Audio
    Sink* as demonstrated in Tutorial 3. Recall that you will need a
    *Rational Resampler* to adjust the sampling rate to one that works
    with the *Audio Sink*.

-   You will also need a multiplier to reduce the amplitude of the
    signal before it enters the *Audio Sink*. Find a suitable value by
    first observing the maximum peak on a scope sink and using the
    reciprocal of this value as the multiplier.

-   Test your SSB receiver; you should hear the voice.

    -   Note: It may be helpful to add a *waterfall sink* to aid in
        locating the signal of interest.

-   The Weaver demodulator can also be implemented entirely with complex
    signals. Create a second SSB receiver using only complex signals,
    with conversion to real just before the audio sink. Test this
    receiver and confirm that it works in the same way as the receiver
    using real signals.

-   Test this receiver using the data file below

    [SDRSharp\_20130920\_024052Z\_14190kHz\_IQ.wav](./data/SDRSharp_20130920_024052Z_14190kHz_IQ.wav)

    This is a WAV file! To read it in GNURadio:

    -   Add a *Wav File Source* and modify its properties as shown in
        [figure\_title](#wav_file_properties):

    -   This WAV file was recorded using the I and Q streams for the L
        and R channels. By setting the block to have 2 output channels
        you will be able to use the full I/Q signal.

    -   Add a [Float To
        Complex](http://www.ece.uvic.ca/~ece350/grc_doc/ar01s11s10.html)
        block to convert from I and Q to a complex signal.

-   There are two SSB voice signals in this file, both are upper
    sideband (USB), whereas the first data file was lower sideband
    (LSB). The Weaver demodulator needs a small modification to work
    with USB.

    -   Hint: Refer to the diagram above illustrating the Weaver
        Demodulator and now consider using the upper sideband

-   A data file taken using a software receiver with a wire antenna
    about 6 meters above the ground is found here:

    [SDRSharp\_20130919\_004154Z\_14053kHz\_IQ](./data/SDRSharp_20130919_004154Z_14053kHz_IQ.wav).

    -   Change the Wav File Source to read this file, and test your
        receiver using this file.

    -   The file contains mostly Morse code signals, no voice signals.
        Replace the fixed offset of 1500 Hz with a variable and control
        it with a WX GUI Slider. Explain what happens when the slider is
        moved and why.

    -   Replace the fixed bandwidth of the firdes module with a variable
        and control it with a Slider. For receiving Morse code signals,
        a bandwidth of 50-200 Hz is best.

Save this flowgraph. You can modify it for use with the RTL-SDR receiver
and listen to live Morse code and SSB signals in the frequency range
24.9-25.0 MHz, 27-29 MHz, 50.0-50.2 MHz. These frequencies will
propagate over long distances via the ionosphere for some (not all) of
the time. Other frequencies are 144.0-144.3 MHz and 145.8-146.0 MHz.
