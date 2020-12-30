#!/usr/bin/env python
# encoding: utf-8

name = "6_membered_central_C-C_shift/training"
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
        A = (2.30946e+10, 's^-1'),
        n = 0.360276,
        Ea = (144.706, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: I <=> II
""",
)

entry(
    index = 1,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.06322e+11, 's^-1'),
        n = -0.0265989,
        Ea = (166.561, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P_reverse""",
    longDesc = 
u"""
Taken from entry: II <=> I
""",
)

entry(
    index = 2,
    label = "C10H10 <=> C10H10-2",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(2.214e+09, 's^-1'), n=0.749, Ea=(47.859, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W4
""",
)

entry(
    index = 3,
    label = "C10H10-2 <=> C10H10",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(3.213e+11, 's^-1'), n=0.07, Ea=(18.329, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W4 <=> W1
""",
)

entry(
    index = 4,
    label = "C10H10-3 <=> C10H10-4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(4.484e+11, 's^-1'), n=0.032, Ea=(50.631, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W2 <=> W3
""",
)

entry(
    index = 5,
    label = "C10H10-4 <=> C10H10-3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(3.626e+11, 's^-1'), n=0.119, Ea=(18.066, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W3 <=> W2
""",
)

entry(
    index = 6,
    label = "C10H14 <=> C10H14-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.75e+14,'1/s','+|-',6.66667e+12), n=0, Ea=(151.8,'kJ/mol','+|-',5.2), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: CPD-ISP_2 <=> CPD-ISP_3
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 12 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 7,
    label = "C8H12 <=> C8H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.59503e+10,'s^-1'), n=0.0992821, Ea=(104.188,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.04618, dn = +|- 0.00628203, dEa = +|- 0.0231287 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: DVCB <=> COD
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

