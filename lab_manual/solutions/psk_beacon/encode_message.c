//
// ELEC350 PSK31 Beacon Message Encoder
// Stephen Harrison
//

#include <stdio.h>
#include <string.h>
#include "varicode.h"

#define USER_MESSAGE_LENGTH 100
#define PREAMBLE_LENGTH 16
#define ENCODED_MESSAGE_LENGTH 2*PREAMBLE_LENGTH+12*USER_MESSAGE_LENGTH
#define FILENAME "output.dat"

int encodePSK31(char *userMsg, char *varicodeMsg) {

  unsigned int i;

  *varicodeMsg = 0;

  for (i = 0; i < PREAMBLE_LENGTH; i++) {
    strcat(varicodeMsg, "0");
  }

  for (i = 0; i < strlen(userMsg); i++) {
    strcat(varicodeMsg, varicode_tbl[userMsg[i]]);
    strcat(varicodeMsg, "00");
  }

  for (i = 0; i < PREAMBLE_LENGTH-2; i++) {
    strcat(varicodeMsg, "0");
  }

  return 0;

}

int encodeDifferential(char *varicodeMsg, float *encodedMsg) {

  unsigned int i;

  // Assume the initial phase is 0 degrees
  encodedMsg[0] = 1.0;

  // Do the differential encoding
  for (i = 0; i < strlen(varicodeMsg); i++) {

    // '1' means no change in carrier phase.
    if (varicodeMsg[i] == '1') {
      encodedMsg[i+1] = encodedMsg[i];
    } 

    // else change the carrier phase.
    else {
      if (encodedMsg[i] == 1.0) {
	encodedMsg[i+1] = -1.0;
      } else {
	encodedMsg[i+1] = 1.0;
      }
    }
  }

  // Make sure that the message ends with 180 degrees so that 
  // we can play it in a loop

  if (encodedMsg[i] == 1.0) {
    encodedMsg[i+1] = -1.0;
    i++;
  }

  i++;

  return i;

}

int main(void) {

  char  userMsg[USER_MESSAGE_LENGTH];
  char  varicodeMsg[ENCODED_MESSAGE_LENGTH];
  float encodedMsg[ENCODED_MESSAGE_LENGTH];

  unsigned int i;
  int encLen;

  FILE *outfile;

  // Get the user message string.
  printf("Message String: ");
  fgets(userMsg, USER_MESSAGE_LENGTH, stdin);
  
  // Encode the message
  encodePSK31(userMsg, varicodeMsg);
  encLen = encodeDifferential(varicodeMsg, encodedMsg);

  // Print some stuff on the screen for the user's benefit.
  printf("Varicode Message: %s\n", varicodeMsg);
  printf("Differentially Encoded Message: %.1f", encodedMsg[0]);

  for (i = 1; i < encLen; i++) {
    printf(", %.1f", encodedMsg[i]);
  }

  printf("\n");

  // Write the output file
  printf("Writing %s...\n", FILENAME);

  outfile = fopen(FILENAME, "wb");
  if (outfile == NULL) {
    printf("Could not open %s.", FILENAME);
    return -1;
  }

  fwrite(encodedMsg, sizeof(float), encLen, outfile);
  fclose(outfile);

  printf("Done.\n");

  return 0;

}

// END OF CODE
