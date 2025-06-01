#!/bin/bash
for i in $(seq 3); do
  for j in $(seq 3); do
    if [[ $j -eq 2 ]]; then
      echo $j
      break 2  # Exits only the inner loop, default behavior
    fi
    # if [[ $j -eq 2 ]]; then
    #   echo $j
    #   break 2  # Exits both the inner and outer loops
    # fi
    echo "$i $j"
  done
done
