#!/bin/bash
mkdir Modified

find . -type f -name "*.txt" -exec rename 's/\.txt$/.bak/' {} +

find . -type f -name "*.bak" -exec mv {} Modified/ \;