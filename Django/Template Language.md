
## Templates
A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

A template contains **variables**, which get replaced with values when the template is evaluated, and **tags**, which control the logic of the template.

Below is a minimal template that illustrates a few basics. Each element will be explained later in this document.

```html
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
	<h1>{{ section.title }}</h1>
	
	{% for story in story_list %}
		<h2>
		  <a href="{{ story.get_absolute_url }}">
		    {{ story.headline|upper }}
		  </a>
		</h2>
		<p>{{ story.tease|truncatewords:"100" }}</p>
	{% endfor %}
{% endblock %}
```


## Variables
Variables look like this: `{{ variable }}`.

When the template engine encounters a variable, it evaluates that variable and replaces it with the result.

Use a dot (`.`) to access attributes of a variable.

## Filters
You can modify variables for display by using **filters**.

Filters look like this: `{{ name|lower }}`. This displays the value of the `{{ name }}` variable after being filtered through the [`lower`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-lower) filter, which converts text to lowercase. Use a pipe (`|`) to apply a filter.
Filters can be “chained.” The output of one filter is applied to the next. `{{ text|escape|linebreaks }}` is a common idiom for escaping text contents, then converting line breaks to `<p>` tags.

Some filters take arguments. A filter argument looks like this: `{{ bio|truncatewords:30 }}`. This will display the first 30 words of the `bio` variable.

Filter arguments that contain spaces must be quoted; for example, to join a list with commas and spaces you’d use `{{ list|join:", " }}`.

Django provides about sixty built-in template filters. You can read all about them in the [built-in filter reference](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#ref-templates-builtins-filters). To give you a taste of what’s available, here are some of the more commonly used template filters:


***To know more , see [The Django template language](https://docs.djangoproject.com/en/6.0/ref/templates/language/).***