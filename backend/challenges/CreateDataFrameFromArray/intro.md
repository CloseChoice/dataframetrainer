Cast a numpy array to a DataFrame.
<h3> Example Input</h3>
<h4> array</h4>
array([[1, 2],       [3, 4]])

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>col_1</th>      <th>col_2</th>    </tr>  </thead>  <tbody>    <tr>      <th>col_1</th>      <td>1</td>      <td>2</td>    </tr>    <tr>      <th>col_2</th>      <td>3</td>      <td>4</td>    </tr>  </tbody></table></div>