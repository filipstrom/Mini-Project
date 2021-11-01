# mini-project

## Mini-project report
Medlemmar: Filip Ström, Isabel Silva Henriksson, Joakim Forsberg, Miliam Eliasson

Program: Civilingenjörsprogrammet i Teknisk Matematik

Kurs: 1DV501

Inlämningsdatum: 

## introduktion

I del tre skulle man använda sitt hash-set och sin bst-map förr att göra samma sak som i del ett. Man skulle räkna antalet unika ord i de två textfilerna med sitt hash-set.

```python
def make_HashSet(lst):
    hash_set = hs.HashSet()
    hash_set.init()
    for e in lst:
        hash_set.add(e)
    return hash_set

hash_set.size()
```
 Sedan skulle man printa de tio vanligaste orden i filerna som var fyra tecken eller längre med sin binary search tree-map. 

```python
 def most_common(bist, n):
    word_tuples = bist.as_list()
    valueSorted = (sorted(word_tuples, key=lambda word: word[1]))[::-1]
    for k, v in valueSorted[:n]:
        print(k, "    \t", v)
```

 Sedan skulle man göra två nya saker, man skulle printa den maximala storleken på "buckets" efter man fört in orden i hash-settet, och man skulle printa det absoluta djupet i sitt binary search tree efter orden förts in.

 ```python
    print("Hash set size:", hash_set.get_size())
    print("Max bucket size:", hash_set.max_bucket_size())
 ```


**holy grail words**---------------**english new words**             

|most common words   | count    |most common words | count|
|:------------------:|:-----:|:------------------:|:-----:|
| arthur             | 261| their           |6143|
|launcelot           | 101| about            |4606|
|knight              | 84 |there            |3926|
|galahad             | 81 |would            |3877|
|father              | 74 |people           |3799|
|bedevere            | 68 |which            |3571|
|knights             | 65 |after            |3014|
|robin               | 58 |years            |2984|
|guard               | 58 |first            |2887|
|right               | 57 |other            |2754|



