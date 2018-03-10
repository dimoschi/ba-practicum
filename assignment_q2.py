import os
import pandas as pd

# Load data
sumdf = pd.read_csv(os.path.join(os.getcwd(), "input", "gombe_128.csv"))

# Sub-question A
neuroticism_mean = sumdf.neuroticism.mean()
neuroticism_median = sumdf.neuroticism.median()

# Sub-question B
# Match chimpcodes with 3 or more numbers and with ~ flip True/False
sumdf2d = sumdf[~sumdf.chimpcode.str.contains(r"\d{3}")]
print("There are {} chimpanzees with 2 digits in chimpcode.".format(
    sumdf2d.chimpcode.count()
))

# Sub-question C
sumdf_S_even = sumdf[sumdf.chimpcode.str.contains(r"[A-R].*\d*[02468]$")]
print((
      "There are {} chimpanzees, whose chimpcode starts with S "
      "and numbers are all even."
      ).format(sumdf_S_even.chimpcode.count())
)

# Sub-question D
print("The score_difference is {}".format(
        sumdf.decs.mean() - sumdf.conv.mean()
))

# Sub-question E
# First keep the required columns, then groupby sex and sum each column.
# Using idxmax we keep the columns with the maximum values and lastly to_dict
# function creates a dictionary
sumdf[[
    "sex", "dominance", "extraversion", "conscientiousness",
    "agreeableness", "neuroticism", "openness"
]].groupby(["sex"]).sum().idxmax(axis=1).to_dict()


# Sub-question F
# First keep only the required columns, then find the max for each row. This
# creates a Series with the highest value column on each row. Using
# value_counts the traits are being grouped and counted and lastly to_dict
# function is being used to create the dictionary
sumdf.iloc[:, 3:27].idxmax(axis=1).value_counts().to_dict()


# Sub-question G


# Sub-question H