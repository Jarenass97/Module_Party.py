#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do
  id=$(echo $line | cut -d',' -f1)
  ndni=$(echo $line | cut -d',' -f2)
  letra=$(echo $line | cut -d',' -f3)
  dni=$ndni$letra
  name=$(echo $line | cut -d',' -f4)
  Birthday=$(echo $line | cut -d',' -f5)
  email=$(echo $line | cut -d',' -f6)
  echo "<record id='assistant$id' model='party.assistant'>"
  echo "<field name='dni'>$dni</field>"
  echo "<field name='name'>$name</field>"
  echo "<field name='Birthday'>$Birthday</field>"
  echo "<field name='email'>$email</field>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
