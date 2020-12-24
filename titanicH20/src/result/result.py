import pandas as pd


def result(pred, test, path):
    res = pred.as_data_frame().predict
    passenger_id = test['PassengerId'].as_data_frame()
    res = pd.concat([passenger_id, res], axis=1, ignore_index=True)
    res.to_csv(path, index=False)
