# simu

![license](https://img.shields.io/github/license/uncle-lv/simu) ![stars](https://img.shields.io/github/stars/uncle-lv/simu) ![issues](https://img.shields.io/github/issues/uncle-lv/simu) ![forks](https://img.shields.io/github/forks/uncle-lv/simu) ![python version](https://img.shields.io/badge/python-3.7.0-blue)

A simulation data generator



## Install

Please ensure you have installed Python and pip on your personal computer.

```bash
$ pip install simu
```



### Usage

### Random

#### Constants

```python
DEFAULT_MAX = 1 << 12       # the default maximum
DEFAULT_MIN = -DEFAULT_MAX  # the default minimum
DEFAULT_SIZE = 10           # the default length of list
```



#### Boolean

##### random.*boolean()*

return a random boolean value



##### random.*booleans(size: int = DEFAULT_SIZE)*

return a list of random boolean values



parameter list:

| parameter |    description     | default |      optional      |
| :-------: | :----------------: | :-----: | :----------------: |
|   size    | the length of list |   10    | :heavy_check_mark: |



#### Natural number

##### random.*natural(min: int = 0, max: int = DEFAULT_MAX)*

return a random natural number



parameter list:

| parameter | description | default |      optional      |
| :-------: | :---------: | :-----: | :----------------: |
|    min    | lower limit |    0    | :heavy_check_mark: |
|    max    | upper limit |  4096   | :heavy_check_mark: |



##### random.*naturals(min: int = 0, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

return a list of natural numbers



parameter list:

| parameter |    description     | default |      optional      |
| :-------: | :----------------: | :-----: | :----------------: |
|    min    |    lower limit     |    0    | :heavy_check_mark: |
|    max    |    upper limit     |  4096   | :heavy_check_mark: |
|   size    | the length of list |   10    | :heavy_check_mark: |



#### Integer

##### random.*integer(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX)*

return a random integer



parameter list:

| parameter | description | default |      optional      |
| :-------: | :---------: | :-----: | :----------------: |
|    min    | lower limit |  -4096  | :heavy_check_mark: |
|    max    | upper limit |  4096   | :heavy_check_mark: |



##### simu.random.*integers(min: int = DEFAULT_MIN, max: int = DEFAULT_MAX, size: int = DEFAULT_SIZE)*

return a list of random integers



parameter list:

| parameter |    description     | default |      optional      |
| :-------: | :----------------: | :-----: | :----------------: |
|    min    |    lower limit     |  -4096  | :heavy_check_mark: |
|    max    |    upper limit     |  4096   | :heavy_check_mark: |
|   size    | the length of list |   10    | :heavy_check_mark: |



#### Floating number

##### random.*floating(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2)*

return a random floating number



parameter list:

| parameter |                      description                       | default |      optional      |
| :-------: | :----------------------------------------------------: | :-----: | :----------------: |
|    min    |                      lower limit                       |  -4096  | :heavy_check_mark: |
|    max    |                      upper limit                       |  4096   | :heavy_check_mark: |
|  ndigits  | rounded to *ndigits* precision after the decimal point |    2    | :heavy_check_mark: |



##### random.*floatings(min: float = DEFAULT_MIN, max: float = DEFAULT_MAX, ndigits: int = 2, size: int = DEFAULT_SIZE)*

return a list of random floating numbers



parameter list:

| parameter |                      description                       | default |      optional      |
| :-------: | :----------------------------------------------------: | :-----: | :----------------: |
|    min    |                      lower limit                       |  -4096  | :heavy_check_mark: |
|    max    |                      upper limit                       |  4096   | :heavy_check_mark: |
|  ndigits  | rounded to *ndigits* precision after the decimal point |    2    | :heavy_check_mark: |
|   size    |                   the length of list                   |   10    | :heavy_check_mark: |



#### Character

##### random.*string(pool: str = string.ascii_letters, min: int = 3, max: int = 10)*

return a random character from the character pool



parameter list:

| parameter |  description   |                           default                            |      optional      |
| :-------: | :------------: | :----------------------------------------------------------: | :----------------: |
|   pool    | character pool | *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)* | :heavy_check_mark: |



#### String

##### random.*string(pool: str = string.ascii_letters, min: int = 3, max: int = 10)*

return a string which consists of the characters from the character pool



parameter list:

| parameter |         description          |                           default                            |      optional      |
| :-------: | :--------------------------: | :----------------------------------------------------------: | :----------------: |
|   pool    |        character pool        | *[string.ascii_letters](https://docs.python.org/3/library/string.html?highlight=ascii_letter#string.ascii_letters)* | :heavy_check_mark: |
|    min    | the minimum length of string |                              3                               | :heavy_check_mark: |
|    max    | the maximum length of string |                              10                              | :heavy_check_mark: |

