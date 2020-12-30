#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C8H12 <=> C4H6 + C4H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.93464e+10,'s^-1'), n=0.515023, Ea=(60.1683,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.10306, dn = +|- 0.0136496, dEa = +|- 0.0502543 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: DVT <=> BD + BD
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

entry(
    index = 2,
    label = "C10H12 <=> C5H6 + C5H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.98006e+08,'s^-1'), n=1.10032, Ea=(30.078,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 161 data points; dA = *|/ 1.24176, dn = +|- 0.0301173, dEa = +|- 0.111431 kJ/mol"""),
    rank = 3,
    shortDesc = """CBS-QB3 level calculation""",
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: Bicyclopentyl-3-3-Diene <=> cyclopentadiene + cyclopentadiene
CBS-QB3 calculations related to cyclopentadiene polymerization reaction
""",
)

