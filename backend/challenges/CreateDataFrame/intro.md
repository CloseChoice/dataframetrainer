Combine the lists so that the first elements are in the first row, the second elements in the second row, etc.
Make sure your columns are ordered as desired.
<h3> Example Input</h3>
<h4> list1</h4>
[1, 2, 3, 4, 5]

<h4> list2</h4>
[-1.0, 2.0, 3.0, 4.0, 5.0]

<h4> list3</h4>
['a', 'b', 'c', 'd', 'e']

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>string_list</th>      <th>float_list</th>      <th>integer_list</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>a</td>      <td>1.0</td>      <td>1</td>    </tr>    <tr>      <th>1</th>      <td>b</td>      <td>2.0</td>      <td>2</td>    </tr>    <tr>      <th>2</th>      <td>c</td>      <td>3.0</td>      <td>3</td>    </tr>    <tr>      <th>3</th>      <td>d</td>      <td>4.0</td>      <td>4</td>    </tr>    <tr>      <th>4</th>      <td>e</td>      <td>5.0</td>      <td>5</td>    </tr>  </tbody></table></div>