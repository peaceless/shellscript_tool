#!/bin/bash
aim=`pwd`/${1}
echo $aim
g++ -std=c++11 -g ${aim}
