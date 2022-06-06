#!/bin/bash

printf 'Insira o HOST que será feito o ping: '
read -r HOST
printf 'Insira o numero de tentativas de ping: '
read -r MAX

INIT_TIME=$1
mkdir -p resources/${INIT_TIME}

for i in $(seq 1 ${MAX});
do
	ping -c 1 -D 8.8.8.8 | awk '{print $5"," $1"," $8}' | tr -d [ | tr -d : | tr -d ] | tr -d "time=" | grep 8.8.8.8 >> "resources/${INIT_TIME}/results.csv"
	if [ $(($i % 10)) -eq '0' ]
	then
		echo $i
	fi
done
