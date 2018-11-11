EESchema Schematic File Version 4
LIBS:test2-cache
EELAYER 26 0
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
L mcu_atmel:ATSAMD10C13A-SSU IC1
U 3 1 5BE62716
P 2700 3300
F 0 "IC1" H 2949 3456 60  0000 L CNN
F 1 "ATSAMD10C13A-SSU" H 2949 3350 60  0000 L CNN
F 2 "soic:soic_14_wide" H 2500 2650 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/mcu/atmel/SAMD10.pdf" H 2500 2550 60  0001 L CNN
F 4 "Atmel" H 2949 3244 60  0000 L CNN "Manufacturer"
	3    2700 3300
	1    0    0    -1  
$EndComp
$Comp
L driver:MAX232ACPE+ IC2
U 1 1 5BE6E651
P 2850 1550
F 0 "IC2" H 2850 2450 60  0000 C CNN
F 1 "MAX232ACPE+" H 2850 2344 60  0000 C CNN
F 2 "dip:dip_16" H 3050 900 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/driver/maxim/MAX220_249.pdf" H 3050 800 60  0001 L CNN
	1    2850 1550
	1    0    0    -1  
$EndComp
$Comp
L connector_phoenix_contact:MKDSO_2.5_4_L_KMGY CON1
U 1 1 5BE8C365
P 7200 2150
F 0 "CON1" H 7435 2306 60  0000 L CNN
F 1 "MKDSO_2.5_4_L_KMGY" H 7435 2200 60  0000 L CNN
F 2 "connector_phoenix_contact:MKDSO_2.5_4_L_KMGY" H 7000 1800 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/connector_phoenix_contact/00556587_MKDSO_2.5_4-L.pdf" H 7000 1700 60  0001 L CNN
F 4 "Phoenix Contact" H 7435 2094 60  0000 L CNN "Manufacturer"
	1    7200 2150
	1    0    0    -1  
$EndComp
$Comp
L connector_phoenix_contact:MKDSO_2.5_4_L_KMGY CON2
U 1 1 5BE8D061
P 7200 2700
F 0 "CON2" H 7435 2856 60  0000 L CNN
F 1 "MKDSO_2.5_4_L_KMGY" H 7435 2750 60  0000 L CNN
F 2 "connector_phoenix_contact:MKDSO_2.5_4_L_KMGY" H 7000 2350 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/connector_phoenix_contact/00556587_MKDSO_2.5_4-L.pdf" H 7000 2250 60  0001 L CNN
F 4 "Phoenix Contact" H 7435 2644 60  0000 L CNN "Manufacturer"
	1    7200 2700
	1    0    0    -1  
$EndComp
$Comp
L connector_phoenix_contact:MKDSO_2.5_4_R_KMGY CON3
U 1 1 5BE8D12E
P 7200 3250
F 0 "CON3" H 7435 3406 60  0000 L CNN
F 1 "MKDSO_2.5_4_R_KMGY" H 7435 3300 60  0000 L CNN
F 2 "connector_phoenix_contact:MKDSO_2.5_4_R_KMGY" H 7000 2900 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/connector_phoenix_contact/00814578_MKDSO_2.5_4-R.pdf" H 7000 2800 60  0001 L CNN
F 4 "Phoenix Contact" H 7435 3194 60  0000 L CNN "Manufacturer"
	1    7200 3250
	1    0    0    -1  
$EndComp
$Comp
L connector_phoenix_contact:MKDSO_2.5_4_R_KMGY CON4
U 1 1 5BE8D1BD
P 7200 3800
F 0 "CON4" H 7435 3956 60  0000 L CNN
F 1 "MKDSO_2.5_4_R_KMGY" H 7435 3850 60  0000 L CNN
F 2 "connector_phoenix_contact:MKDSO_2.5_4_R_KMGY" H 7000 3450 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/connector_phoenix_contact/00814578_MKDSO_2.5_4-R.pdf" H 7000 3350 60  0001 L CNN
F 4 "Phoenix Contact" H 7435 3744 60  0000 L CNN "Manufacturer"
	1    7200 3800
	1    0    0    -1  
$EndComp
$Comp
L mechanic_phoenix_contact:ME_LPZS_LEFT CON5
U 1 1 5BE8D4A1
P 9150 2150
F 0 "CON5" H 9385 2306 60  0000 L CNN
F 1 "ME_LPZS_LEFT" H 9385 2200 60  0000 L CNN
F 2 "mechanic_phoenix_contact:ME_LPZS_LEFT" H 8950 1800 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/mechanic_phoenix_contact/ME_LPZS_00837054.pdf" H 8950 1700 60  0001 L CNN
F 4 "Phoenix Contact" H 9385 2094 60  0000 L CNN "Manufacturer"
	1    9150 2150
	1    0    0    -1  
$EndComp
$Comp
L mechanic_phoenix_contact:ME_LPZS_RIGHT CON6
U 1 1 5BE8D5C2
P 9150 2700
F 0 "CON6" H 9385 2856 60  0000 L CNN
F 1 "ME_LPZS_RIGHT" H 9385 2750 60  0000 L CNN
F 2 "mechanic_phoenix_contact:ME_LPZS_RIGHT" H 8950 2350 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/mechanic_phoenix_contact/ME_LPZS_00837054.pdf" H 8950 2250 60  0001 L CNN
F 4 "Phoenix Contact" H 9385 2644 60  0000 L CNN "Manufacturer"
	1    9150 2700
	1    0    0    -1  
$EndComp
$Comp
L connector_phoenix_contact:PHOENIX_CONTACT_ME_TBUS CON7
U 1 1 5BE8C116
P 1400 1650
F 0 "CON7" H 1347 1050 60  0000 C CNN
F 1 "PHOENIX_CONTACT_ME_TBUS" H 1347 1156 60  0000 C CNN
F 2 "connector_phoenix_contact:PHOENIX_CONTACT_ME_TBUS" H 1200 1200 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/connector_phoenix_contact/00786807_02.pdf" H 1200 1100 60  0001 L CNN
F 4 "Phoenix Contact" H 1347 1262 60  0000 C CNN "Manufacturer"
	1    1400 1650
	-1   0    0    1   
$EndComp
$Comp
L mcu_atmel:ATSAMD10C13A-SSU IC1
U 2 1 5BE8CA8A
P 5100 2950
F 0 "IC1" H 5349 3106 60  0000 L CNN
F 1 "ATSAMD10C13A-SSU" H 5349 3000 60  0000 L CNN
F 2 "soic:soic_14_wide" H 4900 2300 60  0001 L CNN
F 3 "${KICAD_DOCUMENT_DIR}/mcu/atmel/SAMD10.pdf" H 4900 2200 60  0001 L CNN
F 4 "Atmel" H 5349 2894 60  0000 L CNN "Manufacturer"
	2    5100 2950
	-1   0    0    1   
$EndComp
$Comp
L supply:GND #PWR02
U 1 1 5BE8D047
P 2850 2200
F 0 "#PWR02" H 2850 2250 60  0001 C CNN
F 1 "GND" H 2850 2020 60  0000 C CNN
F 2 "" H 2850 2200 50  0001 C CNN
F 3 "" H 2850 2200 50  0001 C CNN
	1    2850 2200
	1    0    0    -1  
$EndComp
$Comp
L supply:+3V3 #PWR01
U 1 1 5BE8D0CA
P 2850 800
F 0 "#PWR01" H 2850 725 60  0001 C CNN
F 1 "+3V3" H 2850 1081 60  0000 C CNN
F 2 "" H 2850 800 50  0001 C CNN
F 3 "" H 2850 800 50  0001 C CNN
	1    2850 800 
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 850  2850 800 
Wire Wire Line
	2850 2150 2850 2200
Wire Wire Line
	1700 1950 2150 1950
Wire Wire Line
	2150 1950 2150 1650
Wire Wire Line
	2150 1650 2550 1650
Wire Wire Line
	2550 1850 1700 1850
$EndSCHEMATC
