# get the total and average of all series A rounds (TechCrunch Continental USA Set)
# strategy
# 1. read every line of the file
# 2. split each line into a list of values
# 3. extract the column names
# 4. use the column names and list to create a dictionary
# 5. filter out rounds we are not interested in
# 6. calculate total and average values of rounds we are interested in

from pathlib import Path

# step 0: load file
file = Path(__file__).parent / "assets" / "techcrunch.csv"

# step 1
lines = (line for line in open(file))

# step 2
list_line = (s.rstrip().split(",") for s in lines)

# step 3
cols = next(list_line)

# step 4
company_dicts = (dict(zip(cols, data)) for data in list_line)

# step 5
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

# step 6
total_series_a = sum(funding)
print(f"Total Series A funding: ${total_series_a}")

# average per company, im stuck
