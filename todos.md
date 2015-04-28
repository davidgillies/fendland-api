1. Redesign layer structure
2. How do I deal with it as input?
3. Generic API for sections.
4. Develop more output templates.
5. Inject js into output for validation, other jquery shit?
6. Changing strings to dates etc. needs to be done by custom shit as you need to which string is a date.
7. if models set to true redirect to url for rest framework?
8. Perhaps use conversion for whatever query I get e.g. post or json etc. and just forward to a view?
9. Data visualization in a canvas?
10. Try out Django CBV and Forms to build default object views for models with a bootstrap template. 
11. Form based validation for html posts, what about API?
12. Add new appointment button or something on template.  It needs to know it's a mutli.
13. If you know datetime objects are there from Question data type, you have to know that when modifying data to strings and back to dates etc.
14. Need to return errors to frontend for models.
15. Need to add errors to select template etc.
16. Fix the select template Hack I did to match string to integer.
17. change over to showcase logs.
18. Add db.rollback() on a failure.
19. When the Queryset gets results stick them in a variable so they can be gotten again without running the query twice.
20. Subclass User?
21. Would it be worth giving error messages an html printout and making them objects?
22. http://django-uni-form.readthedocs.org/en/latest/index.html # outputs django forms as divs, worth a test.
23. New stuff that can tell you what apps are installed and what fields they have, it is an API which is now stable.
24. Form Media - you can add js/css widgets to forms as in admin.  Not sure how it works.
25. DRF error messaging.
26. Store templates in your database, try that.
27. check out template tags available now.
28. One suggested use case of managers was to have delete just mark things as deleted and have a manager return non-deleted objects.  
29. Change validation so app passes questions which have properties set for each rule, e.g. required, max_length etc.  Then compare values to question parameters, seems easier to do than what I've done so far.

XML -> Application Object

Request -> View

Data -> Object or functions?  Can we have something generic here.

Custom logic -> how does it fit in?

##Requests Process
1. request comes in
2. View processes request and gets section, question_group, question from Application object?  When should the data be bound to this?  
3. Bind data to Application object in data layer.
4. Custom logic called wherever needed?
