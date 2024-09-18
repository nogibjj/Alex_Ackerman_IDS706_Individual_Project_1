"""
Library
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_csv_file(file_name):
    return pd.read_csv(file_name)


def stats_overview(df, col):
    stat_table = df[[col]].describe()  # Doesn't include median
    median = df[[col]].median()
    stat_table.loc["median"] = median  # Add median to stat_table
    return stat_table


def split_day_night(df):
    # Transform 'date_time to datetime'
    df["date_time"] = pd.to_datetime(df["date_time"])

    # Separate data into day and night
    df_day = df.copy()[(df["date_time"].dt.hour >= 7) & (df["date_time"].dt.hour < 19)]
    df_night = df.copy()[
        (df["date_time"].dt.hour >= 19) | (df["date_time"].dt.hour < 7)
    ]

    return df_day, df_night


def hist_day_night(df_day, df_night):
    fig = plt.figure(figsize=(11, 4))

    plt.subplot(1, 2, 1)
    plt.hist(df_day["traffic_volume"])
    plt.xlim(-100, 7500)
    plt.ylim(0, 8000)
    plt.title("Traffic Volume: Day")
    plt.xlabel("Traffic Volume")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(df_night["traffic_volume"])
    plt.xlim(-100, 7500)
    plt.ylim(0, 8000)
    plt.title("Traffic Volume: Night")
    plt.xlabel("Traffic Volume")
    plt.ylabel("Frequency")

    return fig
