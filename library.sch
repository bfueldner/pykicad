EESchema Schematic File Version 2
LIBS:library-rescue
LIBS:capacitor
LIBS:connector_phoenix
LIBS:connector_stift
LIBS:default
LIBS:diode
LIBS:driver
LIBS:inductor
LIBS:led
LIBS:logic
LIBS:mcu
LIBS:resistor
LIBS:rf
LIBS:supply
LIBS:transistor
LIBS:voltage_regulator
LIBS:library-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L capacitor_bipolar C1
U 1 1 54D3F067
P 5150 2050
F 0 "C1" H 5200 2150 60  0000 L CNN
F 1 "capacitor_bipolar" H 5200 1950 60  0000 L CNN
F 2 "footprint" V 5050 2050 60  0000 C CNN
F 3 "" H 5150 2050 60  0000 C CNN
	1    5150 2050
	1    0    0    -1  
$EndComp
$Comp
L diode D1
U 1 1 54D3F116
P 5350 3050
F 0 "D1" H 5350 3150 60  0000 C CNN
F 1 "diode" H 5350 2950 60  0000 C CNN
F 2 "footprint" H 5350 2850 60  0000 C CNN
F 3 "" H 5350 3050 60  0000 C CNN
	1    5350 3050
	1    0    0    -1  
$EndComp
$Comp
L resistor R1
U 1 1 54D3F195
P 4650 2550
F 0 "R1" H 4650 2550 60  0000 C CNN
F 1 "resistor" H 4650 2450 60  0000 C CNN
F 2 "footprint" H 4650 2650 60  0000 C CNN
F 3 "" H 4650 2550 60  0000 C CNN
	1    4650 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 2550 4250 3650
Wire Wire Line
	4250 3200 4400 3200
Wire Wire Line
	4400 2550 4250 2550
Connection ~ 4250 3200
$Comp
L BC557 T1
U 1 1 55912965
P 4600 3200
F 0 "T1" H 4400 3350 60  0000 L CNN
F 1 "BC557" H 4400 3050 60  0000 L CNN
F 2 "to_92" H 4500 2950 60  0001 C CNN
F 3 "doc/transistor/BC556_560.pdf" H 4500 2850 60  0001 C CNN
	1    4600 3200
	1    0    0    -1  
$EndComp
$EndSCHEMATC
