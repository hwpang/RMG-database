#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C8H12 <=> C8H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0,
        Ea = (7.5312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (550, 'K'),
        Tmax = (650, 'K'),
    ),
    rank = 10,
    shortDesc = u"""[186] Benson et al.""",
    longDesc = 
u"""
[186] Benson, S.W. J. Chem. Phys. 1967, 46, 4920.

CH2=CHCH(.)CH2CH2CH(.)CH=CH2 --> 4-vinylcyclohexene. (Rxn. -c); arises from birad recombination of resonance isomer: .CH2CH=CHCH2CH2CH(.)CH=CH2

Data are estimated.

***this only considers cis-cis isomer reaction*** cis-trans A prefactor is 50% of the value used here; also, on p. 4923, it is stated that cis trans rate is 5/6 of the overall rate, so maybe the k that should be used is 0.6 of the value currently in place?
Verified by Greg Magoon: Rxn. -d. also looks to be of interest here; whether the rate is high-pressure limit was not investigated, but p. 4922 says that pressures involved were low; DE0 uncertainty added; regarding temperature range, I considered dropping lower temperature limit from 550 K to 400 K (based on p. 4923), but it seems that experiments were performed at or around 600 K, so I will leave it at 550-650 K

Note: after some preliminary confusion on my part, it looks like the existing groups are correct (the correct resonance form for the CH2 radical is taken into account with the Ypri_rad_out (i.e. Cpri_rad_out_H2)), but arguably, another, a more-specific group (C_rad_out_H2/OneDe and Cpri_rad_out_H2/OneDe) should be specified to account for delocalizing group at this site

Converted to training reaction from rate rule: R6_SSSDS;C_rad_out_H/OneDe;Cpri_rad_out_2H
""",
)

entry(
    index = 2,
    label = "C4H8 <=> C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.62e+12, 's^-1'),
        n = -0.305,
        Ea = (8.28432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2. -> cyclopentane (k4-1 in Scheme 5/Table 7)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant

Converted to training reaction from rate rule: R4_SSS;C_rad_out_2H;Cpri_rad_out_2H
""",
)

entry(
    index = 3,
    label = "C5H10 <=> C5H10-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.76e+09, 's^-1'),
        n = 0.311,
        Ea = (7.1128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2CH2. -> cyclohexane (k5-1+k5-2 in Scheme 7/Table 10) (includes formation of both boat and chair conformations)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant; the rate constant added here was found my performing least squares fit for log(ktot) from 600-2000 K (where ktot is the sum of k5-1 and k5-2)

Note: Recent experimental/RRKM study by Kiefer, Gupte, Harding, and Klippenstein (http://www.combustion.org.uk/ECM_2009/P810069.pdf) (stated uncertainty is +/- 30%) appears to agree with Sirjean et al. results, but they only report forward rate constant

Converted to training reaction from rate rule: R5_SSSS;C_rad_out_2H;Cpri_rad_out_2H
""",
)

entry(
    index = 4,
    label = "C6H12 <=> C6H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.21e+10, 's^-1'),
        n = 0.137,
        Ea = (8.87008, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6_SSSSS;C_rad_out_2H;Cpri_rad_out_2H
""",
)

entry(
    index = 5,
    label = "CH2S2 <=> CH2S2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.18e+16, 's^-1'),
        n = 0,
        Ea = (2.9288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3_SS;S_rad;Spri_rad
""",
)

entry(
    index = 6,
    label = "C8H12 <=> C8H12-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.47047e+10,'s^-1'), n=0.235677, Ea=(5.14242,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.03099, dn = +|- 0.00424699, dEa = +|- 0.0156363 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: DVT <=> VCH
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

entry(
    index = 7,
    label = "C8H12-3 <=> C8H12-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.00689e+10,'s^-1'), n=0.00215293, Ea=(22.4612,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.00636, dn = +|- 0.000882325, dEa = +|- 0.00324848 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: DVT <=> COD
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

entry(
    index = 8,
    label = "C8H12-5 <=> C8H12-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.21792e+10,'s^-1'), n=0.359974, Ea=(13.4572,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.05924, dn = +|- 0.00800783, dEa = +|- 0.0294826 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Conjugated_diene
Original entry: DVT <=> DVCB
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3
""",
)

