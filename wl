#!/bin/bash

echo -n "weight?  "
read weight
echo "$(date "+%y-%m-%d"),$weight"
echo "$(date "+%y-%m-%d"),$weight" >> ~/.weight_log.dat
