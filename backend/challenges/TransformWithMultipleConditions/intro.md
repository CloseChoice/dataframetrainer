
Add an additional column `Color`, whose values depend on `Set` and `Type`. If:
 - `Set` is `Z` and `Type` is `A` then set `Color` to `green`
 - `Set` is `Z` and `Type` is `B` then set `Color` to `red`
 - `Set` is not `Z` and `Type` is `B` then set `Color` to `pink`
<h3> Example Input</h3>
<h4> df</h4>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Type</th>      <th>Set</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>A</td>      <td>Z</td>    </tr>    <tr>      <th>1</th>      <td>B</td>      <td>Z</td>    </tr>    <tr>      <th>2</th>      <td>B</td>      <td>X</td>    </tr>    <tr>      <th>3</th>      <td>C</td>      <td>Y</td>    </tr>  </tbody></table></div>

<h3> Expected Output</h3>
<div><style scoped>    .dataframe tbody tr th:only-of-type {        vertical-align: middle;    }    .dataframe tbody tr th {        vertical-align: top;    }    .dataframe thead th {        text-align: left;    }</style><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Type</th>      <th>Set</th>      <th>Color</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>A</td>      <td>Z</td>      <td>green</td>    </tr>    <tr>      <th>1</th>      <td>B</td>      <td>Z</td>      <td>red</td>    </tr>    <tr>      <th>2</th>      <td>B</td>      <td>X</td>      <td>pink</td>    </tr>    <tr>      <th>3</th>      <td>C</td>      <td>Y</td>      <td>black</td>    </tr>  </tbody></table></div>