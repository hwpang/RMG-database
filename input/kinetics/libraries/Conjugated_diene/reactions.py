#!/usr/bin/env python
# encoding: utf-8

name = "Conjugated_diene"
shortDesc = u"Conjugated diene reactions calculated at CBS-QB3"
longDesc = u"""
In conjunction with the Conjugated_diene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to conjugated diene dimerization and oligomerization.
Both calculations are done in CBS-QB3 level of theory using Gaussian 09.
Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed with frequency scale factor: 0.99
2. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
3. Hindered rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step, using B3LYP/CBSB7
4. All files generated were fed to Arkane.
5. Bond additivity correction was not used for the rate calculation.

Calculations done by Hao-Wei Pang and Duminda Ranasinghe. Library organized by Hao-Wei Pang.
"""

entry(
    index = 0,
    label = 'ISP + ISP <=> DISP4',
    kinetics = Arrhenius(
        A = (6.6251, 'cm^3/(mol*s)'),
        n = 2.52542,
        Ea = (86.3763, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Isoprene reactions calculated at CBS-QB3",
    longDesc = """Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019"""
)

entry(
    index = 1,
    label = 'ISP + ISP <=> DISP3',
    kinetics = Arrhenius(
        A = (6.69932, 'cm^3/(mol*s)'),
        n = 2.50029,
        Ea = (85.3903, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Isoprene reactions calculated at CBS-QB3",
    longDesc = """Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019"""
)

entry(
    index = 2,
    label = 'ISP + ISP <=> DISP2',
    kinetics = Arrhenius(
        A = (3.63093, 'cm^3/(mol*s)'),
        n = 2.51242,
        Ea = (89.5878, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Isoprene reactions calculated at CBS-QB3",
    longDesc = """Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019"""
)

entry(
    index = 3,
    label = 'ISP + ISP <=> DISP1',
    kinetics = Arrhenius(
        A = (7.00684, 'cm^3/(mol*s)'),
        n = 2.50593,
        Ea = (90.3462, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = "Isoprene reactions calculated at CBS-QB3",
    longDesc = """Isoprene reactions calculated at CBS-QB3 by Hao-Wei Pang in Oct 2019"""
)

entry(
index = 4,
label = "BD <=> CB",
kinetics = Arrhenius(A=(5.05558e+13,'s^-1'), n=-0.386712, Ea=(186.246,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.0933, dn = +|- 0.0124118, dEa = +|- 0.0456969 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 5,
label = "DVT <=> BD + BD",
kinetics = Arrhenius(A=(7.93464e+10,'s^-1'), n=0.515023, Ea=(60.1683,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.10306, dn = +|- 0.0136496, dEa = +|- 0.0502543 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 6,
label = "BD + BD <=> VCH",
kinetics = Arrhenius(A=(17556.2,'m^3/(mol*s)'), n=0, Ea=(95.853,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 171 data points; dA = *|/ 1.01483, dn = +|- 0, dEa = +|- 0.0941516 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 7,
label = "DVT <=> VCH",
kinetics = Arrhenius(A=(1.47047e+10,'s^-1'), n=0.235677, Ea=(5.14242,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.03099, dn = +|- 0.00424699, dEa = +|- 0.0156363 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 8,
label = "DVT <=> COD",
kinetics = Arrhenius(A=(1.00689e+10,'s^-1'), n=0.00215293, Ea=(22.4612,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.00636, dn = +|- 0.000882325, dEa = +|- 0.00324848 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 9,
label = "DVT <=> DVCB",
kinetics = Arrhenius(A=(3.21792e+10,'s^-1'), n=0.359974, Ea=(13.4572,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.05924, dn = +|- 0.00800783, dEa = +|- 0.0294826 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 10,
label = "DVCB <=> COD",
kinetics = Arrhenius(A=(7.59503e+10,'s^-1'), n=0.0992821, Ea=(104.188,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.04618, dn = +|- 0.00628203, dEa = +|- 0.0231287 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 11,
label = "BD + VCH <=> TRIN",
kinetics = Arrhenius(A=(0.839769,'m^3/(mol*s)'), n=1.15583, Ea=(108.915,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.03231, dn = +|- 0.00442451, dEa = +|- 0.0162898 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
index = 12,
label = "BD + VCH <=> TRIC",
kinetics = Arrhenius(A=(0.286588,'m^3/(mol*s)'), n=1.28193, Ea=(89.6631,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(1000,'K'), comment="""Fitted to 81 data points; dA = *|/ 1.03126, dn = +|- 0.0042835, dEa = +|- 0.0157707 kJ/mol"""),
longDesc = 
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: B3LYP/CBSB7 in vacuum (freq scale factor: 0.99)
SP: CBS-QB3 
"""
)

entry(
    index = 13,
    label = 'cyclopentadiene + cyclopentadiene <=> DICYCLOPENTADIENE',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.96068, 'cm^3/(mol*s)'),
        n = 2.71606,
        Ea = (60.1473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
        comment = 'Fitted to 161 data points; dA = *|/ 1.02799, dn = +|- 0.00384009, dEa = +|- 0.0142079 kJ/mol',
    ),
    shortDesc = u"""CBS-QB3 level calculation""",
    longDesc = """
    CBS-QB3 calculations related to cyclopentadiene polymerization reaction
    """
)

entry(
    index = 14,
    label = 'Bicyclopentyl-3-3-Diene <=> cyclopentadiene + cyclopentadiene',
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.98006e+08, 's^-1'),
        n = 1.10032,
        Ea = (30.078, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
        comment = 'Fitted to 161 data points; dA = *|/ 1.24176, dn = +|- 0.0301173, dEa = +|- 0.111431 kJ/mol',
    ),
    shortDesc = u"""CBS-QB3 level calculation""",
    longDesc = """
    CBS-QB3 calculations related to cyclopentadiene polymerization reaction
    """
)
