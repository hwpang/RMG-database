#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C4H6 + C2H4 <=> C6H10",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""default""",
    longDesc = 
u"""
Converted to training reaction from rate rule: diene_out;diene_in;ene
""",
)

entry(
    index = 2,
    label = "C4H6-2 + C4H6 <=> C8H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.91e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (102.257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (464, 'K'),
        Tmax = (557, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_2H_HDe
""",
)

entry(
    index = 3,
    label = "C4H6-3 + C4H6 <=> C8H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.91e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (102.257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (464, 'K'),
        Tmax = (557, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HDe_2H
""",
)

entry(
    index = 4,
    label = "C5H8 + C4H6 <=> C9H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.798e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (92.299, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (515, 'K'),
        Tmax = (572, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HNd_HDe
""",
)

entry(
    index = 5,
    label = "C5H8-2 + C4H6 <=> C9H14-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.798e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (92.299, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (515, 'K'),
        Tmax = (572, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HDe_HNd
""",
)

entry(
    index = 6,
    label = "C5H8-3 + C2H4 <=> C7H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (123.888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1180, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_HNd;ene_unsub_unsub
""",
)

entry(
    index = 7,
    label = "C2H4 + C5H8-4 <=> C7H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (123.888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1180, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_NdH;ene_unsub_unsub
""",
)

entry(
    index = 8,
    label = "C4H6-3 + C5H8-3 <=> C9H14-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (78.2408, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (492, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_HNd;ene_HDe_2H
""",
)

entry(
    index = 9,
    label = "C4H6-2 + C5H8-4 <=> C9H14-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (78.2408, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (492, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_NdH;ene_2H_HDe
""",
)

entry(
    index = 10,
    label = "C2H4 + C6H10-2 <=> C8H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.14e+09, 'cm^3/(mol*s)', '*|/', 1.05),
        n = 0,
        Ea = (108.91, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (450, 'K'),
        Tmax = (592, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Huybrechts et al. [109]""",
    longDesc = 
u"""
[109] Huybrechts, G.; Rigaux, D.; Vankeerberghen, J.; Van Mele, B. Int. J. Chem. Kinet. 1980, 12, 253.
1,3-cyclohexadiene + C2H4 --> bicyclo[2.2.2]oct-2-ene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.05-0.25 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_unsub_unsub
""",
)

entry(
    index = 11,
    label = "C3H6 + C6H10-2 <=> C9H16",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.24e+09, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        Ea = (111.42, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd
""",
)

entry(
    index = 12,
    label = "C3H6-2 + C6H10-2 <=> C9H16-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.24e+09, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        Ea = (111.42, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_2H
""",
)

entry(
    index = 13,
    label = "C4H6-2 + C6H10-2 <=> C10H16",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4.08e+09, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        Ea = (83.9729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (379, 'K'),
        Tmax = (581, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe
""",
)

entry(
    index = 14,
    label = "C4H6-3 + C6H10-2 <=> C10H16-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4.08e+09, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        Ea = (83.9729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (379, 'K'),
        Tmax = (581, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_2H
""",
)

entry(
    index = 15,
    label = "C5H8 + C6H10-2 <=> C11H18",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.52e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (69.831, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (352, 'K'),
        Tmax = (423, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_HDe
""",
)

entry(
    index = 16,
    label = "C5H8-2 + C6H10-2 <=> C11H18-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.52e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (69.831, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (352, 'K'),
        Tmax = (423, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_HNd
""",
)

entry(
    index = 17,
    label = "C7H10 + C4H8 <=> C11H18-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.1622, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (103.554, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: diene_5ring_Nd_Nd_out;diene_in_2H;ene_HNd_HNd
""",
)

entry(
    index = 18,
    label = "C3H4 + C4H6 <=> C7H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.244, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (117.57, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7 HO, butadiene + propyne""",
    longDesc = 
u"""
Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;yne_unsub_monosub
""",
)

entry(
    index = 19,
    label = "C3H4-2 + C4H6 <=> C7H10-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.708, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (121.336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7 HO, butadiene + allene""",
    longDesc = 
u"""
Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;allene_unsub
""",
)

entry(
    index = 20,
    label = "C5H8-5 + C5H8-4 <=> C10H16-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.16667e+10,'cm^3/(mol*s)','+|-',2.16667e+09), n=0, Ea=(109.7,'kJ/mol','+|-',3.7), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: ISP + ISP <=> DISP_2
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 5 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 21,
    label = "C5H8-6 + C5H8-4 <=> C10H16-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.23333e+08,'cm^3/(mol*s)','+|-',1e+07), n=0, Ea=(90.3,'kJ/mol','+|-',1.4), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: ISP + ISP <=> DISP_3
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 6 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 22,
    label = "C5H8-4 + C5H6 <=> C10H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.46667e+07,'cm^3/(mol*s)','+|-',3e+06), n=0, Ea=(77.9,'kJ/mol','+|-',2), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: CPD + ISP <=> CPD-ISP_3
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 11 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 23,
    label = "C5H8 + C5H8-7 <=> C10H16-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.3e+09,'cm^3/(mol*s)','+|-',2.33333e+08), n=0, Ea=(108.2,'kJ/mol','+|-',2.9), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: tP + tP <=> DtP_2
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 16 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 24,
    label = "C5H8-8 + C5H8-7 <=> C10H16-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34833e+08,'cm^3/(mol*s)','+|-',3.5e+06), n=0, Ea=(89.6,'kJ/mol','+|-',1.4), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: tP +tP <=> DtP_6
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 20 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 25,
    label = "C5H8-7 + C5H6 <=> C10H14-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.63333e+08,'cm^3/(mol*s)','+|-',7.83333e+07), n=0, Ea=(96.1,'kJ/mol','+|-',5.9), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: CPD + tP <=> CPD-tP_5
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 26 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 26,
    label = "C5H8-7 + C5H6-2 <=> C10H14-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.1e+09,'cm^3/(mol*s)','+|-',1.83333e+08), n=0, Ea=(93.3,'kJ/mol','+|-',2.8), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: CPD + tP <=> CPD-tP_6
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 27 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 27,
    label = "C5H6-3 + C5H10 <=> C10H16-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.93333e+08,'cm^3/(mol*s)','+|-',2.16667e+07), n=0, Ea=(96.5,'kJ/mol','+|-',4.1), T0=(1,'K')),
    rank = 3,
    shortDesc = """Obtained from experimental data by Xu et al.""",
    longDesc = 
"""
Training reaction from kinetics library: Xu_cyclopentadiene
Original entry: CPD + t2P <=> CPD-t2P_1
Kinetic parameters for reactions among C5 compounds
were obtained from regression analysis of experimental
reaction data from Xu et al. Table 1 entry 30 in DOI: 10.1021/acs.iecr.9b04018
Ind. Eng. Chem. Res. 2019, 58, 22516−22525
""",
)

entry(
    index = 28,
    label = "C5H8-6 + C5H8-4 <=> C10H16-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.69932,'cm^3/(mol*s)'), n=2.50029, Ea=(85.3903,'kJ/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """Isoprene reactions calculated at CBS-QB3""",
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: ISP + ISP <=> DISP3
Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019
""",
)

entry(
    index = 29,
    label = "C5H8-5 + C5H8-4 <=> C10H16-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.63093,'cm^3/(mol*s)'), n=2.51242, Ea=(89.5878,'kJ/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """Isoprene reactions calculated at CBS-QB3""",
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: ISP + ISP <=> DISP2
Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019
""",
)

entry(
    index = 30,
    label = "C4H6 + C8H12-3 <=> C12H18",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(839769,'cm^3/(mol*s)'), n=1.15583, Ea=(108.915,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.03231, dn = +|- 0.00442451, dEa = +|- 0.0162898 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: BD + VCH <=> TRIN
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

