#!/usr/bin/env python
#
# ELEC350 PSK31 Beacon Message Encoder
# Stephen Harrison
#

from struct import pack
import varicode

def encodePSK31(message):

    # Create a list of the varicode strings based on the characters in the 
    # message.
    varicodeList = [varicode.dict[char] for char in list(message)]

    # Send 16 zeros and then join all of the varicode strings with 2 zeros
    # between.
    return '0' * 16 + '00'.join(varicodeList) + '0' * 16

def encodeDifferential(message):
    
    # Assume the initial phase is 0 degrees
    diffMessage = [1.0]
    
    # Do the differential encoding
    for char in list(message):

        # '1' means no change in carrier phase.
        if char == '1':
            diffMessage.append(diffMessage[-1])
        
        # else change the carrier phase
        else:
            if diffMessage[-1] == 1.0:
                diffMessage.append(-1.0)
            else:
                diffMessage.append(1.0)

    # Make sure that the message ends with 180 degrees so that 
    # we can play it in a loop
    if diffMessage[-1] == 1.0:
        diffMessage.append(-1.0)

    return diffMessage            

# Get the user message string.
userMsg = raw_input('Message String: ')

# Encode the message
varicodeMsg = encodePSK31(userMsg + '\n')
encodedMsg = encodeDifferential(varicodeMsg)

# Print some stuff on the screen for the user's benefit.
print('Varicode Message: ' + varicodeMsg)
print('Differentially Encoded Message: ' + ', '.join([str(x) for x in encodedMsg]))

# Write the output file
filename = 'output.dat'
print('Writing ' + filename + '...')

try:
    outfile = open(filename, 'w')
except:
    print('Could not open ' + filename + '.')
    exit(-1)

outputStr = ''.join([pack('f', x) for x in encodedMsg])
outfile.write(outputStr)
outfile.close()

print('Done.')

# END OF CODE
