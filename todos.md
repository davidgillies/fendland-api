1. Redesign layer structure
2. How do I deal with it as input?
3. Generic API for sections.
4. Develop more output templates.
5. Inject js into output for validation, other jquery shit?
6. Changing strings to dates etc. needs to be done by custom shit as you need to which string is a date.
7. Pass a generic SQL statement and return result.
8. if models set to true redirect to url for rest framework?
9. Perhaps use conversion for whatever query I get e.g. post or json etc. and just forward to a view?
10. Data visualization in a canvas?
11. Try out Django CBV and Forms to build default object views for models with a bootstrap template. 
12. Form based validation for html posts, what about API?
13. Add new appointment button or something on template.  It needs to know it's a mutli.
14. modified_by should match up to User model for models but not for tomcat...
15. If you know datetime objects are there from Question data type, you have to know that when modifying data to strings and back to dates etc.
16. Need to return errors to frontend for models.
17. Need to add errors to select template etc.
18. Fix the select template Hack I did to match string to integer.
19. change over to showcase logs.
20. Add db.rollback() on a failure.
21. When the Queryset gets results stick them in a variable so they can be gotten again without running the query twice.
22. Subclass User?


XML -> Application Object

Request -> View

Data -> Object or functions?  Can we have something generic here.

Custom logic -> how does it fit in?

##Requests Process
1. request comes in
2. View processes request and gets section, question_group, question from Application object?  When should the data be bound to this?  
3. Bind data to Application object in data layer.
4. Custom logic called wherever needed?
