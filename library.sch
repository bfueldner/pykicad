EESchema Schematic File Version 2
LIBS:logic
LIBS:discret
LIBS:transistor
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
L 74*05 IC2
U 1 1 54D3F0BF
P 4650 2900
F 0 "IC2" H 4800 3050 60  0000 C CNN
F 1 "74*05" H 4800 2750 60  0000 C CNN
F 2 "" H 4650 2900 60  0000 C CNN
F 3 "" H 4650 2900 60  0000 C CNN
	1    4650 2900
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
L 74*05 IC3
U 1 1 54D3FB70
P 6100 2750
F 0 "IC3" H 6250 2900 60  0000 C CNN
F 1 "74*05" H 6250 2600 60  0000 C CNN
F 2 "" H 6100 2750 60  0000 C CNN
F 3 "" H 6100 2750 60  0000 C CNN
	1    6100 2750
	1    0    0    -1  
$EndComp
$Comp
L 74HC14 IC?
U 1 1 54D404BB
P 2950 2050
F 0 "IC?" H 3000 2200 60  0000 L CNN
F 1 "74HC14" H 3000 1900 60  0000 L CNN
F 2 "" H 2950 2050 60  0000 C CNN
F 3 "" H 2950 2050 60  0000 C CNN
	1    2950 2050
	1    0    0    -1  
$EndComp
$Comp
L transistor_npn T?
U 1 1 54D56254
P 5350 3600
F 0 "T?" H 5250 3750 60  0000 C CNN
F 1 "transistor_npn" H 5250 3450 60  0000 C CNN
F 2 "" H 5350 3600 60  0000 C CNN
F 3 "" H 5350 3600 60  0000 C CNN
	1    5350 3600
	1    0    0    -1  
$EndComp
$Comp
L fet_n_channel T?
U 1 1 54D562AC
P 6200 3450
F 0 "T?" H 6100 3650 60  0000 C CNN
F 1 "fet_n_channel" H 5950 3250 60  0000 C CNN
F 2 "" H 6200 3450 60  0000 C CNN
F 3 "" H 6200 3450 60  0000 C CNN
	1    6200 3450
	1    0    0    -1  
$EndComp
$EndSCHEMATC
