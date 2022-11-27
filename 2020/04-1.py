with open("04.txt") as fp:
    print(len([vp for vp in [{k: v for k, v in [e.split(":") for e in p.strip().split(" ")]} for p in fp.read().replace("\n\n", ",").replace("\n", " ").split(",")] if all(mk in vp.keys() for mk in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])]))
