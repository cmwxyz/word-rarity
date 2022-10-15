import pandas as pd
from os.path import dirname, abspath

src_dir = f"{abspath(dirname(__file__))}"
word_df = pd.read_csv(f"{src_dir}/word_rarity_list.csv")
dict_size = word_df["word"].size
