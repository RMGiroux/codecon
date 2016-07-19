#!/bin/bash

for i in $(seq 1 99); do if [[ -e test.$i ]]; then echo $i; if [[ $(python ../lannisters.py < test.$i) != $(<result.$i) ]]; then echo "TEST $i FAILED"; fi; fi; done
