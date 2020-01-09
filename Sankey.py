#Snakey Expenses Diagram

import datetime
import pandas as pd
import numpy as np

# viz
import plotly.graph_objects as go
from plotly.offline import plot, iplot

# prints the present date and time as a form of log
print("This notebook was last run: ", datetime.datetime.now())

basedata = pd.read_csv(filepath_or_buffer = "C:/Users/FIY716/Documents/PythonScripts/expenses.csv")

category_columns = ['lvl_1_level', 'lvl_2_level', 'lvl_3_level']

value_column = 'dollar_value'

label_list = []
# iterate over all categories to get an exhaustive list of categories
for category in category_columns:
# temporarily stores, for each lvl of labels, the labels in that column
    label_list_temp = list(set(basedata[category].values))
    #Create the final list of all labels across all categories
    label_list = label_list + label_list_temp
label_list

# transform our base df into a source-target pair...
# which is the required data format for the plotly sankey to consume...
# iterate over all categories to log all source-target pair combinations, along with corresponding values
for i in range(len(category_columns)-1):
    if i==0:
        source_target_df = basedata[[category_columns[i],category_columns[i+1],value_column]]
        source_target_df.columns = ['source','target','count']
    else:
        temp_df = basedata[[category_columns[i],category_columns[i+1],value_column]]
        temp_df.columns = ['source','target','count']
        source_target_df = pd.concat([source_target_df,temp_df])

# cleans up the df and drops duplicative pairs / values     
source_target_df = source_target_df.groupby(['source','target']).agg({'count':'sum'}).reset_index()

source_target_df


# add indexes for source-target pairs...
# this will be needed later when building the plotly figure
source_target_df['source_id'] = source_target_df['source'].apply(lambda x: label_list.index(x))
source_target_df['target_id'] = source_target_df['target'].apply(lambda x: label_list.index(x))

source_target_df

# turning the label list into a df so we can more easily color-code each label manually
label_name_and_color_df = pd.DataFrame(label_list, columns = ['label'])

label_name_and_color_df

label_color_conditions = [
    (label_name_and_color_df['label'] == 'Gross Monthly Pay'),
    (label_name_and_color_df['label'] == 'Pre-Tax Deductions'),
    (label_name_and_color_df['label'] == 'Net Pay'),
    (label_name_and_color_df['label'] == 'Taxes'),
    (label_name_and_color_df['label'] == 'Car Payment'),
    (label_name_and_color_df['label'] == 'Medicare + Social Security'),
    (label_name_and_color_df['label'] == '401k'),
    (label_name_and_color_df['label'] == 'Federal Witholding'),
    (label_name_and_color_df['label'] == 'State Tax - VA'),
    (label_name_and_color_df['label'] == 'Vision'),
    (label_name_and_color_df['label'] == 'Dental'),
    (label_name_and_color_df['label'] == 'Net Pay'),
    (label_name_and_color_df['label'] == 'Medical'),
    (label_name_and_color_df['label'] == 'Dry Cleaning'),
    (label_name_and_color_df['label'] == 'Youtube TV'),
    (label_name_and_color_df['label'] == 'Acorns'),
    (label_name_and_color_df['label'] == 'Rent'),
    (label_name_and_color_df['label'] == 'Entertainment'),
    (label_name_and_color_df['label'] == 'Groceries'),
    (label_name_and_color_df['label'] == 'Spotify'),
    (label_name_and_color_df['label'] == 'Shopping'),
    (label_name_and_color_df['label'] == 'Haircut'),
    (label_name_and_color_df['label'] == 'Wealthfront'),              
    (label_name_and_color_df['label'] == 'Metro/Gas')
]

# list of colors to assign if each of the corresponding conditions above == TRUE
label_color_choices = [
    '#2933FC', # blue 
    '#FD7523', # orange
    '#FD7523', # orange
    '#23FB64', # green
    '#FC2C29', # red
    '#FD7523', # orange
    '#FC2C29', # red
    '#FD7523', # orange
    '#FC2C29', # red
    '#FC2C29', # red
    '#B31EFD', # purple
    '#B31EFD', # purple
    '#23FB64', # green
    '#B31EFD', # purple
    '#FC2C29', # red
    '#FC2C29', # red
    '#B31EFD', # purple
    '#B31EFD', # purple
    '#23FB64', # green
    '#B31EFD', # purple
    '#FD7523', # orange
    '#FC2C29', # red
    '#FD7523', # orange
    '#FC2C29', # red
]

len(label_color_choices)
len(label_color_conditions)
# create a new column -- color -- based on conditions and choices set out above...
# default to black if no conditional logic provided
label_name_and_color_df['color'] = np.select(label_color_conditions, label_color_choices, default='#000000')

# and now we repeat this process again, but this time adding the english names of the colors...
# this isn't necessary for the figure to be created; I just do it to make the ultimate df easier to read
label_color_name_conditions = [
    label_name_and_color_df['color'] == '#2933FC',
    label_name_and_color_df['color'] == '#FD7523',
    label_name_and_color_df['color'] == '#23FB64',
    label_name_and_color_df['color'] == '#FC2C29',
    label_name_and_color_df['color'] == '#B31EFD',
    
]
label_color_name_choices = [
    'blue',
    'orange',
    'green',
    'red',
    'purple'
]

# adding color names to the final df (for readability and convenience only)
label_name_and_color_df['color_name'] = np.select(label_color_name_conditions, label_color_name_choices, default='black')

label_name_and_color_df

link_color_conditions = [
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Acorns')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Car Payment')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Dry Cleaning')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Entertainment')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Groceries')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Haircut')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Metro/Gas')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Rent')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Shopping')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Spotify')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Wealthfront')),
    ((source_target_df['source'] == 'Net Pay') & (source_target_df['target'] == 'Youtube TV')),
    ((source_target_df['source'] == 'Gross Monthly Pay ') & (source_target_df['target'] == 'Cash In Paycheck')),
    ((source_target_df['source'] == 'Gross Monthly Pay ') & (source_target_df['target'] == 'Pre-Tax Deductions')),
    ((source_target_df['source'] == 'Gross Monthly Pay ') & (source_target_df['target'] == 'Taxes')),
    ((source_target_df['source'] == 'Pre-Tax Deductions') & (source_target_df['target'] == '401k')),
    ((source_target_df['source'] == 'Pre-Tax Deductions') & (source_target_df['target'] == 'Dental')),
    ((source_target_df['source'] == 'Pre-Tax Deductions') & (source_target_df['target'] == 'Medical')),
    ((source_target_df['source'] == 'Pre-Tax Deductions') & (source_target_df['target'] == 'Vision')),
    ((source_target_df['source'] == 'Taxes') & (source_target_df['target'] == 'Federal Withholding')),
    ((source_target_df['source'] == 'Taxes') & (source_target_df['target'] == 'Medicare + Social Security')),
    ((source_target_df['source'] == 'Taxes') & (source_target_df['target'] == 'State Tax - VA'))
   
]

link_color_choices = [
    '#FD7523', # orange
    '#FD7523', # orange
    '#23FB64', # green
    '#FC2C29', # red
    '#FD7523', # orange
    '#FC2C29', # red
    '#FD7523', # orange
    '#FC2C29', # red
    '#FC2C29', # red
    '#B31EFD', # purple
    '#B31EFD', # purple
    '#23FB64', # green
    '#B31EFD', # purple
    '#FC2C29', # red
    '#FC2C29', # red
    '#B31EFD', # purple
    '#B31EFD', # purple
    '#23FB64', # green
    '#B31EFD', # purple
    '#FD7523', # orange
    '#FC2C29', # red
    '#FD7523', # orange
]

len(link_color_conditions)
len(link_color_choices)
source_target_df['link_color'] = np.select(link_color_conditions, link_color_choices, default='#000000')
                
link_color_name_conditions = [
    source_target_df['link_color'] == '#B1FCC4',
    source_target_df['link_color'] == '#FDB488',
    source_target_df['link_color'] == '#E1BAFE',
    source_target_df['link_color'] == '#FFAFAE'
    
]
link_color_name_choices = [
    'light green',
    'light orange',
    'light purple',
    'light red'
]

source_target_df['link_color_name'] = np.select(link_color_name_conditions, link_color_name_choices, default='black')

source_target_df

# creating the sankey diagram's components
# as with all plotly charts, the figure is composed of two dictionaries...
# one for the data behind the chart, and one for layout-related specifics

# creating the data behind the figure
data = dict(
    # specify the type of figure we want -- sankey
    type = 'sankey',
    # defining all info / aesthetics regarding the nodes (aka bars / rectangles in the sankey)
    # note: I made the choice to NOT show value and category name for each node-label...
    # I did this to minimize the business in the chart, but if you want both, you would...
    # need to change the "label" parameter below to point at a column concatenating both...
    # the value and name, i.e. label =  label_list_hypotheticaldf['val_and_label_concat']
    node = dict(
        # how much padding between the nodes
        pad = 15,
        # how thick should the nodes be
        thickness = 20,
        # provides faint dark outline for the bars
        line = dict(
            color = "black",
            width = 0.5
        ),
        # speciy the list of category labels
        label = label_list,
        # specify the color of the labels (the bars in the sankey)
        color = label_name_and_color_df['color']
    ),
    # defining all info / aesthetics regarding the linkages between the nodes (aka the flow visuals)
    link = dict(
        source = source_target_df['source_id'],
        target = source_target_df['target_id'],
        value = source_target_df['count'],
        color = source_target_df['link_color']
    ),
    # specifies the orientation of the flows in the sankey
    orientation = "h",
    # adds a $ as prefix and limits to 2 decimals
    # this field uses JS format codes, per the link below...
    # https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_format
    valueformat = "$.2f",
)

# creating the layout behind the figure
layout =  dict(
    # using breaks and tags in-text to achieve the sub-titles
    title = """
    Where Did My Paycheck Go? 
    <br><sub> Breakdown of Monthly Paycheck</sub>
    <br><sub> Source: @Yusful33</sub>
    """,
    # specifiying base font-size for title
    font = dict(
        size = 12
    )
)

#build the plotly figure out of the data and layout components
fig = dict(data=[data], layout=layout)

#import plotly.graphobjects as go
from plotly.offline import plot, iplot
# display the chart interactively in the notebook
iplot(
    figure_or_data = fig
)


# save out an HTML version of the sankey chart
plot(
    figure_or_data = fig,
    filename = "C:/Users/FIY716/Documents/PythonScripts/paycheck_breakdown.html",
    auto_open = False
);