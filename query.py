import pandas as pd


def gen_query():
    sheet_url = "https://docs.google.com/spreadsheets/d/1uvSnHxwpO0NAqj247IKMmgijM6_OqCh2e1nqmGccCY0/edit#gid=0"
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

    df = pd.read_csv(url_1)
    query_list = []
    for rowIndex, row in df.iterrows():
        flag = True
        email = ''
        temp_list = []
        for columnIndex, value in row.items():
            if flag:
                email = value
                flag = False
                continue
            if value == value:
                temp_list.append(value.split())
        query_list.append((email, temp_list))
    return query_list
