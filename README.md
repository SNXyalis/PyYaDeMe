### Deep merge YAML module

## What does it do
It takes a list of yaml files and merge it into one.
If there are common keys, the children keys will be nested
in the common parent key.

## Example

| | Input 1: | |
| en: |
|   activity: |
|     morning: |
|       wakeup: "wake up" |
|       work: "go to work" |
|     evening: |
|       watch: "watch tv" |
|       sleep: "sleep" |
|   status:  |
|     healthy: "healthy" |


| | Input 2: | |
| en: |
|   activity: |
|     morning: |
|       feed: "feed the dog" |
|       pat: "pat the cat" |
|   holiday: |
|     hawaii: "go to hawaii" |
|   Christmas: |
|     gifts: |
|       chocolate: "Hot Chocolate" |
| el: |
|   greetings: "Geia!" |

| | Output: | |
| en: |
|   activity: |
|     morning: |
|       wakeup: "wake up" |
|       work: "go to work" |
|       feed: "feed the dog" |
|       pat: "pat the cat" |
|     evening: |
|       watch: "watch tv" |
|       sleep: "sleep" |
|   holiday: |
|     hawaii: "go to hawaii" |
|   Christmas: |
|     gifts: |
|       chocolate: "Hot Chocolate" |
|   status:  |
|     healthy: "healthy"   |
| el: |
|   greetings: "Geia!" |

