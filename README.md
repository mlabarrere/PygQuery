# 🐷 PygQuery

Simple helper to read and write data with Google BigQuery without the hassle of the heavy BigQuery API

### Install
On CLI, just type: 
```shell
pip install pygquery
```

### Read Data

Let's import the module first
```python
from pygquery.bigquery import BigQueryReader
```

The class needs 3 arguments to work:
1. `request` : A string of your query. E.g. `"""SELECT * FROM project.dataset.table"""`
2. `project` : The string of the project you are currently gathering data
3. `api_key_path` : a path of the G Sevice Account key, you can create one in the IAM tab of your GCP interface


