count = {}

Names = ["venky", "venky", "sailu", "ashish", "venky", "ashish"]

for name in Names :
    count[name] = count.get(name, 0) + 1


print(count)

### OUTPUT
{'venky': 3, 'sailu': 1, 'ashish': 2}
###
