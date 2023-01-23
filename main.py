import deepdiff
import json 

with open("1.json") as f1, open("2.json") as f2:
    file1 = json.load(f1)
    file2 = json.load(f2)

patch = deepdiff.DeepDiff(file1, file2, ignore_order=True, report_repetition=True)

with open("patch.json", "w") as f:
    json.dump(patch, f, indent=2)

delta = deepdiff.Delta(patch)

with open("final-data.json") as f:
    data = json.load(f)

data = data+delta

with open("final-data.json", "w") as f:
    json.dump(data, f, indent=2)