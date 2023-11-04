import taipy as tp
from taipy import Config, Core, Gui
import pandas as pd


################################################################
#            Configure application                             #
################################################################
def build_message(name):
    return f"Hello {name}!"


# A first data node configuration to model an input name.
input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# A second data node configuration to model the message to display.
message_data_node_cfg = Config.configure_data_node(id="message")
file_data_node_cfg = Config.configure_csv_data_node(id="csv_node", exposed_type='numpy')

# A task configuration to model the build_message function.
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
# The scenario configuration represents the whole execution graph.
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

################################################################
#            Design graphical interface                        #
################################################################

input_name = "Taipy"
message = None
csv_node = None



def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()

def submit_homework(state):
    state.scenario.csv_node.write(state.csv_node)

x_range = range(1, 6)
data = {
    "X": x_range,
    "Y": [x*x for x in x_range]
}

column_orders = [("X;Y", "Squared"), ("Y;X", "Square root")]
columns = column_orders[0]

page = """
<|container container-styling|
<center>
Homework Queue 
</center>
|>

<|{data}|table|columns={columns[0]}|show_all|>
<|{columns}|toggle|lov={column_orders}|>



<center>
<|file_selector|label=Upload Homework|drop_message=Drop file here|hover_text=Click here to insert file|extensions=.csv|on_action=submit_homework|>
</center>






"""


Core().run()

    ################################################################
    #            Manage scenarios and data nodes                   #
    ################################################################
scenario = tp.create_scenario(scenario_cfg)

    ################################################################
    #            Instantiate and run Gui service                   #
    ################################################################

Gui(page).run()