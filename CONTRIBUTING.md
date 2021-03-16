For New Contributors

The focus of the development is around two components: core.py and the flask app that serves as the interface.
The remaining tasks are to get the following working:
1) post_items: This should read from the item_data.db and take the items that don't have a post date, and posts them to grailed - this is a little complicated and requres familiarity with the site.

2) sales.html: This is where all the sales data from sales_data.db can be viewed and analyzed. It will consist of a table view, and a graph view.
-The table view should just list the sales_data.db information as a table in an orderly fashion.
-The graph view should show sales over time.

3) manage.html: This is where the user can view the information in their item_data.db - it should have a table laying out their templates and values of each field in the template, with a radio button to the far right to post the item

As you go through the code and run into issues, it may be helpful to other contributors if you update the troubleshooting.txt file with what helped you get past those issues. This will go a long way to creating a documentation page to help everyone understand the code base.

Otherwise, claim tasks and do your development on a new branch as described: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
