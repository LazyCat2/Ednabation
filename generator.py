import os, json, random

dataset = json.load(open(f"dataset/{len(os.listdir('dataset'))}.json"))
keys = dataset.keys()

def generate(start):
	if start: start=start.lower()
	k = start if start in keys else random.choice(list(keys))
	text = k
	
	for x in range(50):
		random.shuffle(dataset[k])
		nk = None
		for i in dataset[k]:
			if i in dataset:
				nk = i
				break
		if not nk:
			nk = random.choice(list(keys))
		text += " " + nk
		k = nk
	
	return text
