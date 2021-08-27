# Python - Decorator練習

<img src="https://img.shields.io/badge/Python-exercise-green">

## 練習題目
假設已經存在一個func叫divide(也就是除法)
```python
def divide(n,  d):
       return n  / d
```

n, d分別代表分子、分母，若我們傳0進去分母，程式會出錯當掉。

請寫一個decorator 來修正這個問題，把它變成傳0進去分母的時候，會return 0，而不是當掉。

## 解決方式
`input`傳回來的值為字串，先用`int`或`float`轉為數字
```python
x = int(input('請輸入分子'))
y = int(input('請輸入分母'))
```
在`Decorator`中新增if、else判斷，分母為時0回傳0
```python
if d == 0 :
    return 0
else:
    return n  / d
```
function上打上名為`@zero`的Decorator並print出結果
```python
@zero
def divide(n,  d):
       return int(n  / d)

print(divide(x,y))
```
## 執行結果
![](https://raw.githubusercontent.com/westleft/Decorator/main/result.jpg)
