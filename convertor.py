import json
from datetime import datetime

import click
import pandas as pd

from weather.location import geocode_by_ip
from weather.weather import get_weather_data


@click.command()
@click.argument('input_path', type=click.Path(exists=False))
@click.argument('output_path')
def main(input_path, output_path):
    current = datetime(2016, 4, 4, 7, 56)
    print(current.timestamp())
    current = datetime.strptime('4/4/16 7:56', '%m/%d/%y %H:%M')
    print(current.timestamp())
    current = datetime.strptime('4/4/16 7:56 -0500', '%m/%d/%y %H:%M %z')
    print(current.timestamp())
    # df = pd.read_csv('./sample/sample.csv')
    # new_df = pd.DataFrame()
    # index = []
    # for _, row in df.iterrows():
    #     t1_ip_address = row['T1_IPAddress']
    #     t1_start_time = row['T1_StartDate']
    #     if t1_ip_address and t1_start_time != '#NULL!':
    #         print(t1_start_time)
    #         current = datetime.strptime('4/4/16 7:56', '%m/%d/%y %H:%M')
    #         print(current.timestamp())
    #         current = datetime.strptime('4/4/16 7:56 -0500', '%m/%d/%y %H:%M %z')
    #         print(current.timestamp())
    #         # result = get_weather_data(ip_address=t1_ip_address,
    #         #                         date_string=t1_start_time)
    #         # json_string = json.dumps(result, sort_keys=True, indent=4)
    #         # print(json_string)
    #     t2_ip_address = row['T2_IPAddress']
    #     t2_start_time = row['T2_StartDate']


if __name__ == '__main__':
    main()
