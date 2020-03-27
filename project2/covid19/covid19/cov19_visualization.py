import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go

online_fname = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
local_fname = 'time_series_2019-ncov-Confirmed.csv'
local_country_name_fname = "country_code.xlsx"

def aggregate_nation_data(country, df):
    if country == 'China':
        states_data = df[(df["Country/Region"] == 'China').values | (df["Country/Region"] == 'Taiwan*').values]
    else:
        states_data = df[df["Country/Region"] == country]
    nation_data = states_data.sum()
    nation_data['Province/State'] = np.nan
    nation_data['Country/Region'] = country
    if country in ['China', 'Australia', 'Canada']:
        nation_data['Lat'] = states_data['Lat'].values.mean()
        nation_data['Long'] = states_data['Long'].values.mean()
    else:
        nation_data['Lat'] = states_data[states_data["Province/State"] == country]['Lat'].values[0]
        nation_data['Long'] = states_data[states_data["Province/State"] == country]['Long'].values[0]
    nation_data = pd.DataFrame(nation_data)
    df.drop(states_data.index, inplace = True)
    return pd.DataFrame(nation_data)

def get_data(data_path, country_code_path):
    df = pd.read_csv(data_path)
    us_rows = df[df["Country/Region"] == "US"]
    us_counties = us_rows[us_rows["Province/State"].apply(lambda x: ',' in x)]
    df.drop(us_counties.index, inplace = True)
    df.reset_index(inplace=True)
    countries = ['Australia', 'China', 'Canada', 'US', 'United Kingdom', 'France', 'Denmark', 'Netherlands']
    for country in countries:
        aggregated = aggregate_nation_data(country, df)
        df = pd.concat([df, aggregated.T], axis = 0)
    df.reset_index(inplace=True)
    df.drop(['level_0', 'index', 'Province/State'], axis = 1, inplace=True)
    country_code = pd.read_excel(country_code_path)
    countries_with_data = df["Country/Region"].values.tolist()
    coded_countries = country_code["COUNTRY"].values.tolist()
    no_data_countries = [c for c in coded_countries if not c in countries_with_data]
    blank_countries = pd.DataFrame(np.zeros((len(no_data_countries), df.shape[1])), columns = df.columns)
    blank_countries["Country/Region"] = no_data_countries
    appended_df = pd.concat([df, blank_countries], axis = 0)
    merged_df = pd.merge(appended_df, country_code, left_on='Country/Region', right_on = 'COUNTRY', how = 'left')
    merged_df[merged_df.COUNTRY.isnull()]
    cleaned_df = merged_df[merged_df.COUNTRY.notnull()]
    return cleaned_df


def draw_figure(df, date):
    fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df[date],
        text = df['Country/Region'],
        colorscale = 'Reds',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='lightgray',
        marker_line_width=0.5,
        colorbar_title = 'Confirmed cases',
    ))

    fig.update_layout(
        title_text='COVID19 Accumulative Confirmed Cases on '+ date,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    return fig

def run(date, data_path, country_code_path, output_file_prefix):
    cleaned_df = get_data(data_path, country_code_path)
    fig = draw_figure(cleaned_df, date)
    date_code = date.replace('/', '-')
    output_file_name = output_file_prefix + 'cov19-confirmed-'+ date_code + '.html'
    plotly.offline.plot(fig, filename=output_file_name, auto_open=False)
    return output_file_name
if __name__ == '__main__':
    date = '3/21/20'
    output_fname = run(date, './data/' + local_fname, './data/' + local_country_name_fname,'./output/')