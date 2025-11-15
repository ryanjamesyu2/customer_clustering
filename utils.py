# A module containing useful helper methods for customer clustering
def normalize(data):
    """A function to normalize data used for DBSCAN clustering

    Parameters
    ----------
    data : DataFrame
        A pandas DataFrame to be normalized

    Returns
    -------
    DataFrame
        The normalized DataFrame
    """
    cols = [c for c in data.columns if c != 'customer_id']
    for col in cols:
        data[col] = (data[col] - data[col].mean()) / data[col].std()

    return data
