from pyparsing import Word, alphas

rules = []

with open('07-test.txt') as fp:
    for rule in fp:
        rules.append(rule.strip())

print(rules)
