import pandas as pd

df=pd.DataFrame([
    ["전동윤","1994.02.15","2022-0001"],
    ["이희연","1993-06-05","2022-0002"],
    ["채희천","1993-12-24","2022-0004"]
    ])

print(df)

df.to_excel(r'Chapter4\main12\certificate.xlsx', index=False, header=False)