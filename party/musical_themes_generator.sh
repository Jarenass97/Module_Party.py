#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do

  id=$(echo $line | cut -d',' -f1)
  title=$(echo $line | cut -d',' -f2)
  release_Date=$(echo $line | cut -d',' -f3)
  duration=$(echo $line | cut -d',' -f4)
  is_group=$(echo $line | cut -d',' -f5)
  echo "<record id='musical_theme$id' model='party.musical_theme'>"
  echo "<field name='title'>$title</field>"
  echo "<field name='release_Date'>$release_Date</field>"
  echo "<field name='duration'>$duration</field>"
  echo "<field name='is_group'>$is_group</field>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
