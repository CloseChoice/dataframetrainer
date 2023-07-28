def rename_column(df):
    df = df.rename(columns={"Value": "NewValue"})
    print('sheeeeeeeeesh')

    df.iloc[0]['NewValue'] = 9876
    return df