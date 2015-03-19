1. Redesign layer structure
2. Sort id/names for multiline output.  
3. How do I deal with it as input?
4. Generic API for multi-models, joins etc.
5. Develop more output templates.
6. More generic application methods.
7. Best way to use custom functionality?
8. Add in database introspection to create admin interface.
9. Inject js into output for validation, other jquery shit?
10. Plan work for next few weeks
11. Integrate REST framework
12. Test out delete with json, line 243, cam_apps.py
13. Sort out question and question_group views.
14. Changing strings to dates etc. needs to be done by custom shit as you need to which string is a date.
15. Set up fieldsets on Volunteer admin. (24 mins 39 secs into video)
16. Maybe have a surgery view have a list of read-only volunteers (28 mins 34 secs)
17. Extend primary secondary generic table method and what's needed.
18. Pass a generic SQL statement and return result.


XML -> Application Object

Request -> View

Data -> Object or functions?  Can we have something generic here.

Custom logic -> how does it fit in?

##Requests Process
1. request comes in
2. View processes request and gets section, question_group, question from Application object?  When should the data be bound to this?  
3. Bind data to Application object in data layer.
4. Custom logic called wherever needed?
