import time

import taipy as tp
from taipy import Config, Core, Gui
import pandas as pd
from prioritize import prioritize as pr


#File Settings
pd.set_option('display.max_columns', None)

#Variables
data = {
    "Assignment": ["Please Enter a "],
    "Priority": ["CSV File"]
}
time_comp = 0

#columns = "Assignment;Priority",
path = None

dark_mode = "container-styling_dark"
light_mode = "container-styling_light"
mode = dark_mode

file_name = "Template"
content = "Homework Template.xlsx"

#Functions
def load_csv_file(state):
    local_data = pd.read_csv(state.path)
    start_time = time.time()
    local_data = pr(local_data)
    end_time = time.time()
    global time_comp
    time_comp = end_time - start_time
    time_comp = f"{time_comp} seconds"
    print(time_comp)
    data["Assignment"] = local_data.iloc[:, 0]
    data["Priority"] = local_data.iloc[:, -1]
    state.data = data

#CSS Styling
p1_kit = {
    "color_primary": "#1B4965",
    "color_secondary": "#BEE9E8",
    "color_background_dark": "#102a43",
    "color_background_light": "#ffffff",
    "font-family": "Comfortaa, sans-serif",
}

t1_kit = {
    "font-family": "Comfortaa, sans-serif",
    "border-radius": "20px",
    "color_background_light": "#9bd4e4",
    "text-align": "center",
}

#HTML Style Webpage
p1 = """
<|toggle|theme|>

<|container {mode}|
<center>
    Tai Your Life Together
</center>
|>

<center>
    <|{data}|table|show_all|width=1000px|style=t1_kit|page_size=10|>
</center>

<center>
    <|Grade|button|hover_text=Grade|>
    <|Date|button|hover_text=Date|>
    <|Difficulty|button|hover_text=Difficulty|>
</center>

<center>
    <|{path}|file_selector|label=Upload Homework|on_action=load_csv_file|extensions=.csv|hover_text=Upload Homework|>
</center>

<center>
    <|{content}|file_download|label=Download Template|name={file_name}|bypass_preview=False|hover_text=Download Template|>
</center>
"""

Gui(p1).run(stylekit=p1_kit, title="Tai your Life Together")
