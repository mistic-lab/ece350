#!/bin/bash

user=`whoami`

scp -r data ${user}@wireless.ece.uvic.ca:/home/ece350/.www/lab_manual
