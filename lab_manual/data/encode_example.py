#!/usr/bin/env python
#
# ELEC350 PSK31 Beacon Message Encoder Example
#

from struct import pack
import varicode

def myVaricodeEncodingFunction(message):

    ##################################################################
    # The following code is for illustration purposes only. This code
    # does not do the Varicode encoding but illustrates how you might
    # use the Varicode table provided.
    encoding_tbl = { 0 : '1010', 1 : '1011' }
    
    print("Encoding user message: " + message[:-1])
    charList = [encoding_tbl[ord(char)%2] for char in list(message)]

    print("Encoded user message as " + ''.join(charList))
    return ''.join(charList)
    # END OF EXAMPLE CODE
    ##################################################################


def myDifferentialEncodingFunction(message):
    
    ##################################################################
    # The following code is for illustration purposes only. This code
    # does not do the differential encoding, it only illustrates
    # how you might fill the array of floats using the input string.
    out = []

    for char in list(message):
        if (char == '0'):
            out.append(-1.0)
        else:
            out.append(1.0)
   
    print("Encoded " + message + " as " + ' '.join([str(x) for x in out]))

    return out
    # END OF EXAMPLE CODE
    ##################################################################


if __name__ == "__main__":

    # Get the user message string.
    userMsg = raw_input('Message String: ')

    # Call your own function to translate the 
    # ASCII input characters to Varicode strings.
    varicodeMsg = myVaricodeEncodingFunction(userMsg + '\n')

    # Call your own function to perform the differential 
    # encoding on the varicode string.
    encodedMsg = myDifferentialEncodingFunction(varicodeMsg)

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
