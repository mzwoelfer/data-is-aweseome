import json
import os


def create_filename(folder, query_string):
    filename = os.path.join(folder, query_string)
    return filename


def create_url(search_string, base_url):
    url = os.path.join(base_url, search_string)
    return url


def write_json_data_to_file(json_data, filename):
    with open(filename, "w") as f:
        json.dump(json_data, f)


def create_query_string(intervall_query_string, date_query_string):
    search_string = intervall_query_string + "_" + str(date_query_string) + ".json"
    return search_string


def main():
    """Generates a list of downloadlinks and writes to search_urls.json"""
    year_list = list(range(1990, 2027))
    base_url = "https://www.energy-charts.info/charts/power/data/de/"
    old_base_url = "https://www.energy-charts.info/charts/power/raw_data/de/"
    search_urls = []
    intervall_query_string = "year"

    for year in year_list:
        search_string = create_query_string(intervall_query_string, year)
        search_filename = create_filename("", search_string)
        url = create_url(search_filename, base_url)
        old_url = create_url(search_filename, old_base_url)

        search_urls.append(url)
        search_urls.append(old_url)

    write_json_data_to_file(search_urls, "search_urls.json")


if __name__ == "__main__":
    main()
