printf 'Insira o HOST que será feito o ping: '
read -r HOST
printf 'Insira o numero de tentativas de ping: '
read -r MAX

for i in $(seq 1 ${MAX});
do
	ping -c 1 -D 8.8.8.8 | awk '{print $5"," $1"," $8}' | tr -d [ | tr -d : | tr -d ] | tr -d "time=" | grep 8.8.8.8 >> results.csv
done
