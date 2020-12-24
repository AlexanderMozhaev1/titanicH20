def load_data(h2o, path):
    df = h2o.upload_file(path)
    y = "Survived"
    df[y] = df[y].asfactor()
    return df, y
