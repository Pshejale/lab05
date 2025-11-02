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

## Reflection
**1. Which issues were the easiest to fix, and which were the hardest? Why?**
-  Easiest fixes:
  The easiest issues to fix were PEP 8 formatting (missing blank lines, snake_case naming) and adding docstrings. These were straightforward because they only required stylistic adjustments suggested directly by   Flake8 and Pylint.

  - Hardest fixes:
    The most challenging issue was replacing the use of the global keyword and handling mutable default arguments. These required code restructuring to avoid shared state and improve modularity. Additionally,         replacing unsafe file handling with context managers (with open(...)) required careful changes to preserve functionality.

**2. Did the static analysis tools report any false positives? If so, describe one example.**
  - There were no major false positives, but Pylint’s “global-statement” warning was not a functional issue in this small script. It’s considered poor practice in larger applications, but acceptable here for simplicity. Thus, it can be treated as a false positive in context since the code still works as intended.

**3. How would you integrate static analysis tools into your actual software development workflow?**

- I would integrate static analysis tools as part of both local development and Continuous Integration (CI) processes:
  - Run Pylint, Flake8, and Bandit automatically before each commit using Git pre-commit hooks.
  - Include these tools in CI pipelines (e.g., GitHub Actions) to ensure code quality and security checks run on every pull request.
  - Configure a shared .pylintrc and .flake8 config file for consistent rules across the team.
  - Fail builds if critical security or logical errors (like eval() or bare except) are detected.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
  - The cleaned code became more secure, maintainable, and readable.
  - Replacing eval() and bare except blocks eliminated potential runtime risks.
  - Using f-strings, type validation, and structured logging made the output cleaner and debugging easier.
  - Adding docstrings and following PEP 8 naming conventions improved overall readability and professionalism.
  - The final Pylint score increased from 4.80/10 to 10/10, confirming a significant improvement in quality.
