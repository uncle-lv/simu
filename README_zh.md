# mock

![license](https://img.shields.io/github/license/uncle-lv/mock) ![stars](https://img.shields.io/github/stars/uncle-lv/mock) ![issues](https://img.shields.io/github/issues/uncle-lv/mock) ![forks](https://img.shields.io/github/forks/uncle-lv/mock) ![python version](https://img.shields.io/badge/python-3.7.0-blue)

一个模拟数据生成库



## 使用说明

### 随机数（random）

#### 常量（constant）

```python
DEFAULT_MAX = 1 << 12       // 默认最大值
DEFAULT_MIN = -DEFAULT_MAX  // 默然最小值
DEFAULT_SIZE = 10           // 默认列表长度
```



#### 布尔值（boolean）

##### mock.rand.*boolean()*

返回一个随机布尔值



##### mock.rand.*booleans(size: int = DEFAULT_SIZE)*

返回一个随机布尔值



**size**：可选参数，表示列表长度。默认值为 10



#### 自然数（natural number）

##### mock.rand.*natural(min: int = 0, max: int = DEFAULT_MAX)*

返回一个随机自然数



**min**：可选参数，表示取值下限。默认值为 0

**max**：可选参数，表示取值上限。默认值为 4096



##### mock.rand.*naturals(min: int = 0, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

返回一个随机自然数列表



**min**：可选参数，表示取值下限。默认值为 0

**max**：可选参数，表示取值上限。默认值为 4096

**size**：可选参数，表示列表长度。默认值为 10



#### 整数（integer）

##### mock.rand.*integer(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX)*

返回一个随机整数



**min**：可选参数，表示取值下限。默认值为 -4096

**max**：可选参数，表示取值上限。默认值为 4096



##### mock.rand.*integers(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

返回一个随机整数列表



**min**：可选参数，表示取值下限。默认值为 -4096

**max**：可选参数，表示取值上限。默认值为 4096

**size**：可选参数，表示列表长度。默认值为 10



#### 浮点数（floating number）

##### mock.rand.*floating(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2)*

返回一个随机浮点数



**min**：可选参数，表示取值下限。默认值为 -4096

**max**：可选参数，表示取值上限。默认值为 4096

**n**：可选参数，表示保留到小数点后 *n* 位（四舍五入）。默认值为 2



##### mock.rand.*floatings(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2, size: int = DEFAULT_SIZE)*

返回一个随机浮点数列表



**min**：可选参数，表示取值下限。默认值为 -4096

**max**：可选参数，表示取值上限。默认值为 4096

**n**：可选参数，表示保留到小数点后 *n* 位（四舍五入）。默认值为 2

**size**：可选参数，表示列表长度。默认值为 10



#### 字符（character）

##### mock.rand.*char(pool: str = string.ascii_letters)*

从字符池中返回一个字符



**pool**：可选参数，表示字符池，将从中选择一个字符返回。默认值为 *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)*



#### 字符串（string）

##### mock.rand.*string(pool: str = string.ascii_letters, min: int = 3, max: int = 10)*

返回一个由字符池中的字符随机组成的字符串



**pool**：可选参数，表示字符池，将从中选择一个字符返回。默认值为 *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)*

**min**：可选参数，表示字符串长度下限。默认值为 3

**max**：可选参数，表示字符串长度上限。默认值为 10