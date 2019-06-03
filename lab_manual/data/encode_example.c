//
// ELEC350 PSK31 Beacon Message Encoder Example
//

#include <stdio.h>
#include <string.h>
#include "varicode.h"

// You may change these value to suit your preferences.

// Maximum length of the user message. 
#define USER_MESSAGE_LENGTH 100

// Output file name
#define FILENAME "output.dat"

// Add a preamble of 0's to help the receiver sync up?
#define PREAMBLE_LENGTH 16

// Maximum length of varicode is 10 bits, plus 2 bits between characters.
// Add a preamble and postamble (same length). This is an upper bound on
// how many bits are required.
#define ENCODED_MESSAGE_LENGTH PREAMBLE_LENGTH+(10+2)*USER_MESSAGE_LENGTH+PREAMBLE_LENGTH

// Varicode encoding function
void myVaricodeEncodingFunction(char *in, char *out) {

  //////////////////////////////////////////////////////////////////
  // The following code is for illustration purposes only. This code
  // does not do the Varicode encoding but illustrates how you might
  // use the Varicode table provided.
  int i;
  const char const *encoding_tbl[] = { "1010", "1011" };

  // Initialize the output string
  *out = 0;

  // Add encoded characters to the output string
  printf("Encoding user message: %s", in);
  for (i = 0; i < strlen(in); i++) {
    strcat(out, encoding_tbl[in[i]%2]);
  }

  printf("Encoded user message as %s\n", out);
  // END OF EXAMPLE CODE
  //////////////////////////////////////////////////////////////////

}

// Differential encoding function
int myDifferentialEncodingFunction(char *in, float *out) {

  int num_bits = 0;

  //////////////////////////////////////////////////////////////////
  // The following code is for illustration purposes only. This code
  // does not do the differential encoding, it only illustrates
  // how you might fill the array of floats using the input string.
  int i;

  for (i = 0; i < strlen(in); i++) {
    if (in[i] == '0') {
      out[i] = -1.0;
    } else {
      out[i] = 1.0;
    }
  }
   
  printf("Encoded %s as ", in);
  for (i = 0; i < num_bits; i++) {
    printf("%.1f ", out[i]);
  }
  printf("\n");

  num_bits = strlen(in);
  // END OF EXAMPLE CODE
  //////////////////////////////////////////////////////////////////

  return num_bits; // Number of differentially encoded bits.

}

int main(void) {

  // Hold the message input by the user (chars)
  char  userMsg[USER_MESSAGE_LENGTH];

  // Message translated to varicode alphabet (chars)
  char  varicodeMsg[ENCODED_MESSAGE_LENGTH];

  // Differentially encoded message (floats)
  float encodedMsg[ENCODED_MESSAGE_LENGTH];

  // Length of differentially encoded message.
  unsigned int len;

  // Output file
  FILE *outfile;

  // Get the user message string using fgets.
  printf("Message String: ");
  fgets(userMsg, USER_MESSAGE_LENGTH, stdin);
  
  // Call your own function to translate the 
  // ASCII input characters to Varicode strings.
  myVaricodeEncodingFunction(userMsg, varicodeMsg);
  
  // Call your own function to perform the differential 
  // encoding on the varicode string.
  len = myDifferentialEncodingFunction(varicodeMsg, encodedMsg);

  // Write the output file
  printf("Writing %s...\n", FILENAME);

  outfile = fopen(FILENAME, "wb");
  if (outfile == NULL) {
    printf("Could not open %s.", FILENAME);
    return -1;
  }

  fwrite(encodedMsg, sizeof(float), len, outfile);
  fclose(outfile);

  printf("Done.\n");

  return 0;

}

// END OF CODE
