Transform the dictionary into a DataFrame, so that each value corresponds to a row and the key is the index. The column names
are starting from 0 and are ever increasing.
<h3> Example Input</h3>
<h4> col_1</h4>
['Charles', 'Lisa']

<h4> col_2</h4>
['Andrew', 'Emily']

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>0</th>      <th>1</th>    </tr>  </thead>  <tbody>    <tr>      <th>col_1</th>      <td>Charles</td>      <td>Lisa</td>    </tr>    <tr>      <th>col_2</th>      <td>Andrew</td>      <td>Emily</td>    </tr>  </tbody></table></div>