
name = "2+2_cycloaddition/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["db"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "db",
    group = 
"""
1 *1 [Cd,Cdd,CO,CS]         u0 {2,D}
2 *2 [Cd,Cdd,CO,CS,O2d,S2d] u0 {1,D}
3 *3 [Cd,Cdd,CO,CS,O2d,S2d] u0 {4,D}
4 *4 [Cdd,CO,CS]            u0 {3,D}
""",
    kinetics = None,
)