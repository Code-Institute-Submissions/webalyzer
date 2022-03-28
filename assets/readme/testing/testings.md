# Testings

## Regex

I used regex to filter out bad domains with non-valid characters and set requirements to include HTTP(s) as the beginning of the string. View the code here: [here](https://regex101.com/r/HJk3sf/1 "regex101.com/r/HJk3sf/1")

<br>

## Inputs

A lot of work has gone into the validation and checks of inputs. Things like lowering all letters, stripping any extra whitespace, and removing any spaces between letters. If statements to ensure that letters are valid only where intended.

| CONVERTION | NOT VALID INPUT |
|:--------:|:--------:|
| ![app-page](./converted-url-link-answer.jpg) | ![app-page](./not-valid-input.jpg) |

<br>

### Testing URL inputs

| VALID | INVALID |
|:--------:|:--------:|
| ![app-page](./if-url-valid.jpg) | ![app-page](./invalid-link.jpg) |

| 404 ERROR | FAILED TO PARSE | UNREACHABLE |
|:--------:|:--------:|:--------:|
| ![app-page](./404-error.jpg) | ![app-page](./failed-to-parse.jpg) | ![app-page](./site-cant-be-reached.jpg) |

<br>

### Testing Validation Code

| NO ERRORS | WITH ERRORS |
|:--------:|:--------:|
| ![app-page](./code-validation-with-no-errors.jpg) | ![app-page](./code-validation-with-errors.jpg) |

