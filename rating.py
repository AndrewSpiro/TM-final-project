import pandas as pd

data = pd.read_csv("data/annotation.csv")
data = data.astype(str)

anno = input("Annotator 1 or 2? ")
anno = "label" + str(anno)

for index in range(len(data)):
    # print(data.loc[index, anno])

    if data.loc[index, anno] == "nan":
        summary = data.loc[index, "summary"]
        print(summary)

        label = input("Is this note biased (1) or unbiased (0)? ")

        if label in ["0", "1"]:
            data.loc[index, anno] = str(label)

            data.to_csv("data/annotation.csv",
                        columns=["noteId", "status", "summary", "label1", "label2"])
