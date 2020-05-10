# Deep Learning

```py
weight = 0.1

def neural_network(input, weight):
    prediction = input * weight;
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
# 8.5
input = number_of_toes[0]
pred = neural_network(input, weight)
# 8.5 * 0.1 = 0.85
print(pred)
```
