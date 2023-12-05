import datetime
import time
from taipy import Gui
import pandas as pd
from prioritize import prioritize as pr


#File Settings
pd.set_option('display.max_columns', None)

#Variables
data = {
    "Assignment": ["Please Enter a "],
    "Priority": ["CSV File"]
}

saved_format = {
    "Assignment": ["Please Enter a "],
    "Priority": ["CSV File"]
}

loaded_data = None

time_comp = 0

path = None

dark_mode = "container-styling_dark"
light_mode = "container-styling_light"
calendar = "calendar.svg"
mode = dark_mode
logo = "container-styling_logo"

file_name = "Template"
content = "Homework Template.xlsx"
curr_date = datetime.datetime.now().strftime('%m/%d/%Y')
p_type = 1
w_type = "Grade"

#Functions
def load_csv_file(state):
    global loaded_data
    global time_comp
    global path

    local_data = pd.read_csv(state.path)
    loaded_data = pd.read_csv(state.path)
    start_time = time.time()
    local_data = pr(local_data, p_type)
    end_time = time.time()
    time_comp = end_time - start_time
    #time_comp = f"{time_comp} seconds"
    print(time_comp)
    data["Assignment"] = local_data.iloc[:, 0]
    data["Priority"] = local_data.iloc[:, -1]
    state.data = data
    state.time_comp = time_comp
    state.curr_date = datetime.datetime.now().strftime('%m/%d/%Y')
    path = None


def reload_csv_file(state):
    global loaded_data
    local_data = pr(loaded_data, p_type)
    data["Assignment"] = local_data.iloc[:, 0]
    data["Priority"] = local_data.iloc[:, -1]
    state.data = data

def what_type(priority_type):
    if priority_type == 1: return "Grade"
    elif priority_type == 2: return "Date"
    elif priority_type == 3: return "Difficulty"
def set_grade(state):
    global p_type
    global w_type
    p_type = 1
    state.w_type = what_type(p_type)

def set_date(state):
    global p_type
    global w_type
    p_type = 2
    state.w_type = what_type(p_type)

def set_difficulty(state):
    global p_type
    global w_type
    p_type = 3
    state.w_type = what_type(p_type)


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

<|container {logo}|
<|{calendar}|image|hover_text=Head Empty == True|width=100px|>
|>
<|Current Date: {curr_date}|button|>

<|toggle|theme|>

<|
<|container {mode}|
<center>
    Tai Your Life Together
</center>


|>
|>

<center>
    <|{data}|table|show_all|width=1000px|style=t1_kit|page_size=10|>
</center>

<center>
    <|Grade|button|hover_text=Grade|on_action=set_grade|>
    <|Date|button|hover_text=Date|on_action=set_date|>
    <|Difficulty|button|hover_text=Difficulty|on_action=set_difficulty|>
</center>

<center>
    <|Prioritizing by: {w_type}|button|hover_text=Prioritizing by: {w_type}|>
</center>

<center>
    <|{path}|file_selector|label=Upload Homework|on_action=load_csv_file|extensions=.csv|hover_text=Upload Homework|>
</center>

<center>
    <|{content}|file_download|label=Download Template|name={file_name}|bypass_preview=False|hover_text=Download Template|>
</center>

<center>
    <|Time: {time_comp}|button|>
</center>

"""

Gui(p1).run(stylekit=p1_kit, title="Tai Your Life Together")
