# simu

![license](https://img.shields.io/github/license/uncle-lv/simu) ![stars](https://img.shields.io/github/stars/uncle-lv/simu) ![issues](https://img.shields.io/github/issues/uncle-lv/simu) ![forks](https://img.shields.io/github/forks/uncle-lv/simu) ![python version](https://img.shields.io/badge/python-3.7.0-blue)

一个模拟数据生成器



## 安装

请确保你电脑安装了 Python 环境和 pip

```bash
$ pip install simu
```



## 使用说明

### 随机数（random）

#### 常量（constant）

```python
DEFAULT_MAX = 1 << 12       # 默认最大值
DEFAULT_MIN = -DEFAULT_MAX  # 默然最小值
DEFAULT_SIZE = 10           # 默认列表长度
```



#### 布尔值（boolean）

##### random.*boolean()*

返回一个随机布尔值



##### random.*booleans(size: int = DEFAULT_SIZE)*

返回一个随机布尔值列表



参数列表：

| 参数 |   描述   | 默认值 |        可选        |
| :--: | :------: | :----: | :----------------: |
| size | 列表长度 |   10   | :heavy_check_mark: |



#### 自然数（natural number）

##### random.*natural(min: int = 0, max: int = DEFAULT_MAX)*

返回一个随机自然数



参数列表：

| 参数 |   描述   | 默认值 |        可选        |
| :--: | :------: | :----: | :----------------: |
| min  | 取值下限 |   0    | :heavy_check_mark: |
| max  | 取值上限 |  4096  | :heavy_check_mark: |



##### random.*naturals(min: int = 0, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

返回一个随机自然数列表



参数列表：

| 参数 |   描述   | 默认值 |        可选        |
| :--: | :------: | :----: | :----------------: |
| min  | 取值下限 |   0    | :heavy_check_mark: |
| max  | 取值上限 |  4096  | :heavy_check_mark: |
| size | 列表长度 |   10   | :heavy_check_mark: |



#### 整数（integer）

##### random.*integer(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX)*

返回一个随机整数



参数列表：

| 参数 |   描述   | 默认值 |        可选        |
| :--: | :------: | :----: | :----------------: |
| min  | 取值下限 | -4096  | :heavy_check_mark: |
| max  | 取值上限 |  4096  | :heavy_check_mark: |



##### random.*integers(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

返回一个随机整数列表



参数列表：

| 参数 |   描述   | 默认值 |        可选        |
| :--: | :------: | :----: | :----------------: |
| min  | 取值下限 | -4096  | :heavy_check_mark: |
| max  | 取值上限 |  4096  | :heavy_check_mark: |
| size | 列表长度 |   10   | :heavy_check_mark: |



#### 浮点数（floating number）

##### random.*floating(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2)*

返回一个随机浮点数



参数列表：

|  参数   |               描述                | 默认值 |        可选        |
| :-----: | :-------------------------------: | :----: | :----------------: |
|   min   |             取值下限              | -4096  | :heavy_check_mark: |
|   max   |             取值上限              |  4096  | :heavy_check_mark: |
| ndigits | 保留到小数点后 *n* 位（四舍五入） |   2    | :heavy_check_mark: |



##### random.*floatings(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2, size: int = DEFAULT_SIZE)*

返回一个随机浮点数列表



参数列表：

|  参数   |               描述                | 默认值 |        可选        |
| :-----: | :-------------------------------: | :----: | :----------------: |
|   min   |             取值下限              | -4096  | :heavy_check_mark: |
|   max   |             取值上限              |  4096  | :heavy_check_mark: |
| ndigits | 保留到小数点后 *n* 位（四舍五入） |   2    | :heavy_check_mark: |
|  size   |             列表长度              |   10   | :heavy_check_mark: |



#### 字符（character）

##### random.*char(pool: str = string.ascii_letters)*

从字符池中返回一个字符



参数列表：

| 参数 |  描述  |                            默认值                            |        可选        |
| :--: | :----: | :----------------------------------------------------------: | :----------------: |
| pool | 字符池 | *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)* | :heavy_check_mark: |



#### 字符串（string）

##### random.*string(pool: str = string.ascii_letters, min: int = 3, max: int = 10)*

返回一个由字符池中的字符随机组成的字符串



参数列表：

| 参数 |      描述      |                            默认值                            |        可选        |
| :--: | :------------: | :----------------------------------------------------------: | :----------------: |
| pool |     字符池     | *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)* | :heavy_check_mark: |
| min  | 字符串长度下限 |                              3                               | :heavy_check_mark: |
| max  | 字符串长度上限 |                              10                              | :heavy_check_mark: |

