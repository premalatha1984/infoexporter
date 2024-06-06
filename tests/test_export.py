
#### 6. Testing

In `tests/test_export.py`, write tests:

```python
# tests/test_export.py
import os
import json
import pandas as pd
from data_exporter import export_data

def test_export_csv():
    data = [['name', 'age'], ['Alice', 30], ['Bob', 25]]
    export_data(data, 'csv', 'test_output.csv')
    assert os.path.exists('test_output.csv')

def test_export_json():
    data = [['name', 'age'], ['Alice', 30], ['Bob', 25]]
    export_data(data, 'json', 'test_output.json')
    with open('test_output.json') as f:
        loaded_data = json.load(f)
    assert loaded_data == data

def test_export_excel():
    data = [['name', 'age'], ['Alice', 30], ['Bob', 25]]
    export_data(data, 'excel', 'test_output.xlsx')
    df = pd.read_excel('test_output.xlsx')
    assert df.values.tolist() == data

# Clean up test files
def teardown_module(module):
    os.remove('test_output.csv')
    os.remove('test_output.json')
    os.remove('test_output.xlsx')
