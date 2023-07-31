We make it pretty easy for you: Rename the `Value` column to `NewValue` and keep everything else as is.

<!--These html outputs are generated with  RenameColumn.create_df_func().example().to_html()-->
### Input
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Value</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>2</td>    </tr>    <tr>      <th>1</th>      <td>4</td>    </tr>    <tr>      <th>2</th>      <td>5</td>    </tr>  </tbody></table>


<!--These html outputs are generated with  
df = RenameColumn.create_df_func().example()
RenameColumn.transform(df).to_html()
-->
### Expected Output
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>NewValue</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>2</td>    </tr>    <tr>      <th>1</th>      <td>4</td>    </tr>    <tr>      <th>2</th>      <td>5</td>    </tr>  </tbody></table>