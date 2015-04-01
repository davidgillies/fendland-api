1. Redesign layer structure
2. Sort id/names for multiline output.  
3. How do I deal with it as input?
4. Generic API for multi-models, joins etc.
5. Develop more output templates.
6. More generic application methods.
7. Best way to use custom functionality?
8. Inject js into output for validation, other jquery shit?
9. Changing strings to dates etc. needs to be done by custom shit as you need to which string is a date.
10. Extend primary, secondary generic table method and what's needed.
11. Pass a generic SQL statement and return result.
12. if models set to true redirect to url for rest framework?
13. Perhaps use convertion for whatever query I get e.g. post or json etc. and just forward to a view?
14. Add in choices to sex etc. admin screens.
15. Data visualization in a canvas?
16. Try out Django CBV and Forms to build default object views for models with a bootstrap template. 
17. Do validation against Application object, derived from XML and possibly from models if you use models.  Could use forms for this, or directly via models and forms...??
18. Form based validation for html posts, what about API?
19. Add new appointment button or something on template.  It needs to know it's a mutli.
20. modified_by should match up to User model for models but not for tomcat...
21. How will validation work in interface?
22. If you know datetime objects are there from Question data type, you have to know that when modifying data to strings and back to dates etc.
23. Need to return errors to frontend for models.


XML -> Application Object

Request -> View

Data -> Object or functions?  Can we have something generic here.

Custom logic -> how does it fit in?

##Requests Process
1. request comes in
2. View processes request and gets section, question_group, question from Application object?  When should the data be bound to this?  
3. Bind data to Application object in data layer.
4. Custom logic called wherever needed?
