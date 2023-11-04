import taipy as tp
from taipy import Config, Core, Gui
import pandas as pd






path = None
md = "<|{path}|file_selector|label=Upload dataset|on_action=load_csv_file|extensions=.csv|>"

def load_csv_file(state):
    data = pd.read_csv(state.path)
    print(data)

Gui(md).run()