Transform the dictionary into a DataFrame, so that each value corresponds to a column and the key is the column name.
<h3> Example Input</h3>
<h4> col_1</h4>
['Charles', 'Lisa']

<h4> col_2</h4>
['Andrew', 'Emily']

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>col_1</th>      <th>col_2</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Charles</td>      <td>Lisa</td>    </tr>    <tr>      <th>1</th>      <td>Andrew</td>      <td>Emily</td>    </tr>  </tbody></table></div>