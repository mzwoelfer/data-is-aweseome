import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from helpers import open_json


def plot_coal_data(year, line_day_of_year=None, line_label=None):
    coal_data = open_json("coal_data.json")

    df = pd.DataFrame(coal_data)
    df["time"] = pd.to_datetime(df["time"])
    df["year"] = df["time"].dt.year

    filtered_df = df[df["year"].between(2015, year)]

    fig, ax = plt.subplots()

    grouped_df = filtered_df.groupby("year")

    for grp_year, data in grouped_df:
        days = (data["time"] - pd.Timestamp(year=grp_year, month=1, day=1)).dt.days
        if grp_year == year:
            ax.plot(days, data["data"], label=str(grp_year), alpha=1)
        else:
            ax.plot(days, data["data"], label=str(grp_year), alpha=0.1)

    if line_day_of_year is not None and line_label is not None:
        ax.axvline(x=line_day_of_year, color="red", label=line_label)

    ax.yaxis.grid(True, linestyle="-", linewidth=0.5)

    formatter = ticker.FuncFormatter(lambda x, pos: f"{x/1e3:.1f}")
    ax.yaxis.set_major_formatter(formatter)

    ax.set_xlabel("Days in Year")
    ax.set_ylabel("Daily Coal Production in GWh")
    ax.set_title(
        f"Daily Germany Net Coal Production - Data Comparison 2015 through {year}"
    )
    ax.legend()

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot coal production data.")
    parser.add_argument(
        "year", type=int, help="Year to highlight in the plot (e.g., 2022)"
    )
    parser.add_argument(
        "--line_day",
        type=int,
        default=None,
        help="Day of the year for the vertical line (optional, e.g., 105)",
    )
    parser.add_argument(
        "--line_label",
        type=str,
        default=None,
        help="Label for the vertical line (optional, e.g., 'Event Description')",
    )

    args = parser.parse_args()

    plot_coal_data(
        args.year, line_day_of_year=args.line_day, line_label=args.line_label
    )
