neutrons = 0


print("input atomic mass")
atomic_mass = int(input())
print("input atomic number")
atomic_number = int(input())
proton = atomic_number
electrons = atomic_number
neutrons = atomic_mass - atomic_number
print("element name")
element = input()
print("the element " + element + " has " + str(proton) + " proton(s)" + " and " + str(electrons) + " electron(s)")
print("and " + str(neutrons) + " neutrons")

# atomic number == protons
# atomic number == electrons
# nuetrons == atomic number - mass number

