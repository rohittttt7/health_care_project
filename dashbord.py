import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([

    html.H1("🏥 Healthcare Analytics Dashboard",
            style={
                'textAlign': 'center',
                'color': 'white',
                'marginBottom': '30px'
            }),

    # ================= KPI SECTION =================
    html.Div(id='kpi_section',
             style={'display': 'flex',
                    'justifyContent': 'space-around',
                    'marginBottom': '40px'}),

    # ================= SLICERS =================
    html.Div([

        html.Div([
            html.Label("Medical Condition", style={'color': 'white'}),
            dcc.Dropdown(
                id='condition_filter',
                options=[{'label': i, 'value': i}
                         for i in df['medical_condition'].unique()],
                multi=True,
                value=list(df['medical_condition'].unique())
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Smoking", style={'color': 'white'}),
            dcc.Dropdown(
                id='smoking_filter',
                options=[{'label': i, 'value': i}
                         for i in df['smoking'].unique()],
                multi=True,
                value=list(df['smoking'].unique())
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Alcohol", style={'color': 'white'}),
            dcc.Dropdown(
                id='alcohol_filter',
                options=[{'label': i, 'value': i}
                         for i in df['alcohol'].unique()],
                multi=True,
                value=list(df['alcohol'].unique())
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Risk Level", style={'color': 'white'}),
            dcc.Dropdown(
                id='risk_filter',
                options=[{'label': i, 'value': i}
                         for i in df['risk_level'].unique()],
                multi=True,
                value=list(df['risk_level'].unique())
            )
        ], style={'width': '24%'})

    ], style={'display': 'flex',
              'justifyContent': 'space-between',
              'marginBottom': '40px'}),

    # ================= SECTION: OVERVIEW =================
    html.H2("📊 Overview Analysis",
            style={'color': 'white', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(id='fig1', style={'width': '48%'}),
        dcc.Graph(id='fig5', style={'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    # ================= SECTION: RISK ANALYSIS =================
    html.H2("⚠ Risk Analysis",
            style={'color': 'white', 'marginTop': '40px'}),

    html.Div([
        dcc.Graph(id='fig3', style={'width': '48%'}),
        dcc.Graph(id='fig7', style={'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    # ================= SECTION: LIFESTYLE =================
    html.H2("🚬 Lifestyle & Health Factors",
            style={'color': 'white', 'marginTop': '40px'}),

    html.Div([
        dcc.Graph(id='fig2', style={'width': '48%'}),
        dcc.Graph(id='fig6', style={'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    # ================= SECTION: MEDICAL PATTERNS =================
    html.H2("🧬 Medical Pattern Insights",
            style={'color': 'white', 'marginTop': '40px'}),

    html.Div([
        dcc.Graph(id='fig4', style={'width': '48%'}),
        dcc.Graph(id='fig8', style={'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),

    html.Div([
        dcc.Graph(id='fig9', style={'width': '48%'}),
        dcc.Graph(id='fig10', style={'width': '48%'})
    ], style={'display': 'flex',
              'justifyContent': 'space-between',
              'marginBottom': '40px'}),

html.H2("📌 Key Insights Summary", style={
    'color':'white',
    'marginTop':'50px'
}),

html.Ul([

    html.Li("Metabolic conditions such as Diabetes and Obesity demonstrate the highest average risk scores, indicating strong association between chronic conditions and overall health risk escalation."),

    html.Li("Smoking shows a clear increase in median cholesterol levels, reinforcing its impact on cardiovascular risk factors."),

    html.Li("A negative correlation exists between stress levels and sleep duration, suggesting behavioral health significantly influences recovery and wellness stability."),

    html.Li("Higher BMI categories are associated with longer hospital stays, indicating increased treatment complexity and recovery time."),

    html.Li("Alcohol consumption contributes to elevated overall risk scores, though its impact is less pronounced compared to smoking."),

    html.Li("Risk scores increase progressively across age groups, confirming age as a primary determinant of health risk severity."),

    html.Li("Density analysis reveals clustering of high glucose levels among patients with elevated BMI, supporting the metabolic risk relationship."),

    html.Li("Combined lifestyle factors (Smoking + High Risk Level) show amplified hospitalization duration, highlighting compounding health effects.")

], style={
    'color':'#d3d3d3',
    'fontSize':'16px',
    'lineHeight':'1.8'
})

], style={
    'backgroundColor': '#1e1e2f',
    'padding': '30px',
    'fontFamily': 'Arial'
})


@app.callback(
    Output('kpi_section','children'),
    Output('fig1','figure'),
    Output('fig2','figure'),
    Output('fig3','figure'),
    Output('fig4','figure'),
    Output('fig5','figure'),
    Output('fig6','figure'),
    Output('fig7','figure'),
    Output('fig8','figure'),
    Output('fig9','figure'),
    Output('fig10','figure'),

    Input('condition_filter','value'),
    Input('smoking_filter','value'),
    Input('alcohol_filter','value'),
    Input('risk_filter','value')
)
def update_dashboard(cond, smoke, alcohol, risk):

    filtered = df.copy()

    if cond:
        filtered = filtered[filtered['medical_condition'].isin(cond)]

    if smoke:
        filtered = filtered[filtered['smoking'].isin(smoke)]

    if alcohol:
        filtered = filtered[filtered['alcohol'].isin(alcohol)]

    if risk:
        filtered = filtered[filtered['risk_level'].isin(risk)]

    # ================= KPI CARDS =================
    kpi_cards = [

        html.Div([
            html.H4("Total Patients", style={'color': '#bbb'}),
            html.H2(len(filtered), style={'color': 'white'})
        ], style={
            'backgroundColor': '#2a2a40',
            'padding': '20px',
            'borderRadius': '10px',
            'width': '22%',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.4)'
        }),

        html.Div([
            html.H4("Average Risk Score", style={'color': '#bbb'}),
            html.H2(round(filtered['risk_score'].mean(),2), style={'color': 'white'})
        ], style={
            'backgroundColor': '#2a2a40',
            'padding': '20px',
            'borderRadius': '10px',
            'width': '22%',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.4)'
        }),

        html.Div([
            html.H4("Average Stay", style={'color': '#bbb'}),
            html.H2(round(filtered['lengthofstay'].mean(),2), style={'color': 'white'})
        ], style={
            'backgroundColor': '#2a2a40',
            'padding': '20px',
            'borderRadius': '10px',
            'width': '22%',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.4)'
        }),

        html.Div([
            html.H4("Avg Cholesterol", style={'color': '#bbb'}),
            html.H2(round(filtered['cholesterol'].mean(),2), style={'color': 'white'})
        ], style={
            'backgroundColor': '#2a2a40',
            'padding': '20px',
            'borderRadius': '10px',
            'width': '22%',
            'boxShadow': '0 4px 8px rgba(0,0,0,0.4)'
        })
        
    ]

    # ================= GRAPHS =================

    fig1 = px.bar(
        filtered.groupby("medical_condition",as_index=False)['risk_score'].mean(),
        x='medical_condition',
        y='risk_score',
        title='Average Risk Score by Medical Condition'
    )

    fig2 = px.box(
        filtered,
        x='smoking',
        y='cholesterol',
        title='Smoking Impact on Cholesterol'
    )

    fig3 = px.scatter(
        filtered,
        x='stress_level',
        y='sleep_hours',
        color='medical_condition',
        trendline='ols',
        title='Stress vs Sleep Relationship'
    )

    fig4 = px.box(
        filtered,
        x='bmi_category',
        y='lengthofstay',
        title='BMI Category vs Length of Stay'
    )

    condition_count = filtered['medical_condition'].value_counts().reset_index()
    condition_count.columns=['medical_condition','count']

    fig5 = px.pie(
        condition_count,
        names='medical_condition',
        values='count',
        hole=0.4,
        title='Patient Distribution by Condition'
    )

    fig6 = px.box(
        filtered,
        x='alcohol',
        y='risk_score',
        title='Alcohol Impact on Risk Score'
    )

    fig7 = px.sunburst(
        filtered,
        path=['medical_condition','smoking','risk_level'],
        values='lengthofstay',
        title='Condition → Smoking → Risk Level Hierarchy'
    )

    fig8 = px.density_contour(
        filtered,
        x='glucose',
        y='bmi',
        title='Glucose vs BMI Density Contour'
    )

    area_data = filtered.groupby('age_group')['risk_score'].mean().reset_index()

    fig9 = px.area(
        area_data,
        x='age_group',
        y='risk_score',
        title='Risk Score Trend Across Age Groups'
    )

    fig10 = px.scatter_3d(
        filtered,
        x='bmi',
        y='glucose',
        z='cholesterol',
        color='medical_condition',
        title='3D Health Risk Visualization'
    )

    # ================= DARK THEME APPLY =================

    for fig in [fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10]:
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='#2a2a40',
            plot_bgcolor='#2a2a40',
            font=dict(color='white')
        )

    return kpi_cards, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10

if __name__ == "__main__":
    app.run(debug=True)