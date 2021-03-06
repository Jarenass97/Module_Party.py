#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do
  id=$(echo $line | cut -d',' -f1)
  name=$(echo $line | cut -d',' -f2)
  place=$(echo $line | cut -d',' -f3)
  date=$(echo $line | cut -d',' -f4)
  is_group=$(echo $line | cut -d',' -f5)
  echo "<record id='party$id' model='party.party'>"
  echo "<field name='name'>$name</field>"
  echo "<field name='place'>$place</field>"
  echo "<field name='date'>$date</field>"  
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
