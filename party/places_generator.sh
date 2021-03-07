#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do
  id=$(echo $line | cut -d',' -f1)
  name=$(echo $line | cut -d',' -f2)
  echo "<record id='place$id' model='party.place'>"
  echo "<field name='name'>$name</field>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"