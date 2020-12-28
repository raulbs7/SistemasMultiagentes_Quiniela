#!/bin/bash

helpFunction()
{
   echo ""
   echo "Uso: $0 -L equipo_local -V equipo_visitante [-l id_agente_local | -v id_agente_visitante]"
   echo "\t-L Nombre del equipo local"
   echo "\t-V Nombre del equipo visitante"
   echo "\t-l Identificador para el agente recolector del equipo local"
   echo "\t-v Identificador para el agente recolector del equipo visitante"
   exit 1 # Exit script after printing help
}

while getopts "L:V:l:v:" opt
do
   case "$opt" in
      L ) equipo_local="$OPTARG" ;;
      V ) equipo_visitante="$OPTARG" ;;
      l ) id_agente_local="$OPTARG" ;;
      v ) id_agente_visitante="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$equipo_local" ] || [ -z "$equipo_visitante" ]
then
   echo "Alguno de los campos obligatorios están vacíos";
   helpFunction
fi

# Begin script in case all parameters are correct

python3 ./src/agenteReglas.py &
sleep 5
python3 -W ignore ./src/agenteRecolector.py $equipo_local $id_agente_local &
python3 -W ignore ./src/agenteRecolector.py $equipo_visitante $id_agente_visitante