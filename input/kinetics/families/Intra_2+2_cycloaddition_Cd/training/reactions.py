#!/usr/bin/env python
# encoding: utf-8

name = "Intra_2+2_cycloaddition_Cd/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.99998e+11, 's^-1'),
        n = 0.0559095,
        Ea = (122.413, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: II <=> III
""",
)

entry(
    index = 1,
    label = "C4H6 <=> C4H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.05558e+13,'s^-1'), n=-0.386712, Ea=(186.246,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.0933, dn = +|- 0.0124118, dEa = +|- 0.0456969 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: BD <=> CB
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

