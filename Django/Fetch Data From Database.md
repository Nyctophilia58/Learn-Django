
To fetch data from models we need functions. For example `home` function. Whenever we want to fetch the data from a model first go inside the model and the model will have objects and then we actually put the query to get all the data inside the table. Based on conditions you can use `get` or `filters` instead of `all` function.


create a context dictionary to pass the data to the html file. 
```html
{% for employee in employees %}

	<tr>
	
	<th scope="row">{{ employee.id }}</th>
	
	<td>{{ employee.first_name }} {{ employee.last_name }}</td>
	
	<td>{{ employee.designation }}</td>
	
	<td>+880{{ employee.phone_number }}</td>
	
	</tr>

{% endfor %}
```




