#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do

  id=$(echo $line | cut -d',' -f1)
  title=$(echo $line | cut -d',' -f2)
  country=$(echo $line | cut -d',' -f3)
  release_Date=$(echo $line | cut -d',' -f4)
  language=$(echo $line | cut -d',' -f5)
  echo "<record id='film$id' model='party.film'>"
  echo "<field name='title'>$title</field>"
  echo "<field name='country'>$country</field>"
  echo "<field name='release_Date'>$release_Date</field>"
  echo "<field name='language'>$language</field>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
