# 🐷 PygQuery

Multi-treaded wrapper to read and write Pandas dataframes with Google BigQuery without the hassle of the heavy BigQuery API.

By design, PygQuery is multi-treaded, meaning that any SQL request is a thread by it's own.
The advantage of this is you can lauch multiples requests in parallel, and wait for data when you need it later.

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
1. `request` : A string of your query. E.g. `"""SELECT * FROM myproject.dataset.table"""`
2. `project` : The string of the project you are currently gathering data
3. `api_key_path` : a path of the G Sevice Account key, you can create one in the IAM tab of your GCP interface

Let's instantiate our data reader:
```python
reader_dict = {
  'request' : """SELECT * FROM myproject.dataset.table""",
  'project' : 'myproject',
  'api_key_path' : 'folder/key.json'
}

# If there any error in your query at the instantiation stage, BigQuery will tell you at this moment
my_request = BigQueryReader(**reader_dict) 
```
Now you have an object ready to be launched. If the line of code above pass, you know that:
1. There is no error in the SQL
2. There is no credentials failure


Let's fire up this object:

```python

my_request.start() # Launch the Tread to download

"# ... Do other things while data is downloading, like launching an other request ... #"

my_request.join() # Say to Python to wait for your download to complete

my_data = myRequest.data # Get your data
```

Et voilà! You have your data in Pandas `DataFrame` format ready to be crunched.
```python
my_data.info()
my_data.head()

```
