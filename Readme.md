# GALAXIES

Small app that uses NASA's api. Specifically NASA Image and Video Library. This little app is meant to help practice Flask and to access and serve API data. Will also use this to practice and review Javascript.

https://api.nasa.gov/
https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf

Goal is to display images of galaxies taken by NASA in the past 5 years and to use javascript to automatially refresh the page with a new image every 5 or so seconds.


## Steps:
- [x] Get Data
    - [x] get collection based on search keyword
    - [x] get collection['metadata'] to get the total number of items. call it total_items
    - [x] total_items/100 to get the number of pages
    - [x] create function to randomly get two integers (pageNum, itemNum)
    - [x] get item based on pageNum and itemNum
    - [x] create context from item
- [ ] Serve template
    - [x] display image, title, and photocredit
    - [ ] use javascript to refresh the page with a new image every X seconds




## run app:
```bash
flask --app main --debug run
```
