Transform the `number_col` so that each 1 becomes 100, 2 becomes 0.5 and 3 becomes 1.
Make sure all are floats.

<h3> Example Input</h3>
<h4> df</h4>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>number_col</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>1</td>    </tr>    <tr>      <th>1</th>      <td>2</td>    </tr>    <tr>      <th>2</th>      <td>3</td>    </tr>    <tr>      <th>3</th>      <td>2</td>    </tr>    <tr>      <th>4</th>      <td>3</td>    </tr>  </tbody></table></div>

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>number_col</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>100.0</td>    </tr>    <tr>      <th>1</th>      <td>0.5</td>    </tr>    <tr>      <th>2</th>      <td>1.0</td>    </tr>    <tr>      <th>3</th>      <td>0.5</td>    </tr>    <tr>      <th>4</th>      <td>1.0</td>    </tr>  </tbody></table></div>