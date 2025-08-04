# Transforming Ordinal Attributes {Encoding}

## Description

Ordinal attributes are categorical attributes with a sense of order among the values.

Shoe sizes, education levels, and employment roles are some examples of ordinal categorical attributes.

## Example

In general, there is no generic module or function to map and transform these features into numeric representations based on order automatically.

Hence we can use a custom encoding/mapping scheme.

```python
gen_ord_map = {'Gen 1': 1, 'Gen 2': 2, 'Gen 3': 3,
               'Gen 4': 4, 'Gen 5': 5, 'Gen 6': 6}

poke_df['GenerationLabel'] = poke_df['Generation'].map(gen_ord_map)
```
