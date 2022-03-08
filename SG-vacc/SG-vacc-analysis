import pandas as pd
import plotly.express as px

sg_vacc = pd.read_csv("data/primary-series-vaccination-take-up-by-age-group.csv")
sg_vacc
#remove_zeros

sg_vacc = sg_vacc[sg_vacc.full_regimen_pcttakeup > 0] 

fig = px.bar(sg_vacc, x="agecat", y="first_dose_pcttakeup", color="full_regimen_pcttakeup", 
                 log_x=False, 
                 animation_frame="vacc_date", labels={"full_regimen_pcttakeup":"Fully Vaccinated"}, # add animation_frame and animation_group
                 range_x=[0,7], range_y=[0,100]              # define x & y axis range for animation duration
)

fig.update_yaxes(title_text= "Percentage with first dose",ticksuffix="%")
fig.update_xaxes(title_text="Age group")

fig.show()
