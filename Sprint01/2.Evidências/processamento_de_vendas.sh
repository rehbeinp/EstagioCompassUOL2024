#!/bin/bash
if [ ! -d /home/paula/vendas ] ; then
        mkdir vendas
fi
cd
cd ecommerce
cp dados_de_vendas.csv ../
cd --
cp dados_de_vendas.csv vendas
cd vendas
if [ ! -d /home/paula/vendas/backup ] ; then
        mkdir backup
fi
cp dados_de_vendas.csv backup
cd backup
touch dados-`date +%Y%m%d`.csv
cp dados_de_vendas.csv dados-`date +%Y%m%d`.csv
mv dados-`date +%Y%m%d`.csv backup-dados-`date +%Y%m%d`.csv
touch relatorio.txt
date +%Y/%m/%d\ %H:%M >> relatorio.txt
touch reserva.txt
head -n2 backup-dados-`date +%Y%m%d`.csv >> reserva.txt
tail -n1 backup-dados-`date +%Y%m%d`.csv >> reserva.txt
cut -d',' -f 5 reserva.txt >> reserva.txt
tail -n2 reserva.txt >> relatorio.txt
rm reserva.txt
echo $(cut -d',' -f 3  backup-dados-`date +%Y%m%d`.csv | paste -sd+ | bc) >> relatorio.txt
head -n 10 backup-dados-`date +%Y%m%d`.csv
head -n 10 backup-dados-`date +%Y%m%d`.csv >> relatorio.txt
zip -r backup-dados-`date +%Y%m%d`.zip backup-dados-`date +%Y%m%d`.csv
rm backup-dados-`date +%Y%m%d`.csv
cd ../
rm dados_de_vendas.csv
