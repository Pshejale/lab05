## Known Issue Table
| **Issue**                              | **Type**              | **Line(s)**                       | **Description**                                                  | **Fix Approach**                                                                 |
| -------------------------------------- | --------------------- | --------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Mutable default argument               | Bug                   | 8                                 | `logs=[]` shared across function calls                           | Change default to `None` and initialize list inside the function                 |
| Missing module and function docstrings | Documentation         | 1, 8, 14, 22, 25, 31, 36, 41, 48  | Functions and module lack docstrings                             | Add meaningful docstrings to describe purpose of module and functions            |
| Function names not in `snake_case`     | Style                 | 8, 14, 22, 25, 31, 36, 41         | Function names like `addItem`, `removeItem` violate PEP 8 naming | Rename using lowercase with underscores (e.g., `add_item`, `remove_item`)        |
| Unused import                          | Style                 | 2                                 | `logging` imported but not used                                  | Remove the unused import                                                         |
| Bare `except:` used                    | Code Smell / Security | 19                                | No exception type specified (`except:` hides all errors)         | Replace with specific exception type (`except KeyError as e:`) and log the error |
| Use of `eval()`                        | Security              | 59                                | `eval()` executes arbitrary code, unsafe                         | Remove or replace with safer alternative (`ast.literal_eval()` or omit entirely) |
| File not closed safely                 | Bug / Security        | 26, 32                            | File opened using `open()` without context manager               | Use `with open(file, 'r', encoding='utf-8') as f:` to safely handle files        |
| Global variable used                   | Code Smell            | 27                                | Use of `global stock_data`                                       | Refactor to pass data as parameter or encapsulate in class                       |
| Missing `encoding` in file operations  | Best Practice         | 26, 32                            | `open()` used without specifying encoding                        | Specify encoding explicitly (`encoding='utf-8'`)                                 |
| Missing blank lines between functions  | Formatting            | 8, 14, 22, 25, 31, 36, 41, 48, 61 | Violates PEP 8 layout guidelines                                 | Add 2 blank lines before and after top-level function definitions                |

### Summary
  - Total issues identified: 10
  - High severity: Use of eval()
  - Medium severity: Bare except:, file handling without context, mutable default argument
  - Low severity: Naming conventions, docstrings, formatting, unused import
