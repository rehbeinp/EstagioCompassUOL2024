#!/bin/bash
cd
cd vendas
cd backup
if [ ! -a home/paula/vendas/backup/relatorio_fina.txt ] ; then
	touch relatorio_fina.txt
fi
cp relatorio.txt relatorio_fina.txt
rm relatorio.txt
