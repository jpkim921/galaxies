


## Steps:
- Get Data
    - get collection based on search keyword
    - get collection['metadata'] to get the total number of items. call it total_items
    - total_items/100 to get the number of pages
    - create function to randomly get two integers (pageNum, itemNum)
    - get item based on pageNum and itemNum
- Serve template
    - display image, title, and photocredit
    - use javascript to refresh the page with a new image every X seconds




## run app:
```bash
flask --app main --debug run
```