# Go

## Links

- [Standard Go Project Layout](https://github.com/golang-standards/project-layout)

## Projects

- [Hexagonal architecture - Banking](https://github.com/ashishjuyal/banking)
- [Hexagonal architecture - Banking Auth](https://github.com/ashishjuyal/banking-auth)
- [Gin framework, gRPC - Simplebank](https://github.com/techschool/simplebank)

## Data Types

- Integer:

  | Data Type | Description                                            | Range                                       | Memory Size |
  | --------- | ------------------------------------------------------ | ------------------------------------------- | ----------- |
  | uint8     | Unsigned 8-bit integer                                 | 0 to 255                                    | 1 byte      |
  | uint16    | Unsigned 16-bit integer                                | 0 to 65535                                  | 2 bytes     |
  | uint32    | Unsigned 32-bit integer                                | 0 to 4294967295                             | 4 bytes     |
  | uint64    | Unsigned 64-bit integer                                | 0 to 18446744073709551615                   | 8 bytes     |
  | uint      | uint32 in 32 bit systems<br />uint64 in 64 bit systems |                                             |             |
  | int8      | Signed 8-bit integer                                   | -128 to 127                                 | 1 byte      |
  | int16     | Signed 16-bit integer                                  | -32768 to 32767                             | 2 bytes     |
  | int32     | Signed 32-bit integer                                  | -2147483648 to 2147483647                   | 4 bytes     |
  | int64     | Signed 64-bit integer                                  | -9223372036854775808 to 9223372036854775807 | 8 bytes     |
  | int       | int32 in 32 bit systems<br />int64 in 64 bit systems   |                                             |             |

- Float:

  | Data Type  | Description                                          | Range                  | Memory Size |
  | ---------- | ---------------------------------------------------- | ---------------------- | ----------- |
  | float32    | 32-bit signed floating-point number                  | -3.4e+38 to 3.4e+38    | 4 bytes     |
  | float64    | 64-bit signed floating-point number                  | -1.7e+308 to +1.7e+308 | 8 bytes     |
  | complex64  | Complex number with float32 real and imaginary parts |                        |             |
  | complex128 | Complex number with float64 real and imaginary parts |                        |             |

- String:

  | Data Type | Description                                      |
  | --------- | ------------------------------------------------ |
  | string    | Is used to store a sequence of characters (text) |

- Boolean:

  | Data Type | Description                            | Memory Size |
  | --------- | -------------------------------------- | ----------- |
  | bool      | Can only take the values true or false | 1 bit       |
