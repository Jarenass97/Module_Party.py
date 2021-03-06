#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do
  ndni=$(echo $line | cut -d',' -f1)
  letra=$(echo $line | cut -d',' -f2)
  dni=$ndni$letra
  name=$(echo $line | cut -d',' -f3)
  Birthday=$(echo $line | cut -d',' -f4)
  email=$(echo $line | cut -d',' -f5)
  echo "<record id='assistant$dni' model='party.assistant'>"
  echo "<field name='dni'>$dni</field>"
  echo "<field name='Birthday'>$Birthday</field>"
  echo "<field name='email'>$email</field>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
