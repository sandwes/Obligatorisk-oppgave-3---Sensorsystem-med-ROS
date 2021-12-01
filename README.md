# Obligatorisk-oppgave-3---Sensorsystem-med-ROS
Obligatorisk oppgave 3 - Sensorsystem med ROS
Video som viser løsning: https://www.youtube.com/watch?v=hbGDS6TPQII

Dette systemet er satt opp ved bruk av en launch-fil med navn «sensordata.launch». Det brukes en service med navn «do_filter_calc.srv», to msg-er med navn «FilteredValue.msg» og «RawValue.msg», to topics med navn «fpmg_raw» og «fpmg_filtered», og fire ulike nodes med navn «filter_server.py», «filter_client.py», «visualizer.py» og «sensordata_publisher.py». 
Filen med navnet «Sensordata_publisher» leser pulsdata fra .csv-filen som ble laget i forrige obligatoriske oppgave, denne pulsdataen blir så publisert som en RawValue til til fpmg_raw.
Filter_client.py subsriber på fpmg_raw og forespør den filterte verdien av servicen do_filter_calc. Etter at Filter_client.py mottar denne filterte verdien, blir den deretter publisert som FilteredValue-melding til fpmg_filtered. Filter_server lytter etter forespørsler på do_filter_calc og filtrerer bort alle verdier >110 og alle verdier <60. visualizer.py subsriber på fpmg_raw og fpmg_filtered, og matplotlib brukes for å visualisere dette i en bildefil. Et bash-script flytter deretter dette til den lokale webserveren. sensordata.launch starter opp roscore/ros master og alle nodene, og på denne måten slipper man å kjøre rosrun i ulike terminaler.

Resultat:
Når det gjelder resultatet så føler jeg at det er så nøyaktig som man får det, jeg har normalt dårlig erfaring med pulsmålere, selv de dyreste treningsklokkene og pulsbeltene klarer ikke å måle pulsen min nøyaktig før jeg er virkelig i gang med treningen. Derfor er jeg fornøyd med resultatet i seg selv, spesielt hvis man ser på de filtrerte verdiene. 
