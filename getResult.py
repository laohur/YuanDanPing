import os
import json

corpus = "wikinews"
corpus = "UN_meeting_records"
corpus = "chinaxiv"
tags = set()
store = {}
# months = ["2024-01", "2024-02"][:]
months = ["2023", "2024"][:]
params = {}
for train in ["eval", "lora"]:
    for month in months:
        output_folder = f"./output/{corpus}/outputs-{train}/{month}"
        if not os.path.exists(output_folder):
            continue
        ppls = []
        names = sorted(os.listdir(output_folder))
        tag = f"{train}#{month}"
        tags.add(tag)
        for name in names:
            src = f"{output_folder}/{name}/eval_results.json"
            try:
                J = json.load(open(src))
                # print(src,J)
                ppl = J["perplexity"]
                loss = J["eval_loss"]
                params[name] = J["all_param"]
            except:
                ppl = -1
            # ppls.append(ppl)
            if name not in store:
                store[name] = {}
            store[name][tag] = ppl
            print(name, tag, ppl)

tags = sorted(list(tags))
head = ["model", "params"] + tags
doc = [head]
names = list(params.keys())
names.sort(key=lambda x: x.lower())

for name in names:
    R = store[name]
    row = [name, params[name]] + [R.get(tag, -2) for tag in tags]
    doc.append(row)

with open(f"result/{corpus}.tsv", "w") as f:
    for row in doc:
        l = "\t".join(str(x) for x in row)
        f.write(l + "\n")

