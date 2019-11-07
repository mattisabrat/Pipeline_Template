#!/usr/bin/env bash

while getopts ':i:b:o:n:f:' flag; do
  case "${flag}" in
    i) foo="${OPTARG}";;
    b) bar="${OPTARG}";;
    o) output="${OPTARG}";;
    n) nThreads=${OPTARG};;
    f) Order=${OPTARG};;
  esac
done

#Read in strings
Foo_str=$(cat $foo)
Bar_str=$(cat $bar)

case $Order in
    1)foobar_str="$Foo_str$Bar_str";;
    2)foobar_str="$Bar_str$Foo_str";;
esac

printf "$foobar_str" > $output
