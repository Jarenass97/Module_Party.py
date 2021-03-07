#!/bin/bash

echo "<odoo>"
echo "<data>"
while read line
do
  id=$(echo $line | cut -d',' -f1)
  name=$(echo $line | cut -d',' -f2)
  date=$(echo $line | cut -d',' -f3)
  numID=$(echo $line | cut -d',' -f4)
  place='party.place'$numID
  echo "<record id='party$id' model='party.party'>"
  echo "<field name='name'>$name</field>"
  echo "<field name='date'>$date</field>"
  echo "<field name='place' ref='$place'/>"
  echo "<field name='films' eval=\"[(6,0,[ref('party.film$id'),ref('party.film$numID')])]\"/>"
  echo "<field name='musical_themes' eval=\"[(6,0,[ref('party.musical_theme$id'),ref('party.musical_theme$numID')])]\"/>"
  echo "<field name='assistants' eval=\"[(6,0,[ref('party.assistant$id'),ref('party.assistant$numID')])]\"/>"
  echo "</record>"
done
echo "</data>"
echo "</odoo>"
