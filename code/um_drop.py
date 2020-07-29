# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:19:16 2018

@author: swathisri.r
"""

import dash
import visdcc
import copy
import pickle
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output
import urllib

static_css_route = '/static/'
stylesheets = ['stylesheet.css']
#first pickle df
df=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\first.pkl",'rb'))#df
d_excel=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\d_excel.pkl",'rb'))
dtot=copy.deepcopy(d_excel)
dff=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\data_final.pkl",'rb'))#dff
g=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\g.pkl",'rb'))
dup=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\dup.pkl",'rb'))
l=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\l.pkl",'rb'))
df_last=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\df_last.pkl",'rb'))
df_last1=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\df_last1.pkl",'rb'))
df_first=pickle.load(open("D:\\TestOptimizer\\TestOptimizer\\NL\\df_first.pkl",'rb'))
df_last1['Description']=df_last['Description'].replace(' ','')
test_id=df_last1['TESTCASE_ID']
df2=pd.Series(df['combined'])
df3=pd.Series(df['100'])
df4=pd.Series(df['90_99'])
df5=pd.Series(df['80_89'])

t=len(df)

#app= flask.Flask(__name__)
css_directory = r'D:\D3'

STATS=['Total','Duplicates','Unique']

app=dash.Dash()
def sim_table(manual_id):
    global df1,df_copy,v
    df1=pd.DataFrame(columns=['TESTCASE_ID','Description','Project','Similarity'])
    #df1=df1[['TESTCASE_ID','Name','Similarity']]
    
    a=df_first[df_first['l']==int(manual_id)]
    b=len(a['100'].iloc[0])
    print(b)
    c=len(a['90_99'].iloc[0])
    d=len(a['80_89'].iloc[0])
    count=0
    
    for i in range(b):
            id1=a['100'].iloc[0][i][0]
            score=a['100'].iloc[0][i][1]
            data1=df_last[df_last['TESTCASE_ID']==id1]
            df1=df1.append(data1)
            df1.Similarity.iloc[count]=score
            count=count+1
            
    for i in range(c):
            id2=a['90_99'].iloc[0][i][0]
            score=a['90_99'].iloc[0][i][1]
            data2=df_last[df_last['TESTCASE_ID']==id2]
            df1=df1.append(data2) 
            df1.Similarity.iloc[count]=score
            count=count+1
    for i in range(d):
            id3=a['80_89'].iloc[0][i][0]
            score=a['80_89'].iloc[0][i][1]
            data3=df_last[df_last['TESTCASE_ID']==id3]
            df1=df1.append(data3)# Header
            df1.Similarity.iloc[count]=score
            count=count+1
            
    df_copy=copy.deepcopy(df1)      
    
    return(df1)


def net_sim(manual_id):
    """
    Example clickData
    data ={'nodes':[{'id': 1, 'label':    x    , 'color':'#00ffff'},
                    {'id': 2, 'label': 'Tc id 2'},
                    {'id': 4, 'label': 'Tc id 4'},
                    {'id': 5, 'label': 'Tc id 5'},
                    {'id': 6, 'label': 'Tc id 6'}                    ],
           'edges':[{'id':'1-3', 'from': 1, 'to': 3},
                    {'id':'1-2', 'from': 1, 'to': 2} ]
           }
    
    
    """
    X=str(manual_id)
    sim_id=[]
    sim_score=[]
    a=df_first[df_first['l']==int(manual_id)]
    b=len(a['100'].iloc[0])
    c=len(a['90_99'].iloc[0])
    d=len(a['80_89'].iloc[0])
    for i in range(b):
            sim_id.append(a['100'].iloc[0][i][0])
            sim_score.append(a['100'].iloc[0][i][1])
    for i in range(c):
            sim_id.append(a['90_99'].iloc[0][i][0])
            sim_score.append(a['90_99'].iloc[0][i][1])        
    for i in range(d):
            sim_id.append(a['80_89'].iloc[0][i][0])
            sim_score.append(a['80_89'].iloc[0][i][1])    
    print(sim_id,sim_score)    
    
    nodes_list=[{'id':i,'label':f'Tc id {i}','color':'#58D3F7'} for i in sim_id]
    
    
    nodes_list.append({'id': X, 'label': str(X), 'color':'#A9E2F3'})
    edge_list=[{'id':f'{X}-{i}','from':X,'to':i,'label': str(round(score,3))} for i,score in zip(sim_id,sim_score)]
    
    data ={'nodes':nodes_list,
           'edges':edge_list,
                    
           }
    return data


element1=visdcc.Network(id ='sim-net', 
                         options = dict(height= '800px', width= '80%'))
element2=html.Div(id='test-diff-output')
graph_vis=html.Div(children=[html.Div(element1,style={'width':'80%','margin-left':'250px'}),
                                 element2],style={'margin-left':'200px','margin-right':'100px' ,'width':'80%'})
def  frontend_layout_with_stats(): 
   global total,dtot
   total=[t,len(l),t-len(l)]
   dup_layout=html.Div([
                     #nav wrapper starts here
   html.Div(
        children=[
            #nav bar
            html.Nav(
                #inside div
                html.Div(
                    children=[
                        html.A(
                            'TestOPTIMIZE',
                            className='brand-logo',
                            href='/',style={'font-size':'16','margin-top':'0px',
    'margin-bottom': '10px',
    'margin-left': '10px'}
                        ),
                        #ul list components
                        html.Ul(
                            children=[
                               html.Li(html.A('HOME', href='http://127.0.0.1:9117/test',style={'font-size':'16'})),
                               
                            ],
                            id='nav-mobile',
                            className='right hide-on-med-and-down'
                        ), 
                    ],
                    className='navbar-brand'
                ),style={'background-color':'#0B3B2E','height':'50px'}),

        ],
        className='navbar-fixed'
    ),
          
     html.Div(
             children=[
 
            html.A(html.Button(str(total[0])+' '+ STATS[0],
                    id=STATS[0],style={'background':'#5F9EA0','font-weight':'bolder','color':'white','margin-top':'100px','border-radius': '50%','box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
    'margin-bottom': '80px',
    'margin-right': '100px',
    'margin-left': '110px','width':'200px','height':'200px','font-size':'23'
  
    }),
    href='#'),
            html.A(html.Button(str(total[1])+' '+STATS[1],
                    id=STATS[1],style={'background':'#5F9EA0','font-weight':'bolder','color':'white','margin-top':'100px','border-radius': '50%','box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
    'margin-bottom': '100px',
    'margin-right': '100px',
    'margin-left': '110px','width':'200px','height':'200px','font-size':'23'
    }),href='#'),
            html.A(html.Button(str(total[2])+' '+STATS[2],
                    id=STATS[2],style={'background':'#5F9EA0','font-weight':'bolder','color':'white','margin-top':'100px','border-radius': '50%','box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
    'margin-bottom': '100px',
    'margin-right': '100px',
    'margin-left': '110px','width':'200px','height':'200px','font-size':'23'
    }
    ),href='#'),
            html.Br(),
            html.Br(),
           
#
   
   
#        
#            sim_ele,
           html.Div(style={'backgroundColor': '#AFEEEE','text-align':'center','font-family': 'corbel','font-style':'bold'
                            }
                            ,children=html.H5('SIMILARITY TABLE')),
           html.Div(dt.DataTable(rows=g.to_dict('records'),
                                     id='similarity-datatable',
                                     columns=['TESTCASE_ID','100','90_99','80_89']
                                    ),style={'background':'#BEF781'}),
            html.Br(),
            html.P(['Enter the testcase id for the node diagram'],style={'text-align':'center','color':'blue'}),dcc.Input(id='manual-test-case-id', name='Enter the testcase',
                                           value=' ', type='text',
                                           style={'width': '20%','margin-left': '550px','margin-right': '20px','text-align':'center','align':'center','font-weight':'bold'}),
            graph_vis,
          
           
            html.Div(style={'backgroundColor': '#AFEEEE','text-align':'center','font-family': 'corbel','font-style':'bold'
                            }
                            ,children=html.H5('TESTCASE TABLE')),
            html.Div(dt.DataTable(id='dt',rows=[{}],row_selectable=True,selected_row_indices=[],filterable=True,sortable=True)),
            html.Br(),
            html.Br(),
            html.Div(html.Button('Purge',id='purge-button',style={'background':'#307D7E','font-weight':'bolder','color':'white'}),style={'margin-left':'800px','height':'500px','width':'100px','margin-top':'70px'}),
            html.Div(id='purge-output',children=" ",style={'margin-left':'810px','height':'500px','width':'100px','margin-top':'-400px'}),],style={'background-image': 'url(/static/img/Slide7.png)'})
  
  
    
            ])
   return dup_layout
def two_columns_grid(element1,element2,className="six column"):
        """
        input :Two html elements (from Dash)
        output: returns dash html div with two grids
        """
        two_colum_div=html.Div(children=[html.Div(children=element1,className=className),html.Div(children=element2)],
                               className="row",style={'margin-left':'80px', 'margin-right': '150px'})
        return two_colum_div
def update_download_link_defect(n_clicks,selected_row_indices):
    """
    Update the download link with new data after every purging of 
    Duplicate testcases
    """
    
    global global_n_clicks,total,df_copy,dup
    global_n_clicks=0
    if n_clicks==None:global_n_clicks=0
        
    if n_clicks!=None:
        if n_clicks-global_n_clicks==1:
#          
#           
#            df_copy.drop(df_copy[df_copy['TESTCASE_ID'].index==selected_row_indices].index)
#              
#            
           
            dtot.set_index('TESTCASE_ID',inplace=True)
            dtot.drop(dtot[dtot.index==selected_row_indices].index,inplace=True)
#            dtot.reset_index(drop=True,inplace=True)
    
#            dtot.drop(labels=selected_row_indices,inplace=True)
                 
             
            csv_string = dtot.to_csv(index=True, encoding='utf-8')
            csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
            
#            global_n_clicks=n_clicks
    
    
    
    return (two_columns_grid(html.H4('Current total testcases {}'.format(dtot.shape[0]),className='dup-count'),
                          html.A(
                            html.H5('Download unique testcases'),
                            id='Download',
                            download="unique_testcases.csv",
                            href=csv_string,
                            target="_blank",style={'color':'blue'},
#    'margin-right': '150px','margin-top':'70px',
#    'margin-left': '80px','width':'200px','height':'200px'},
                            className='download-link')))
def highlight_sent(sent1,sent2):
    """
    Highlights th words that are missing in the both the sentances
    using html span tag
    
    """
    
    sent_list1=[word for word in sent1.split(' ') if word not in sent2.split(' ')]
    sent_list2=[word for word in sent2.split(' ') if word not in sent1.split(' ')]
    template1='<span style="background-color: #99ccff">{}</span>'

    highlighted_sent1=sent1.split(' ')
    for w1 in sent_list1:
        for w2 in sent1.split(' '):
            if w1==w2:
                try:
                    highlighted_sent1[highlighted_sent1.index(w1)]=template1.format(w1)
                except ValueError:
                    pass
    
    
    template2='<span style="background-color: #ff9999">{}</span>'
    highlighted_sent2=sent2.split(' ')
    for w1 in sent_list2:
        for w2 in sent2.split(' '):
            if w1==w2:
                try:
                    highlighted_sent2[highlighted_sent2.index(w1)]=template2.format(w1)
                except ValueError:
                    pass
    
    highlighted_sent1=' '.join(highlighted_sent1)
    highlighted_sent2=' '.join(highlighted_sent2)
    return highlighted_sent1,highlighted_sent2


def give_test_case(graph,manual_id,da):   
    """
    Based on the clicked data from the heatmap it gives the sentances with html tag
    
    """
    
    
#    x=clickData['points'][0]['y']
    
    
    dd=da
    dd['Description']=dd['Description'].replace(' ','')
    x=dd[dd['TESTCASE_ID']==int(manual_id)].index[0]
        
    sent1=dd[dd['TESTCASE_ID']==x].values[0][0]
    
    id1=graph['nodes'][0]
    id2=x
 
    y=dd[dd['TESTCASE_ID']==graph['nodes'][0]].index[0] #.split(' ')  
    sent2=dd[dd['TESTCASE_ID']==y].values[0][0]
    
    htc1,htc2=highlight_sent(sent1,sent2)
#
    htc1='<html><h2>TC: {0}</h2><h3>{1}</h3></html>'.format(id2,htc1)
    htc2='<html><h2>TC: {0}</h2><h3>{1}</h3></html>'.format(id1,htc2)
##    
##    hsd1='<html><h2>{2}: {0}</h2><h3>{1}</h3></html>'.format(id2,hsd1,df_new['TESTCASE_ID'])
##    hsd2='<html><h2>{2}: {0}</h2><h3>{1}</h3></html>'.format(id1,hsd2,df_new['TESTCASE_ID'])
##    
    div1=html.Div(children=[html.Div(html.Iframe(sandbox='',srcDoc=htc1,id='test id',
                                    style={'border-radius':'10px',
                                            'border-style':'solid',
                                            'background':'#E5E4E2',
                                            'border-color':' #FFFFFF',
                                            'border-width':'2px',
                                            'height':'200px',
                                            'width':'45%','margin-top':'10px',
#                                            'font-weight':'normal','padding-top':'-1px','margin-bottom':'2500px',
                                             'float': 'left',
                                            }),style={'margin-top':'30px'})])
    div2= html.Div(children=[html.Div(html.Iframe(sandbox='',srcDoc=htc2,id='test text',
                                    style={'border-radius':'10px',
                                            'border-style':'solid',
                                            'background':'#E5E4E2',
                                            'border-color':' #FFFFFF',
                                            'border-width':'2px',
                                            'height':'200px',
                                            'width':'55%','margin-top':'10px',
                                             'float': 'right'
                                            }))],style={'margin-bottom': '100px',
    'margin-right': '20px',
    'margin-left': '150px'},
                                            className='row')
    div=html.Div([div1,div2])
    
    return (div)

    
    
app.layout=frontend_layout_with_stats()
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                     'https://cdnjs.cloudflare.com/ajax/libs/vis/4.20.1/vis.min.css','https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css',
                    
                     "/static/{}".format(stylesheets[0]) ]

#external_css = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css']


for css in external_css:
    app.css.append_css({"external_url": css})


@app.callback(
     Output('sim-net','data'),
    [Input('manual-test-case-id','value')])
def wrap2(manual_id):
    print (manual_id)
    return net_sim(manual_id)
@app.callback(
    Output('test-diff-output', 'children'),
    [
     Input('sim-net', 'selection'),
     
     Input('manual-test-case-id','value')])
def wrap3(graph,manual_id):
    da=sim_table(manual_id)
    return give_test_case(graph,manual_id,da)    
    
@app.callback(
    Output('dt','rows'),
    [Input('manual-test-case-id','value')])
def wrap4(manual_id):
    da= sim_table(manual_id)
    return (da.to_dict('records'))
#@app.callback(
#     Output('')
#    
@app.callback(
    dash.dependencies.Output('purge-output', 'children'),
     #dash.dependencies.Output('dt', 'rows')],
    
    [ dash.dependencies.Input('purge-button', 'n_clicks'),
#     Input('dt', 'rows'),
      dash.dependencies.Input('dt', 'selected_row_indices')])
def wrap5(n_clicks,selected_row_indices):
     #return 'The input value was "{}" and the button has been clicked {} times'.format(
        #selected_row_indices,
        #n_clicks)
     return update_download_link_defect(n_clicks,selected_row_indices)

if __name__=='__main__':
   #run_simple('0.0.0.0', 8080, server, use_reloader=True, use_debugger=True)
   app.run_server(port=9171,debug=True)   
