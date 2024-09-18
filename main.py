"""
Main
"""

from mylib.lib import read_csv_file, stats_overview, split_day_night, hist_day_night

# import pandas as pd
# import matplotlib.pyplot as plt


def main(csv_file):
    # Read file
    df = read_csv_file(csv_file)

    # Get statistics about traffic volume
    traffic_volume_summary = stats_overview(df, "traffic_volume")
    print("Traffic Volume Summary\n", traffic_volume_summary, "\n")

    # Traffic stats: Day vs Night
    day_df, night_df = split_day_night(df)
    day_traffic_volume = stats_overview(day_df, "traffic_volume")
    print("Day Traffic Volume Stats\n", day_traffic_volume, "\n")

    night_traffic_volume = stats_overview(night_df, "traffic_volume")
    print("Night Traffic Volume Stats\n", night_traffic_volume, "\n")

    # Histogram of Traffic Volume: Day vs Night
    hist_fig = hist_day_night(day_df, night_df)
    hist_fig.savefig("Figure/Traffic.png")


# if __name__ == "__main__":
# main("Metro_Interstate_Traffic_Volume.csv.gz")
