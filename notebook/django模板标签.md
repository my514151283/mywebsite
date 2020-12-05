if标签
```
{% if condition %}
...
{% endif %}
```

多个if标签
```
{% if condition1 %}
...
{% elif condition2 %}
...
{% else condition3 %}
...
{% endif %}
```

if支持and，or，not
```
{% if [not] condition1 and/or [not] condition2%}
...
{% endif %}
```

for标签
```
{% for l in list %}
{{l}}
{% endfor %}
```

反向迭代
```
{% for l in list reversed %}
{{l}}
{% endfor %}
```

ifequal/ifnotequal标签
```
{% ifequal user 'bxm' %}
...
{% else %}
...
{% endifequal %}
```

注释标签
```
{# ... #}
```

转化成小写
```
{{name|lower}}
```

首字母大写
```
{{name|first|upper}}
```

截取前30个词
```
{{name|truncatewords: "30"}}
```

addslashes: 添加反斜杠到任何反斜杠、单引号或者双引号前面。
date: 按指定的格式字符串参数格式化 date 或者 datetime 对象，实例
```
{{pub_date|date: "F j, Y"}}
length: 返回变量的长度
```

包含其他模板
```
{% include 'other.html' %}
```